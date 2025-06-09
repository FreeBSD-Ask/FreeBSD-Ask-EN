# 将 Markdown 翻译逻辑整合为完整 CLI 脚本，包含批处理、目录遍历、文件写入等功能

import sys
import os
import time
import requests
import mistune
from pathlib import Path
from typing import List
import concurrent.futures

API_BASE_URL = "http://localhost:5000"
TRANSLATE_ENDPOINT = f"{API_BASE_URL}/translate"
MAX_RETRIES = 5
RETRY_DELAY = 2
REQUEST_TIMEOUT = 90
CHUNK_SIZE = 4000
MAX_WORKERS = 2


def check_api_ready(base_url, retries=10, delay=5):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(f"{base_url}/languages", timeout=10)
            if response.status_code == 200:
                print(f"[✓] Translation API ready (attempt {attempt})", flush=True)
                return True
        except Exception as e:
            print(f"[!] API check attempt {attempt} failed: {str(e)}", flush=True)
        print(f"[...] Waiting for API... (attempt {attempt}/{retries})", flush=True)
        time.sleep(delay)
    print("[X] Translation API not ready after retries", flush=True)
    return False


def translate_text(text: str) -> str:
    headers = {"Content-Type": "application/json"}
    data = {"q": text, "source": "zh", "target": "en", "format": "text"}
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(TRANSLATE_ENDPOINT, json=data, headers=headers, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json().get("translatedText", "")
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise e


def translate_chunked(text: str) -> str:
    if len(text) <= CHUNK_SIZE:
        return translate_text(text)
    result = []
    for i in range(0, len(text), CHUNK_SIZE):
        result.append(translate_text(text[i:i + CHUNK_SIZE]))
        time.sleep(1)
    return ''.join(result)


def translate_children(nodes: List[dict]) -> List[dict]:
    for node in nodes:
        if node["type"] == "text":
            node["text"] = translate_chunked(node["text"])
        elif "children" in node:
            node["children"] = translate_children(node["children"])
    return nodes


def translate_ast(ast: List[dict]) -> List[dict]:
    translated_ast = []
    for node in ast:
        if node["type"] in {"paragraph", "heading", "block_quote", "list_item"}:
            node["children"] = translate_children(node.get("children", []))
        elif node["type"] == "list":
            node["children"] = [translate_ast(child)[0] for child in node["children"]]
        elif node["type"] == "table":
            node["header"] = [translate_children(cell) for cell in node["header"]]
            node["cells"] = [[translate_children(cell) for cell in row] for row in node["cells"]]
        elif node["type"] == "link":
            node["children"] = translate_children(node.get("children", []))
        elif "children" in node:
            node["children"] = translate_ast(node["children"])
        translated_ast.append(node)
    return translated_ast


def render_markdown(ast: List[dict]) -> str:
    def render_node(node, prefix=''):
        t = node['type']
        if t == 'heading':
            level = node['level']
            content = ''.join(render_node(child) for child in node.get('children', []))
            return f"{'#' * level} {content}\n"
        elif t == 'paragraph':
            return ''.join(render_node(child) for child in node.get('children', [])) + '\n\n'
        elif t == 'text':
            return node['text']
        elif t == 'block_code':
            return f"```{node.get('info') or ''}\n{node['text']}\n```\n\n"
        elif t == 'list':
            return ''.join(render_node(item) for item in node['children'])
        elif t == 'list_item':
            prefix = '- ' if not node.get("ordered") else '1. '
            content = ''.join(render_node(child) for child in node['children'])
            return f"{prefix}{content}\n"
        elif t == 'block_quote':
            body = ''.join(render_node(child) for child in node['children'])
            return '\n'.join(f"> {line}" for line in body.strip().splitlines()) + '\n\n'
        elif t == 'link':
            text = ''.join(render_node(child) for child in node.get('children', []))
            return f"[{text}]({node['link']})"
        elif t == 'image':
            alt = node.get('alt', '')
            src = node.get('src', '')
            return f"![{alt}]({src})"
        elif t == 'table':
            header_row = '| ' + ' | '.join(''.join(render_node(cell) for cell in col) for col in node['header']) + ' |'
            divider_row = '| ' + ' | '.join('---' for _ in node['header']) + ' |'
            body_rows = []
            for row in node['cells']:
                body = '| ' + ' | '.join(''.join(render_node(cell) for cell in col) for col in row) + ' |'
                body_rows.append(body)
            return '\n'.join([header_row, divider_row] + body_rows) + '\n\n'
        return ''

    return ''.join(render_node(n) for n in ast)


def process_markdown(md_text: str) -> str:
    parser = mistune.create_markdown(renderer=mistune.AstRenderer())
    ast = parser(md_text)
    translated_ast = translate_ast(ast)
    return render_markdown(translated_ast)


def process_file(input_path: str, output_path: str) -> bool:
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()
        translated = process_markdown(content)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated)
        print(f"[✓] Translated {input_path} -> {output_path}", flush=True)
        return True
    except Exception as e:
        print(f"[X] Error processing {input_path}: {str(e)}", flush=True)
        return False


def main():
    docs_dir = "./docs"
    translated_dir = "."

    if not os.path.exists(docs_dir):
        print(f"[!] Source directory not found: {docs_dir}", flush=True)
        sys.exit(1)

    if not check_api_ready(API_BASE_URL):
        sys.exit(1)

    file_tasks = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, docs_dir)
                output_path = os.path.join(translated_dir, rel_path)
                file_tasks.append((input_path, output_path))

    print(f"[*] Found {len(file_tasks)} files to translate", flush=True)

    success_count = 0
    failure_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(process_file, input_path, output_path): (input_path, output_path)
            for input_path, output_path in file_tasks
        }
        for future in concurrent.futures.as_completed(futures):
            input_path, _ = futures[future]
            try:
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1
            except Exception as e:
                print(f"[X] Unexpected error with {input_path}: {str(e)}", flush=True)
                failure_count += 1

    print(f"\nTranslation summary: {success_count} succeeded, {failure_count} failed", flush=True)
    if failure_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()

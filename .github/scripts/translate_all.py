#!/usr/bin/env python3
import os
import sys
import time
import requests
import concurrent.futures
import mistune

API_BASE_URL = "http://localhost:5000"
TRANSLATE_ENDPOINT = f"{API_BASE_URL}/translate"
MAX_RETRIES = 5
RETRY_DELAY = 2
REQUEST_TIMEOUT = 90
CHUNK_SIZE = 4000  # 每块字符数上限
MAX_WORKERS = 2   # 最大线程数


def check_api_ready(base_url, retries=10, delay=5):
    """检查翻译 API 是否就绪"""
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


def translate_text(text, max_retries=MAX_RETRIES):
    """翻译文本，带重试机制"""
    headers = {"Content-Type": "application/json"}
    data = {
        "q": text,
        "source": "zh",
        "target": "en",
        "format": "text"
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(
                TRANSLATE_ENDPOINT,
                json=data,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            result = response.json()
            return result.get("translatedText", "")
        except requests.exceptions.RequestException as e:
            print(f"[!] Translation attempt {attempt + 1} failed: {str(e)}", flush=True)
            if attempt < max_retries - 1:
                wait_time = RETRY_DELAY * (attempt + 1)
                print(f"[...] Retrying in {wait_time} seconds...", flush=True)
                time.sleep(wait_time)
                continue
            raise


def translate_ast(ast):
    """递归翻译 AST 中所有文本节点"""
    for node in ast:
        t = node.get("type")
        if t == "text":
            node["text"] = translate_text(node.get("text", ""))
        elif "children" in node and isinstance(node["children"], list):
            # 特殊处理表格节点children结构
            if t == "table":
                for section in node["children"]:
                    if "children" in section:
                        for row in section["children"]:
                            if "children" in row:
                                for cell in row["children"]:
                                    if "children" in cell:
                                        translate_ast(cell["children"])
            else:
                translate_ast(node["children"])
    return ast


def render_node(node):
    t = node.get("type")
    if t == "text":
        return node.get("text", "")
    elif t == "paragraph":
        return ''.join(render_node(child) for child in node.get("children", [])) + "\n\n"
    elif t == "heading":
        level = node.get("attrs", {}).get("level", 1)
        return f"{'#' * level} {''.join(render_node(c) for c in node.get('children', []))}\n\n"
    elif t == "block_code":
        lang = node.get("attrs", {}).get("info", "")
        return f"```{lang}\n{node.get('text', '')}\n```\n\n"
    elif t == "block_quote":
        body = ''.join(render_node(c) for c in node.get("children", []))
        return '\n'.join(f"> {line}" for line in body.strip().splitlines()) + "\n\n"
    elif t == "list":
        ordered = node.get("attrs", {}).get("ordered", False)
        result = []
        for i, item in enumerate(node.get("children", [])):
            bullet = f"{i+1}. " if ordered else "- "
            item_text = ''.join(render_node(c) for c in item.get("children", [])).strip()
            result.append(f"{bullet}{item_text}")
        return '\n'.join(result) + "\n\n"
    elif t == "link":
        text = ''.join(render_node(c) for c in node.get("children", []))
        url = node.get("attrs", {}).get("url", "")
        return f"[{text}]({url})"
    elif t == "image":
        alt = node.get("attrs", {}).get("alt", "")
        url = node.get("attrs", {}).get("url", "")
        return f"![{alt}]({url})"
    elif t == "table":
        rows = node.get("children", [])
        if not rows:
            return ""
        # 第一行是表头
        header = rows[0]
        header_cells = header.get("children", [])
        header_line = '| ' + ' | '.join(
            ''.join(render_node(c) for c in cell.get("children", [])) for cell in header_cells
        ) + ' |'
        divider = '| ' + ' | '.join('---' for _ in header_cells) + ' |'
        body_lines = []
        # 后续行是正文，注意行可能在section中
        if len(rows) > 1:
            body_section = rows[1]
            for row in body_section.get("children", []):
                line = '| ' + ' | '.join(
                    ''.join(render_node(c) for c in cell.get("children", [])) for cell in row.get("children", [])
                ) + ' |'
                body_lines.append(line)
        return '\n'.join([header_line, divider] + body_lines) + '\n\n'
    else:
        # 默认递归children
        return ''.join(render_node(c) for c in node.get("children", []))


def translate_markdown(content):
    """将整个 Markdown 文本解析、翻译、渲染回文本"""
    parser = mistune.create_markdown(renderer=mistune.AstRenderer())
    ast = parser(content)
    ast = translate_ast(ast)
    translated = ''.join(render_node(node) for node in ast)
    return translated


def process_file(input_path, output_path):
    """处理单个 Markdown 文件的翻译"""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > CHUNK_SIZE:
            # 长文本拆块翻译比较复杂，这里简单先整体翻译以免结构破坏
            translated_content = translate_markdown(content)
        else:
            translated_content = translate_markdown(content)

        if translated_content is None:
            print(f"[X] Failed to translate {input_path}", flush=True)
            return False

        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

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

    # 收集所有需要处理的文件
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

    # 使用线程池处理文件
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(process_file, input_path, output_path): (input_path, output_path)
            for input_path, output_path in file_tasks
        }

        for future in concurrent.futures.as_completed(futures):
            input_path, output_path = futures[future]
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

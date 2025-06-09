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
MAX_WORKERS = 2    # 最大线程数


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


def translate_text(text, retries=MAX_RETRIES):
    """调用翻译接口，带重试"""
    headers = {"Content-Type": "application/json"}
    data = {"q": text, "source": "zh", "target": "en", "format": "text"}

    for attempt in range(retries):
        try:
            response = requests.post(
                TRANSLATE_ENDPOINT,
                json=data,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            return response.json().get("translatedText", "")
        except Exception as e:
            print(f"[!] Translate attempt {attempt+1} failed: {e}", flush=True)
            if attempt < retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
    return text  # 失败时返回原文，避免丢失内容


def translate_ast(ast):
    """递归翻译 AST 中所有文本节点"""
    for node in ast:
        t = node["type"]
        if t == "text":
            node["text"] = translate_text(node["text"])
        elif "children" in node:
            translate_ast(node["children"])
        elif t == "table":
            # 表格结构特殊处理：分区->行->单元格->children
            for section in node["children"]:
                for row in section["children"]:
                    for cell in row["children"]:
                        translate_ast(cell["children"])
    return ast


def render_node(node):
    t = node["type"]
    if t == "text":
        return node["text"]
    elif t == "paragraph":
        return ''.join(render_node(child) for child in node["children"]) + "\n\n"
    elif t == "heading":
        level = node["attrs"]["level"]
        return f"{'#' * level} {''.join(render_node(c) for c in node['children'])}\n\n"
    elif t == "block_code":
        lang = node["attrs"].get("info", "")
        return f"```{lang}\n{node['text']}\n```\n\n"
    elif t == "block_quote":
        body = ''.join(render_node(c) for c in node["children"])
        return '\n'.join(f"> {line}" for line in body.strip().splitlines()) + "\n\n"
    elif t == "list":
        ordered = node["attrs"].get("ordered", False)
        result = []
        for i, item in enumerate(node["children"]):
            bullet = f"{i+1}. " if ordered else "- "
            item_text = ''.join(render_node(c) for c in item["children"]).strip()
            result.append(f"{bullet}{item_text}")
        return '\n'.join(result) + "\n\n"
    elif t == "link":
        text = ''.join(render_node(c) for c in node["children"])
        return f"[{text}]({node['attrs']['url']})"
    elif t == "image":
        alt = node["attrs"].get("alt", "")
        url = node["attrs"]["url"]
        return f"![{alt}]({url})"
    elif t == "table":
        rows = node["children"]
        header = rows[0]
        header_line = '| ' + ' | '.join(
            ''.join(render_node(c) for c in cell["children"]) for cell in header["children"]
        ) + ' |'
        divider = '| ' + ' | '.join('---' for _ in header["children"]) + ' |'
        body_lines = []
        for row in rows[1]["children"]:
            line = '| ' + ' | '.join(
                ''.join(render_node(c) for c in cell["children"]) for cell in row["children"]
            ) + ' |'
            body_lines.append(line)
        return '\n'.join([header_line, divider] + body_lines) + '\n\n'
    else:
        return ''.join(render_node(c) for c in node.get("children", []))


def render_markdown(ast):
    return ''.join(render_node(node) for node in ast)


def translate_markdown(text):
    """将 Markdown 文本解析为 AST，递归翻译文本节点后渲染回 Markdown"""
    md = mistune.create_markdown(renderer="ast")
    ast = md(text)
    ast = translate_ast(ast)
    return render_markdown(ast)


def process_file(input_path, output_path):
    """处理单个 Markdown 文件，翻译后写入输出路径"""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 直接用 Markdown 结构化翻译，避免格式损失
        translated_content = translate_markdown(content)

        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

        print(f"[✓] Translated {input_path} -> {output_path}", flush=True)
        return True
    except Exception as e:
        print(f"[X] Error processing {input_path}: {e}", flush=True)
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
            input_path, output_path = futures[future]
            try:
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1
            except Exception as e:
                print(f"[X] Unexpected error with {input_path}: {e}", flush=True)
                failure_count += 1

    print(f"\nTranslation summary: {success_count} succeeded, {failure_count} failed", flush=True)
    if failure_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()

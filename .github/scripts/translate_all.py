#!/usr/bin/env python3
import os
import sys
import time
import requests
import concurrent.futures
from pathlib import Path

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


def translate_in_chunks(text, chunk_size=CHUNK_SIZE):
    """分块翻译大文本"""
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    translated_chunks = []

    for i, chunk in enumerate(chunks):
        print(f"[...] Translating chunk {i+1}/{len(chunks)}", flush=True)
        translated = translate_text(chunk)
        if translated is None:
            return None
        translated_chunks.append(translated)
        time.sleep(1)  # 稍微控制请求频率

    return "".join(translated_chunks)


def process_file(input_path, output_path):
    """处理单个 Markdown 文件的翻译"""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > CHUNK_SIZE:
            translated_content = translate_in_chunks(content)
        else:
            translated_content = translate_text(content)

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
    translated_dir = "./translated_docs"

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
#!/usr/bin/env python3
import os
import sys
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = "http://localhost:5000/translate"
MAX_RETRIES = 3
RETRY_DELAY = 5
REQUEST_TIMEOUT = 60
CHUNK_SIZE = 3000
MAX_WORKERS = 8  # 同时最多翻译几个文件，可调高

def check_api_ready(url, retries=10, delay=5):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(f"{url}/languages", timeout=10)
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
                API_URL,
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
            return None

def translate_in_chunks(text):
    chunks = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    translated_chunks = []
    for i, chunk in enumerate(chunks):
        print(f"[...] Translating chunk {i + 1}/{len(chunks)}", flush=True)
        translated = translate_text(chunk)
        if translated is None:
            return None
        translated_chunks.append(translated)
        time.sleep(0.5)  # 降低速率
    return "".join(translated_chunks)

def process_file(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        translated_content = translate_in_chunks(content) if len(content) > CHUNK_SIZE else translate_text(content)
        if translated_content is None:
            print(f"[X] Failed to translate {input_path}", flush=True)
            return False

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

        print(f"[✓] Translated {input_path} -> {output_path}", flush=True)
        return True
    except Exception as e:
        print(f"[X] Error processing {input_path}: {str(e)}", flush=True)
        return False

def main():
    docs_dir = "./docs"
    translated_root = "."  # 改成根路径

    if not os.path.exists(docs_dir):
        print(f"[!] Source directory not found: {docs_dir}", flush=True)
        sys.exit(1)

    if not check_api_ready(API_URL):
        sys.exit(1)

    file_tasks = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, docs_dir)
                output_path = os.path.join(translated_dir, rel_path)
                file_tasks.append((input_path, output_path))

    success_count = 0
    failure_count = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_file, inp, out): (inp, out) for inp, out in file_tasks}
        for future in as_completed(futures):
            inp, _ = futures[future]
            try:
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1
            except Exception as e:
                print(f"[X] Error in task for {inp}: {e}", flush=True)
                failure_count += 1

    print(f"\n[✓] Translation summary: {success_count} succeeded, {failure_count} failed", flush=True)
    if failure_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()

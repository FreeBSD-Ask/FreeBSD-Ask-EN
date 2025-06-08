import os
import sys
import time
import requests

API_URL = os.getenv("TRANSLATE_API_URL") or "http://localhost:5000/translate"

def check_api_ready(url, retries=5, delay=3):
    test_data = {
        "q": "测试",
        "source": "zh",
        "target": "en",
        "format": "text"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, data=test_data, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"[+] Translation API is ready (attempt {attempt})", flush=True)
                return True
            else:
                print(f"[!] Unexpected status code {response.status_code} on attempt {attempt}", flush=True)
        except Exception as e:
            print(f"[!] Attempt {attempt} failed: {e}", flush=True)

        time.sleep(delay)

    print("[X] Translation API is not ready after retries, exiting.", flush=True)
    sys.exit(1)

def translate_text(text):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "q": text,
        "source": "zh",
        "target": "en",
        "format": "text"
    }
    try:
        response = requests.post(API_URL, data=data, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get("translatedText", "")
    except Exception as e:
        print(f"[!] Translation failed: {e}", flush=True)
        return None

def main():
    docs_dir = "./docs"
    translated_dir = "./translated_docs"

    if not os.path.exists(translated_dir):
        os.makedirs(translated_dir)

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                doc_path = os.path.join(root, file)
                rel_path = os.path.relpath(doc_path, docs_dir)
                translated_path = os.path.join(translated_dir, rel_path)
                translated_folder = os.path.dirname(translated_path)
                if not os.path.exists(translated_folder):
                    os.makedirs(translated_folder)

                with open(doc_path, "r", encoding="utf-8") as f:
                    content = f.read()

                translated_content = translate_text(content)
                if translated_content is None:
                    print(f"[!] Skipping file due to translation failure: {doc_path}", flush=True)
                    continue

                with open(translated_path, "w", encoding="utf-8") as f:
                    f.write(translated_content)
                print(f"[+] Translated {doc_path} -> {translated_path}", flush=True)

if __name__ == "__main__":
    check_api_ready(API_URL)
    main()

import os
import sys
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = os.getenv("TRANSLATE_API_URL")
if not API_URL:
    API_URL = "http://localhost:5000/translate"
    print("[!] Warning: TRANSLATE_API_URL not set, using default:", API_URL, flush=True)


DOCS_DIR = Path("docs")
OUTPUT_DIR = Path(".")
MAX_WORKERS = 5
MAX_RETRIES = 5
CHECK_INTERVAL = 3  # 秒

def wait_for_service_ready():
    print("[i] Checking if translation service is ready...", flush=True)
    url = API_URL.replace("/translate", "/languages")
    for attempt in range(30):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print("[i] Translation service is ready!", flush=True)
                return True
        except Exception:
            pass
        print(f"[i] Waiting for service... retry {attempt + 1}/30", flush=True)
        time.sleep(CHECK_INTERVAL)
    print("[X] Translation service did not become ready in time.", flush=True)
    return False

def translate_text(text: str) -> str | None:
    try:
        response = requests.post(
            API_URL,
            data={
                "q": text,
                "source": "zh",
                "target": "en",
                "format": "text"
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("translatedText")
    except Exception as e:
        print(f"[!] Translation failed: {e}", flush=True)
        return None

def process_file(src_path: Path):
    rel_path = src_path.relative_to(DOCS_DIR)
    dest_path = OUTPUT_DIR / rel_path

    print(f"[*] Processing file: {src_path}", flush=True)
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    translated = translate_text(content)
    if translated is None:
        print(f"[!] Skipping (translation failed): {src_path}", flush=True)
        return False

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(translated)
    print(f"[✓] Wrote translated file: {dest_path}", flush=True)
    return True

def main():
    if not wait_for_service_ready():
        sys.exit(1)

    md_files = list(DOCS_DIR.rglob("*.md"))
    print(f"[i] Found {len(md_files)} markdown files in {DOCS_DIR}", flush=True)

    files_to_process = md_files
    success_files = set()
    retry_count = 0

    while files_to_process and retry_count < MAX_RETRIES:
        print(f"[i] Translation attempt {retry_count + 1}", flush=True)
        failed_files = []

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_file = {executor.submit(process_file, f): f for f in files_to_process}

            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    result = future.result()
                    if result:
                        success_files.add(file)
                    else:
                        failed_files.append(file)
                except Exception as e:
                    print(f"[!] Exception while processing {file}: {e}", flush=True)
                    failed_files.append(file)

        if failed_files:
            print(f"[!] {len(failed_files)} files failed to translate, retrying...", flush=True)
        else:
            print("[i] All files translated successfully!", flush=True)
            break

        files_to_process = failed_files
        retry_count += 1
        if retry_count < MAX_RETRIES:
            print(f"[i] Waiting {CHECK_INTERVAL}s before next retry...", flush=True)
            time.sleep(CHECK_INTERVAL)

    if files_to_process:
        print(f"[X] Failed to translate {len(files_to_process)} files after {MAX_RETRIES} attempts.", flush=True)
        for f in files_to_process:
            print(f" - {f}", flush=True)
    else:
        print(f"[✓] Successfully translated all {len(md_files)} files.", flush=True)

if __name__ == "__main__":
    main()

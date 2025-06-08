import os
import sys
import requests
from pathlib import Path

API_URL = os.getenv("TRANSLATE_API_URL")
if not API_URL:
    print("[X] ERROR: TRANSLATE_API_URL environment variable is not set.")
    sys.exit(1)

DOCS_DIR = Path("docs")
OUTPUT_DIR = Path(".")

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
        print(f"[!] Translation failed: {e}")
        return None

def process_file(src_path: Path):
    rel_path = src_path.relative_to(DOCS_DIR)
    dest_path = OUTPUT_DIR / rel_path

    print(f"[*] Processing file: {src_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    translated = translate_text(content)
    if translated is None:
        print(f"[!] Skipping (translation failed): {src_path}")
        return

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(translated)
    print(f"[✓] Wrote translated file: {dest_path}")

def main():
    md_files = list(DOCS_DIR.rglob("*.md"))
    print(f"[i] Found {len(md_files)} markdown files in {DOCS_DIR}")
    for idx, file_path in enumerate(md_files, 1):
        print(f"[{idx}/{len(md_files)}] Translating: {file_path}")
        process_file(file_path)

if __name__ == "__main__":
    main()

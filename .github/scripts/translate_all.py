import os
import requests
from pathlib import Path

TRANSLATE_API = os.getenv("TRANSLATE_API_URL")
if not TRANSLATE_API:
    raise RuntimeError("Environment variable TRANSLATE_API_URL is not set")

DOCS_DIR = Path("docs")
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

def translate_text(text):
    data = {
        "q": text,
        "source": "zh",
        "target": "en",
        "format": "text"
    }
    try:
        r = requests.post(TRANSLATE_API, data=data, timeout=10)
        r.raise_for_status()
        return r.json()["translatedText"]
    except Exception as e:
        print(f"[!] 翻译失败: {e}")
        return text

def translate_file(src_path, dst_path):
    content = src_path.read_text(encoding="utf-8")
    translated = translate_text(content)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text(translated, encoding="utf-8")
    print(f"✔️ Translated {src_path} -> {dst_path}")

def main():
    all_md_files = list(DOCS_DIR.rglob("*.md"))
    print(f"Found {len(all_md_files)} .md files in {DOCS_DIR}")

    for src_path in all_md_files:
        relative_path = src_path.relative_to(DOCS_DIR)
        dst_path = REPO_ROOT / relative_path
        translate_file(src_path, dst_path)

if __name__ == "__main__":
    main()

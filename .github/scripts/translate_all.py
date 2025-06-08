import os
import requests
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"
TRANSLATE_API = "https://libretranslate.com/translate"

def translate_text(text):
    if not text.strip():
        return ""
    response = requests.post(TRANSLATE_API, data={
        "q": text,
        "source": "zh",
        "target": "en",
        "format": "text"
    })
    response.raise_for_status()
    return response.json()["translatedText"]

def find_all_md_files():
    return list(DOCS_DIR.rglob("*.md"))

def main():
    all_md_files = find_all_md_files()
    print(f"Found {len(all_md_files)} .md files in /docs")

    for md_file in all_md_files:
        src_path = md_file
        with src_path.open("r", encoding="utf-8") as f:
            content = f.read()

        translated = translate_text(content)

        # Save to root project, keeping same structure but removing leading 'docs/'
        relative_path = md_file.relative_to(DOCS_DIR)
        target_path = REPO_ROOT / relative_path

        target_path.parent.mkdir(parents=True, exist_ok=True)
        with target_path.open("w", encoding="utf-8") as f:
            f.write(translated)

        print(f"Translated {md_file} -> {target_path}")

if __name__ == "__main__":
    main()

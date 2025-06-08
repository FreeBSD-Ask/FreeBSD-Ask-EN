import os
import subprocess
import requests
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"
TRANSLATE_API = "https://libretranslate.com/translate"

def get_changed_md_files():
    result = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True)
    changed_files = result.stdout.strip().split("\n")
    return [Path(f) for f in changed_files if f.endswith(".md") and f.startswith("docs/")]

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

def main():
    md_files = get_changed_md_files()
    for md_file in md_files:
        src_path = REPO_ROOT / md_file
        with src_path.open("r", encoding="utf-8") as f:
            content = f.read()

        translated = translate_text(content)

        # Remove leading 'docs/' from path
        relative_path = md_file.relative_to("docs")
        target_path = REPO_ROOT / relative_path

        # Create parent folders if needed
        target_path.parent.mkdir(parents=True, exist_ok=True)

        with target_path.open("w", encoding="utf-8") as f:
            f.write(translated)

        print(f"Translated {md_file} -> {target_path}")

if __name__ == "__main__":
    main()

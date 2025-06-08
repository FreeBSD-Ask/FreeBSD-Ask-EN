import os
import requests
from pathlib import Path
import sys

# 强制要求环境变量
API_URL = os.getenv("TRANSLATE_API_URL")
if not API_URL:
    print("[X] 未设置环境变量 TRANSLATE_API_URL")
    sys.exit(1)

DOCS_DIR = Path("docs")
OUTPUT_DIR = Path(".")

def translate_text(text: str) -> str:
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
        return response.json()["translatedText"]
    except Exception as e:
        print(f"[!] 翻译失败：{e}")
        return None

def process_file(src_path: Path):
    rel_path = src_path.relative_to(DOCS_DIR)
    dest_path = OUTPUT_DIR / rel_path

    print(f"[*] 处理文件：{src_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    translated = translate_text(content)
    if translated is None:
        print(f"[!] 跳过（翻译失败）：{src_path}")
        return

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(translated)
    print(f"[✓] 写入翻译文件：{dest_path}")

def main():
    all_md = list(DOCS_DIR.rglob("*.md"))
    print(f"[i] 共发现 {len(all_md)} 个 Markdown 文件")
    for i, file in enumerate(all_md, 1):
        print(f"[{i}/{len(all_md)}] 翻译中：{file}")
        process_file(file)

if __name__ == "__main__":
    main()

from pathlib import Path
from googletrans import Translator

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"

def find_all_md_files():
    return list(DOCS_DIR.rglob("*.md"))

def translate_text(text, translator):
    try:
        result = translator.translate(text, src="zh-cn", dest="en")
        return result.text
    except Exception as e:
        print(f"[!] 翻译失败：{e}")
        return text  # 出错时返回原文

def translate_file(content, translator):
    paragraphs = content.split("\n\n")
    translated = [translate_text(p, translator) for p in paragraphs]
    return "\n\n".join(translated)

def main():
    translator = Translator()
    all_md_files = find_all_md_files()
    print(f"Found {len(all_md_files)} .md files in /docs")

    for md_file in all_md_files:
        with md_file.open("r", encoding="utf-8") as f:
            content = f.read()

        translated = translate_file(content, translator)

        relative_path = md_file.relative_to(DOCS_DIR)
        target_path = REPO_ROOT / relative_path

        target_path.parent.mkdir(parents=True, exist_ok=True)
        with target_path.open("w", encoding="utf-8") as f:
            f.write(translated)

        print(f"✔️ Translated {md_file} -> {target_path}")

if __name__ == "__main__":
    main()

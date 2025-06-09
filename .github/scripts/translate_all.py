#!/usr/bin/env python3
import os
import sys
import time
import re
import html
import requests
import concurrent.futures
import mistune

API_BASE_URL    = "http://localhost:5000"
TRANSLATE_URL   = f"{API_BASE_URL}/translate"
MAX_RETRIES     = 5
RETRY_DELAY     = 2
REQUEST_TIMEOUT = 90
CHUNK_SIZE      = 3500
MAX_WORKERS     = 2
SENT_DELIMS     = r'[。！？.!?]'


def check_api_ready():
    for i in range(1, 11):
        try:
            r = requests.get(f"{API_BASE_URL}/languages", timeout=10)
            if r.status_code == 200:
                print(f"[✓] API ready (attempt {i})")
                return True
        except:
            pass
        print(f"[...] Waiting for API (attempt {i}/10)…")
        time.sleep(2)
    print("[X] API not ready.")
    return False


def translate_text(raw: str) -> str:
    # 清理控制字符
    txt = html.unescape(re.sub(r'[\x00-\x1F\x7F-\x9F]', '', raw))
    payload = {"q": txt, "source": "zh", "target": "en", "format": "text"}
    for i in range(MAX_RETRIES):
        try:
            r = requests.post(TRANSLATE_URL, json=payload,
                              headers={"Content-Type":"application/json"},
                              timeout=REQUEST_TIMEOUT)
            r.raise_for_status()
            return r.json().get("translatedText", "")
        except Exception as e:
            if i < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY*(i+1))
                continue
            print(f"[!] translate failed for text fragment:\n  {txt[:30]}... -> {e}")
            return raw  # 最后返回原文，避免丢失


def split_sentences(text: str) -> list[str]:
    parts = []
    last = 0
    for m in re.finditer(SENT_DELIMS, text):
        parts.append(text[last:m.end()])
        last = m.end()
    if last < len(text):
        parts.append(text[last:])
    return parts


def chunked_translate(text: str) -> str:
    segs = split_sentences(text)
    chunks, cur = [], ""
    for s in segs:
        if len(cur)+len(s) <= CHUNK_SIZE:
            cur += s
        else:
            chunks.append(cur); cur = s
    if cur: chunks.append(cur)

    out = []
    for i, c in enumerate(chunks, 1):
        out.append(translate_text(c))
        time.sleep(0.5)
    return "".join(out)


def translate_node_text(t: str) -> str:
    if not t.strip(): return t
    # 避免整行是 markdown 语法时乱翻
    if re.fullmatch(r'[\s`#*>\-\[\]\(\):.!0-9]+', t):
        return t
    return chunked_translate(t) if len(t) > CHUNK_SIZE else translate_text(t)


def translate_ast(nodes: list[dict]):
    for nd in nodes:
        tp = nd.get("type")
        # 直接文本
        if tp == "text":
            nd["text"] = translate_node_text(nd.get("text",""))
        # 链接：递归翻译显示文本
        elif tp == "link" and "children" in nd:
            translate_ast(nd["children"])
        # 图片：只翻译 alt 文本
        elif tp == "image" and "children" in nd:
            translate_ast(nd["children"])
        # 代码块/行内代码 跳过
        elif tp in ("code_block","codespan"):
            pass
        # 表格结构：children[0] header, children[1:] body
        elif tp == "table" and "children" in nd:
            for sec in nd["children"]:
                translate_ast(sec.get("children",[]))
        # 其他有 children 的节点
        elif "children" in nd:
            translate_ast(nd["children"])
    return nodes


def render_md(nodes: list[dict]) -> str:
    out = []
    def rd(n):
        tp = n.get("type")
        if tp == "text":
            return n.get("text","")
        if tp == "paragraph":
            return "".join(rd(c) for c in n["children"]) + "\n\n"
        if tp == "heading":
            lvl = n.get("attrs",{}).get("level",1)
            txt = "".join(rd(c) for c in n["children"])
            return f"{'#'*lvl} {txt}\n\n"
        if tp == "list":
            ol = n.get("attrs",{}).get("ordered",False)
            start = n.get("attrs",{}).get("start",1)
            res = []
            for i,item in enumerate(n["children"]):
                pre = f"{start+i}. " if ol else "- "
                txt = "".join(rd(c) for c in item.get("children",[])).strip()
                res.append(pre + txt.replace("\n","\n  "))
            return "\n".join(res) + "\n\n"
        if tp == "block_quote":
            txt = "".join(rd(c) for c in n["children"]).strip().splitlines()
            return "\n".join("> "+l for l in txt) + "\n\n"
        if tp == "code_block":
            inf = n.get("attrs",{}).get("info","")
            return f"```{inf}\n{n.get('text','')}```\n\n"
        if tp == "thematic_break":
            return "---\n\n"
        if tp == "link":
            txt = "".join(rd(c) for c in n.get("children",[]))
            url = n.get("link","")
            title = n.get("attrs",{}).get("title")
            tit = f' "{title}"' if title else ""
            return f"[{txt}]({url}{tit})"
        if tp == "image":
            alt = "".join(rd(c) for c in n.get("children",[]))
            url = n.get("link","")
            title = n.get("attrs",{}).get("title")
            tit = f' "{title}"' if title else ""
            return f"![{alt}]({url}{tit})"
        if tp == "table":
            rows = n.get("children",[])
            if not rows: return ""
            # header row
            hdr = rows[0]
            def row_txt(r):
                cells = r.get("children",[])
                texts = ["".join(rd(c) for c in cell.get("children",[])) for cell in cells]
                return "| " + " | ".join(texts) + " |"
            sep = "| " + " | ".join("---" for _ in hdr.get("children",[])) + " |"
            body = [row_txt(r) for r in rows[1:]]
            return row_txt(hdr) + "\n" + sep + "\n" + "\n".join(body) + "\n\n"
        # fallback：递归 children
        if "children" in n:
            return "".join(rd(c) for c in n["children"])
        return ""
    for node in nodes:
        out.append(rd(node))
    return "".join(out)


def translate_file(inp: str, outp: str) -> bool:
    try:
        txt = open(inp, encoding="utf-8").read()
        md = mistune.create_markdown(renderer="ast")
        ast = md(txt)
        translate_ast(ast)
        res = render_md(ast)
        os.makedirs(os.path.dirname(outp), exist_ok=True)
        open(outp, "w", encoding="utf-8").write(res)
        print(f"[✓] {inp} → {outp}")
        return True
    except Exception as e:
        print(f"[X] Error {inp}: {e}")
        return False


def main():
    if not check_api_ready():
        sys.exit(1)
    tasks=[]
    for r,_,fs in os.walk("./docs"):
        for f in fs:
            if f.endswith(".md"):
                ip = os.path.join(r,f)
                rp = os.path.relpath(ip,"./docs")
                op = os.path.join(".", rp)
                tasks.append((ip,op))
    print(f"[*] {len(tasks)} files found.")
    succ=fail=0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as e:
        futs={e.submit(translate_file,ip,op):(ip,op) for ip,op in tasks}
        for f in concurrent.futures.as_completed(futs):
            ok = f.result()
            succ += ok; fail += (not ok)
    print(f"\nSummary: {succ} succeeded, {fail} failed.")
    if fail: sys.exit(1)


if __name__ == "__main__":
    main()

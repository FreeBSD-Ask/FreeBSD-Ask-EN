#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import html
import requests
import concurrent.futures

API_BASE = "http://localhost:5000"
URL_LANGS = f"{API_BASE}/languages"
URL_TRANS = f"{API_BASE}/translate"

MAX_RETRIES = 5
RETRY_DELAY = 2
TIMEOUT = 90
CHUNK = 2000   # 分块大小，防止请求过长
MAX_WORKERS = 2

# 用于句子分割
SENT_PAT = re.compile(r'([。！？\.!\?])')

# 判断行是否是表格
is_table_line = lambda line: line.strip().startswith("|") and line.strip().endswith("|")

# 判断行是否是列表项
is_list_line = lambda line: re.match(r'^\s*([-*+]|\d+\.)\s+', line)

def check_api():
    for i in range(1, 6):
        try:
            r = requests.get(URL_LANGS, timeout=5)
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(1)
    print("[X] 翻译 API 无法访问，请检查")
    return False

def translate_chunk(text: str) -> str:
    """分块翻译长文本"""
    if not text.strip():
        return text
    # 按句子分割再重组
    parts = SENT_PAT.split(text)
    segments = []
    cur = ""
    for seg in parts:
        if len(cur) + len(seg) <= CHUNK:
            cur += seg
        else:
            if cur:
                segments.append(cur)
            cur = seg
    if cur: segments.append(cur)

    out = []
    for seg in segments:
        out.append(_translate_text(seg))
        time.sleep(0.2)
    return "".join(out)

def _translate_text(txt: str) -> str:
    """调用翻译接口"""
    # 清理控制字符
    clean = html.unescape(re.sub(r'[\x00-\x1F\x7F-\x9F]', '', txt))
    payload = {"q": clean, "source": "zh", "target": "en", "format": "text"}
    for i in range(MAX_RETRIES):
        try:
            r = requests.post(URL_TRANS, json=payload,
                              headers={"Content-Type":"application/json"},
                              timeout=TIMEOUT)
            r.raise_for_status()
            return r.json().get("translatedText","")
        except Exception as e:
            if i < MAX_RETRIES-1:
                time.sleep(RETRY_DELAY*(i+1))
            else:
                # 最后一次失败，返回原文以免丢失
                return txt
    return txt

def translate_line(line: str) -> str:
    """翻译单行文本，保留链接/图片结构"""
    # 先处理链接和图片
    def repl_link(m):
        text, url = m.group(1), m.group(2)
        tr = translate_chunk(text)
        return f"[{tr}]({url})"
    line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl_link, line)

    # 处理行内代码，不翻译
    code_spans = {}
    def repl_codespan(m):
        key = f"__CODESPAN_{len(code_spans)}__"
        code_spans[key] = m.group(0)
        return key
    line = re.sub(r'`[^`]+`', repl_codespan, line)

    # 再翻译剩余中文
    tr = translate_chunk(line)

    # 恢复行内代码
    for k,v in code_spans.items():
        tr = tr.replace(k, v)
    return tr

def process_block(block: list[str]) -> list[str]:
    """根据块类型处理"""
    if not block:
        return block
    # 代码块：``` 开始/结束 或 缩进四格
    if block[0].startswith("```"):
        return block  # 整块保留
    if all(line.startswith("    ") or line.startswith("\t") for line in block):
        return block  # 缩进代码块保留

    # 表格块
    if all(is_table_line(ln) or ln.strip().startswith(":") or ln.strip().startswith("---") for ln in block):
        # 第一行表头，第二行分隔符，后续行内容
        out = []
        for i, ln in enumerate(block):
            if i == 1 and re.match(r'^\s*\|[\s:-]+\|', ln):
                out.append(ln)  # 保留分隔符
            else:
                # 分割单元格
                parts = ln.split("|")
                # parts[0]和最后通常为空
                new = [parts[0]]
                for cell in parts[1:-1]:
                    new.append(" " + translate_chunk(cell.strip()) + " ")
                new.append(parts[-1])
                out.append("|".join(new))
        return out

    # 其他：逐行翻译
    return [ translate_line(ln) for ln in block ]

def translate_markdown(text: str) -> str:
    """把全文分块，然后分别处理，最后拼回"""
    lines = text.splitlines()
    res = []
    buf = []
    for ln in lines + [""]:
        # 以空行分块
        if ln.strip() == "":
            res.extend(process_block(buf))
            res.append("")  # 空行
            buf = []
        else:
            buf.append(ln)
    return "\n".join(res)

def work_file(src: str, dst: str) -> bool:
    try:
        txt = open(src, encoding="utf-8").read()
        out = translate_markdown(txt)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf-8").write(out)
        print(f"[✓] {src} → {dst}")
        return True
    except Exception as e:
        print(f"[X] Fail {src}: {e}")
        return False

def main():
    if not check_api():
        sys.exit(1)
    tasks = []
    for root, _, files in os.walk("./docs"):
        for fn in files:
            if fn.endswith(".md"):
                ip = os.path.join(root, fn)
                rp = os.path.relpath(ip, "./docs")
                op = os.path.join(".", rp)
                tasks.append((ip, op))
    print(f"[*] Found {len(tasks)} files")
    ok = fail = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = { ex.submit(work_file, i,o):(i,o) for i,o in tasks }
        for f in concurrent.futures.as_completed(futs):
            if f.result(): ok +=1
            else: fail+=1
    print(f"\nDone: {ok} ok, {fail} fail")
    if fail: sys.exit(1)

if __name__ == "__main__":
    main()

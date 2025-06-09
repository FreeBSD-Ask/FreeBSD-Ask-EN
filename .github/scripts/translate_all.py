#!/usr/bin/env python3
import os
import sys
import time
import requests
import concurrent.futures
import mistune
import re
import html

API_BASE_URL = "http://localhost:5000"
TRANSLATE_ENDPOINT = f"{API_BASE_URL}/translate"
MAX_RETRIES = 5
RETRY_DELAY = 2
REQUEST_TIMEOUT = 90
CHUNK_SIZE = 3500  # 减小分块大小防止400错误
MAX_WORKERS = 2
SENTENCE_DELIMITERS = r'[。！？.!?]'  # 句子分隔符

def check_api_ready(base_url, retries=10, delay=5):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(f"{base_url}/languages", timeout=10)
            if response.status_code == 200:
                print(f"[✓] Translation API ready (attempt {attempt})", flush=True)
                return True
        except Exception as e:
            print(f"[!] API check attempt {attempt} failed: {str(e)}", flush=True)

        print(f"[...] Waiting for API... (attempt {attempt}/{retries})", flush=True)
        time.sleep(delay)
    print("[X] Translation API not ready after retries", flush=True)
    return False

def translate_text(text, max_retries=MAX_RETRIES):
    headers = {"Content-Type": "application/json"}
    
    # 清理文本中的控制字符和非法Unicode
    cleaned_text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    cleaned_text = html.unescape(cleaned_text)
    
    data = {
        "q": cleaned_text,
        "source": "zh",
        "target": "en",
        "format": "text"
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(
                TRANSLATE_ENDPOINT,
                json=data,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            result = response.json()
            return result.get("translatedText", "")
        except requests.exceptions.HTTPError as e:
            # 捕获详细的错误信息
            error_detail = response.text if hasattr(response, 'text') else str(e)
            print(f"[!] Translation attempt {attempt+1} failed: HTTP {response.status_code} - {error_detail}", flush=True)
            if attempt < max_retries - 1:
                wait_time = RETRY_DELAY * (attempt + 1)
                print(f"[...] Retrying in {wait_time} seconds...", flush=True)
                time.sleep(wait_time)
                continue
            raise
        except requests.exceptions.RequestException as e:
            print(f"[!] Translation attempt {attempt+1} failed: {str(e)}", flush=True)
            if attempt < max_retries - 1:
                wait_time = RETRY_DELAY * (attempt + 1)
                print(f"[...] Retrying in {wait_time} seconds...", flush=True)
                time.sleep(wait_time)
                continue
            raise

def split_into_sentences(text):
    """按句子边界分块，保留分隔符"""
    sentences = []
    start = 0
    for match in re.finditer(SENTENCE_DELIMITERS, text):
        end = match.end()
        sentences.append(text[start:end])
        start = end
    if start < len(text):
        sentences.append(text[start:])
    return sentences

def chunk_text(text, max_chars=CHUNK_SIZE):
    """智能分块：先按句子分块，然后合并到最大字符数"""
    sentences = split_into_sentences(text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def translate_in_chunks(text):
    """改进的分块翻译逻辑"""
    chunks = chunk_text(text)
    if not chunks:
        return ""
    
    translated_chunks = []
    for i, chunk in enumerate(chunks):
        print(f"[...] Translating chunk {i+1}/{len(chunks)} (size: {len(chunk)} chars)", flush=True)
        translated = translate_text(chunk)
        if translated is None:
            # 如果失败，尝试更小的分块
            if len(chunk) > 500:
                print(f"[!] Retrying with smaller chunks for failed chunk", flush=True)
                sub_chunks = chunk_text(chunk, max_chars=500)
                for j, sub_chunk in enumerate(sub_chunks):
                    print(f"  [...] Sub-chunk {j+1}/{len(sub_chunks)}", flush=True)
                    sub_trans = translate_text(sub_chunk)
                    if sub_trans:
                        translated_chunks.append(sub_trans)
                    else:
                        translated_chunks.append(f"[TRANSLATION FAILED: {sub_chunk[:50]}...]")
            else:
                translated_chunks.append(f"[TRANSLATION FAILED: {chunk[:50]}...]")
        else:
            translated_chunks.append(translated)
        time.sleep(0.5)  # 减少API压力
    
    return "".join(translated_chunks)

def translate_text_node(text):
    if not text.strip():
        return text
        
    # 跳过代码块和特殊格式的翻译
    if re.match(r'^[\s`#*\-|:>0-9]+$', text):
        return text
        
    if len(text) > 1000:
        return translate_in_chunks(text)
    else:
        return translate_text(text)

# 递归处理 AST，翻译所有文本节点，特殊结构保留格式
def translate_ast_nodes(ast_nodes):
    for node in ast_nodes:
        t = node['type']
        # 对 text 节点翻译
        if t == 'text':
            original_text = node.get('text', '')
            translated = translate_text_node(original_text)
            node['text'] = translated
        # 对链接节点，翻译显示文本，不翻译链接地址
        elif t == 'link':
            if 'children' in node:
                translate_ast_nodes(node['children'])
            # 保留 node['link'] 不变
        # 图片节点，不翻译路径和标题，保持原样
        elif t == 'image':
            pass
        # 代码块不翻译
        elif t == 'code_block':
            pass
        # 内联代码不翻译
        elif t == 'codespan':
            pass
        # 表格的表头、表格内容都在 children 里递归翻译
        elif 'children' in node:
            translate_ast_nodes(node['children'])
    return ast_nodes

# 把 AST 渲染回 Markdown 文本，保证格式
def render_ast_to_markdown(ast_nodes):
    lines = []

    def render_node(node):
        t = node['type']
        if t == 'text':
            return node.get('text', '')
        elif t == 'paragraph':
            content = ''.join(render_node(c) for c in node.get('children', []))
            return content + '\n\n'
        elif t == 'heading':
            level = node.get('attrs', {}).get('level', 1)
            content = ''.join(render_node(c) for c in node.get('children', []))
            return f"{'#' * level} {content}\n\n"
        elif t == 'list':
            # 有序或无序
            ordered = node.get('attrs', {}).get('ordered', False)
            start = node.get('attrs', {}).get('start', 1)
            items = node.get('children', [])
            result = []
            for idx, item in enumerate(items):
                prefix = f"{start + idx}. " if ordered else "- "
                # 列表项通常是段落节点的children
                content = ''.join(render_node(c) for c in item.get('children', []))
                # 保持缩进
                result.append(prefix + content.replace('\n', '\n  '))
            return '\n'.join(result) + '\n\n'
        elif t == 'block_quote':
            content = ''.join(render_node(c) for c in node.get('children', []))
            # 每行加 >
            content_lines = content.strip().split('\n')
            quoted = '\n'.join('> ' + line for line in content_lines)
            return quoted + '\n\n'
        elif t == 'code_block':
            info = node.get('attrs', {}).get('info') or ''
            code = node.get('text', '')
            return f"```{info}\n{code}```\n\n"
        elif t == 'thematic_break':
            return '---\n\n'
        elif t == 'link':
            href = node.get('link', '')
            title = node.get('attrs', {}).get('title')
            content = ''.join(render_node(c) for c in node.get('children', []))
            title_part = f' "{title}"' if title else ''
            return f"[{content}]({href}{title_part})"
        elif t == 'image':
            src = node.get('link', '')
            title = node.get('attrs', {}).get('title')
            alt = ''.join(render_node(c) for c in node.get('children', []))
            title_part = f' "{title}"' if title else ''
            return f"![{alt}]({src}{title_part})"
        elif t == 'table':
            # 先渲染表头
            header = node.get('children', [])[0] if node.get('children') else None
            aligns = node.get('attrs', {}).get('align', [])
            body = node.get('children')[1:] if len(node.get('children', [])) > 1 else []

            def render_table_row(row):
                cells = row.get('children', [])
                cell_texts = [''.join(render_node(c) for c in cell.get('children', [])) for cell in cells]
                return '| ' + ' | '.join(cell_texts) + ' |'

            if not header:
                return ''

            header_line = render_table_row(header)
            # 根据对齐设置，构造分割行
            align_map = {
                'left': ':---',
                'center': ':---:',
                'right': '---:'
            }
            sep_cells = []
            for i in range(len(header.get('children', []))):
                align = aligns[i] if i < len(aligns) else None
                sep_cells.append(align_map.get(align, '---'))
            sep_line = '| ' + ' | '.join(sep_cells) + ' |'

            body_lines = [render_table_row(row) for row in body]

            return header_line + '\n' + sep_line + '\n' + '\n'.join(body_lines) + '\n\n'
        else:
            # 其它节点尝试递归子节点
            if 'children' in node:
                return ''.join(render_node(c) for c in node['children'])
            return ''

    for node in ast_nodes:
        lines.append(render_node(node))

    return ''.join(lines)

def process_file(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        markdown = mistune.create_markdown(renderer='ast')
        ast = markdown(content)

        # 翻译 AST 中的所有文本
        translate_ast_nodes(ast)

        # 渲染回 Markdown
        translated_content = render_ast_to_markdown(ast)

        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

        print(f"[✓] Translated {input_path} -> {output_path}", flush=True)
        return True
    except Exception as e:
        print(f"[X] Error processing {input_path}: {str(e)}", flush=True)
        import traceback
        traceback.print_exc()
        return False

def main():
    docs_dir = "./docs"
    translated_dir = "."

    if not os.path.exists(docs_dir):
        print(f"[!] Source directory not found: {docs_dir}", flush=True)
        sys.exit(1)

    if not check_api_ready(API_BASE_URL):
        sys.exit(1)

    file_tasks = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, docs_dir)
                output_path = os.path.join(translated_dir, rel_path)
                file_tasks.append((input_path, output_path))

    print(f"[*] Found {len(file_tasks)} files to translate", flush=True)

    success_count = 0
    failure_count = 0

    # 先处理小文件测试
    file_tasks.sort(key=lambda x: os.path.getsize(x[0]))

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(process_file, input_path, output_path): (input_path, output_path)
            for input_path, output_path in file_tasks
        }

        for future in concurrent.futures.as_completed(futures):
            input_path, output_path = futures[future]
            try:
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1
            except Exception as e:
                print(f"[X] Unexpected error with {input_path}: {str(e)}", flush=True)
                failure_count += 1

    print(f"\nTranslation summary: {success_count} succeeded, {failure_count} failed", flush=True)
    if failure_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
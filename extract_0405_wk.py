# -*- coding: utf-8 -*-
"""从 c92c6b7 提取 4.05 的悟空/八戒"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import subprocess, json, re

r = subprocess.run(['git', 'show', 'c92c6b7:news-data.js'], capture_output=True, cwd='.')
raw = r.stdout.decode('utf-8', errors='replace')

m = re.search(r'"2026-04-05":\s*\{', raw)
brace = raw.find('{', m.start())
depth = 0
end = brace
for i in range(brace, len(raw)):
    c = raw[i]
    if c == '{': depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break
block = raw[brace:end]

# 清理
clean = block.replace(''', '"').replace(''', '"')
clean = re.sub(r'//.*', '', clean)
clean = re.sub(r',(\s*[}\]])', r'\1', clean)

def is_valid(c):
    code = ord(c)
    if code < 0x80: return True
    if 0x4E00 <= code <= 0x9FFF: return True
    if 0x3000 <= code <= 0x303F: return True
    return c in ' \n\t{}[]:,"\'-_()）：【】《》'

safe = ''.join(c if is_valid(c) else ' ' for c in clean)
safe = re.sub(r'\s+', ' ', safe)

# 找问题区域
pos = 2602
with open('0405_context.txt', 'w', encoding='utf-8') as f:
    f.write(f'Around pos {pos}:\n')
    f.write(repr(safe[max(0,pos-100):pos+100]))
    f.write('\n\n')
    # 逐字符分析问题位置
    for i in range(max(0,pos-50), min(len(safe),pos+50)):
        c = safe[i]
        code = ord(c)
        f.write(f'{i}: {repr(c)} (U+{code:04X})\n')
print('Done')

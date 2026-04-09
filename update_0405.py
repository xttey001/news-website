# -*- coding: utf-8 -*-
"""更新 4.05 的悟空/八戒数据"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json, re

# 读取当前的 news-data.js
with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 读取 4.05 完整数据
with open('orig_20260405_full.json', 'r', encoding='utf-8') as f:
    wk_0405 = json.load(f)

print('4.05 wukong:', wk_0405.get('wukong_judgment', {}).get('market_sentiment', 'N/A'))
print('4.05 bajie:', list(wk_0405.get('bajie_conclusion', {}).keys()))

# 提取当前 news-data.js 中 4.05 的块
# 找到 4.05 开始
start_marker = '"2026-04-05":'
start_idx = raw.find(start_marker)
if start_idx == -1:
    print('4.05 not found!')
    exit(1)

# 找 { 开始
brace_start = raw.find('{', start_idx)
if brace_start == -1:
    print('No brace found!')
    exit(1)

# 平衡找 }
depth = 0
end_idx = brace_start
for i in range(brace_start, len(raw)):
    c = raw[i]
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            end_idx = i + 1
            break

# 构建新的 4.05 块
new_0405 = {
    'date': '2026-04-05',
    'market_tone': '清明假期A股休市，中东危机升级：伊朗拒绝特朗普48小时通牒，中国资产成全球避风港',
    **wk_0405,
    # 补充 s_level（从当前文件保留）
}
# 获取当前的 s_level
old_0405_start = raw.find(start_marker)
old_brace = raw.find('{', old_0405_start)
depth = 0
old_end = old_brace
for i in range(old_brace, len(raw)):
    c = raw[i]
    if c == '{': depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            old_end = i + 1
            break

# 尝试从旧块提取 s_level
old_block = raw[old_brace:old_end]
s_level_match = re.search(r'"s_level":\s*(\[.*?\])\s*,\s*"a_level"', old_block, re.DOTALL)
a_level_match = re.search(r'"a_level":\s*(\[.*?\])\s*,\s*"douyin"', old_block, re.DOTALL)
douyin_match = re.search(r'"douyin":\s*(\[.*?\])\s*\n\s*\}', old_block, re.DOTALL)

if s_level_match:
    new_0405['s_level'] = json.loads(s_level_match.group(1))
if a_level_match:
    new_0405['a_level'] = json.loads(a_level_match.group(1))
if douyin_match:
    new_0405['douyin'] = json.loads(douyin_match.group(1))

print(f's_level: {len(new_0405.get("s_level", []))} items')
print(f'a_level: {len(new_0405.get("a_level", []))} items')

# 序列化新块
new_0405_str = json.dumps(new_0405, ensure_ascii=False, indent=2)
# 缩进调整：增加8个空格
lines = new_0405_str.split('\n')
aligned_lines = []
for line in lines:
    aligned_lines.append('        ' + line)
new_0405_str = '\n'.join(aligned_lines)

# 替换旧块
new_raw = raw[:brace_start] + new_0405_str + raw[old_end:]

# 保存
with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(new_raw)

# 验证
import subprocess
r = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'\nJS语法: {"OK" if r.returncode == 0 else "ERROR"}')
print('更新完成!')

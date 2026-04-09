# -*- coding: utf-8 -*-
"""直接修复 4.05：注入悟空/八戒到已生成的 news-data.js"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json, re

# 读取悟空/八戒数据
with open('orig_20260405_full.json', 'r', encoding='utf-8') as f:
    wk_data = json.load(f)

print('wukong:', wk_data.get('wukong_judgment', {}).get('market_sentiment', 'N/A'))
print('bajie:', wk_data.get('bajie_conclusion', {}).get('optimal_action', 'N/A')[:30])

# 读取当前 news-data.js
with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 找 4.05 块的开始（JSON 对象开始）
# 策略：在 newsData = {...} 中找 "2026-04-05"
newsdata_start = content.find('const newsData = ')
newsdata_obj = content.find('{', newsdata_start)
newsdata_end = content.find('const availableDates', newsdata_start)

obj_content = content[newsdata_obj:newsdata_end]
print(f'newsData 对象: {len(obj_content)} chars')

# 找 4.05 块
date_marker = '"2026-04-05":'
date_pos = obj_content.find(date_marker)
if date_pos == -1:
    print('4.05 not found! Need to restore from scratch.')
    # 重新运行 restore_final.py
    import subprocess
    r = subprocess.run(['python', 'restore_final.py'], capture_output=True, text=True)
    print(r.stdout[-500:] if r.stdout else '')
    exit(0)

# 找到4.05块的开始 {
block_start_in_obj = date_pos + len(date_marker)
brace = obj_content.find('{', block_start_in_obj)
if brace == -1:
    print('No brace for 4.05!')
    exit(1)

# 平衡找结束 }
depth = 0
block_end = brace
for i in range(brace, len(obj_content)):
    c = obj_content[i]
    if c == '{': depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            block_end = i + 1
            break

# 构建新块
old_block = obj_content[brace:block_end]
print(f'旧块: {len(old_block)} chars')

# 获取 s_level, a_level, douyin（保留旧块内容）
def extract_field(block, field_name):
    """从块中提取字段"""
    marker = f'"{field_name}":'
    idx = block.find(marker)
    if idx == -1:
        return None
    # 找 [ 或 {
    bracket = block.find('[', idx)
    brace2 = block.find('{', idx)
    start = bracket if bracket != -1 and (brace2 == -1 or bracket < brace2) else brace2
    if start == -1:
        return None
    # 平衡找结束
    if block[start] == '[':
        depth = 0
        for i in range(start, len(block)):
            c = block[i]
            if c == '[': depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    return block[start:i+1]
    else:
        depth = 0
        for i in range(start, len(block)):
            c = block[i]
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return block[start:i+1]
    return None

s_level = extract_field(old_block, 's_level')
a_level = extract_field(old_block, 'a_level')
douyin = extract_field(old_block, 'douyin')
print(f's_level: {s_level[:50] if s_level else None}...')
print(f'a_level: {a_level[:50] if a_level else None}...')

# 构建新的 4.05 块
new_0405 = {
    'date': '2026-04-05',
    'market_tone': '清明假期A股休市，中东危机升级：伊朗拒绝特朗普48小时通牒，中国资产成全球避风港',
    'wukong_judgment': wk_data.get('wukong_judgment', {}),
    'bajie_conclusion': wk_data.get('bajie_conclusion', {}),
}

# 序列化（8空格缩进）
def serialize(val, indent=8):
    """序列化JSON值，8空格缩进"""
    s = json.dumps(val, ensure_ascii=False, indent=1)
    lines = s.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i == 0:
            result.append(' ' * indent + line)
        elif line.strip() in ('{', '}', '[', ']'):
            result.append(' ' * indent + line)
        else:
            result.append(' ' * (indent + 2) + line)
    return '\n'.join(result)

# 构建新块
new_block_lines = ['{']
new_block_lines.append(' ' * 8 + '"date": "2026-04-05",')
new_block_lines.append(' ' * 8 + '"market_tone": "清明假期A股休市，中东危机升级：伊朗拒绝特朗普48小时通牒，中国资产成全球避风港",')

# wukong_judgment
wk = wk_data.get('wukong_judgment', {})
wk_str = serialize(wk, indent=8)
wk_str = '\n'.join(' ' * 8 + line if i == 0 else (' ' * 8 + line) for i, line in enumerate(wk_str.split('\n')))
new_block_lines.append(' ' * 8 + '"wukong_judgment": ' + wk_str + ',')

# bajie_conclusion
bj = wk_data.get('bajie_conclusion', {})
bj_str = serialize(bj, indent=8)
new_block_lines.append(' ' * 8 + '"bajie_conclusion": ' + bj_str + ',')

# s_level, a_level, douyin
if s_level:
    new_block_lines.append(' ' * 8 + f'"s_level": {s_level},')
if a_level:
    new_block_lines.append(' ' * 8 + f'"a_level": {a_level},')
if douyin:
    new_block_lines.append(' ' * 8 + f'"douyin": {douyin}')

new_block_lines.append(' ' * 8 + '}')
new_block_str = '\n'.join(new_block_lines)

# 替换旧块
block_start_global = newsdata_obj + brace
block_end_global = newsdata_obj + block_end
new_content = content[:block_start_global] + new_block_str + content[block_end_global:]

# 保存
with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

# 验证
import subprocess
r = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'\nJS语法: {"OK" if r.returncode == 0 else "ERROR: " + str(r.stderr)[:100]}')

# 验证 4.05
if r.returncode == 0:
    r2 = subprocess.run(['node', '-e', '''
const fs = require('fs');
const content = fs.readFileSync('news-data.js', 'utf8');
const idx050 = content.indexOf('"2026-04-05":');
const idx060 = content.indexOf('"2026-04-06":');
const block = content.slice(idx050, idx060);
console.log('wukong:', block.includes('wukong_judgment'));
console.log('bajie:', block.includes('bajie_conclusion'));
'''], capture_output=True, text=True)
    print('验证:', r2.stdout.strip())
    print('完成!')

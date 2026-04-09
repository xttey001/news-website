# -*- coding: utf-8 -*-
"""注入4.05悟空/八戒到news-data.js"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json, re, subprocess

# 读取悟空/八戒
with open('orig_20260405_full.json', 'r', encoding='utf-8') as f:
    wk_data = json.load(f)

wk = wk_data.get('wukong_judgment', {})
bj = wk_data.get('bajie_conclusion', {})
print('悟空:', wk.get('market_sentiment', wk.get('emotion', 'N/A')))
print('八戒:', bj.get('optimal_action', bj.get('optimal_action', 'N/A'))[:30])

# 读取news-data.js（原始字节）
with open('news-data.js', 'rb') as f:
    raw = f.read()

# 尝试各种编码
for enc in ['utf-8', 'gbk', 'latin-1', 'cp936']:
    try:
        content = raw.decode(enc)
        print(f'Decoded: {enc}')
        break
    except:
        continue

# 提取JSON部分
m = re.search(rb'const newsData = (.+?);?const availableDates', raw, re.DOTALL)
if not m:
    print('Cannot find newsData!')
    exit(1)

json_bytes = m.group(1).strip().rstrip(b';')
json_str = json_bytes.decode('utf-8', errors='replace')

# 清理JS格式
json_str = re.sub(r'//.*', '', json_str)
json_str = json_str.replace("'", '"')
json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)

try:
    news_data = json.loads(json_str)
except:
    # 逐字符修复
    def is_valid(c):
        code = ord(c)
        if code < 0x80: return True
        if 0x4E00 <= code <= 0x9FFF: return True
        if 0x3000 <= code <= 0x303F: return True
        if 0xFF00 <= code <= 0xFFEF: return True
        return c in ' \n\t{}[]:,"\'-_()）：【】《》'
    safe = ''.join(c if is_valid(c) else ' ' for c in json_str)
    safe = re.sub(r'\s+', ' ', safe)
    try:
        news_data = json.loads(safe)
    except:
        print(f'JSON parse failed: {safe[5000:5200]}')
        exit(1)

print(f'Parsed: {len(news_data)} dates')

# 更新4.05
if '2026-04-05' in news_data:
    news_data['2026-04-05']['wukong_judgment'] = wk
    news_data['2026-04-05']['bajie_conclusion'] = bj
    print('Updated 2026-04-05 with wukong + bajie')
else:
    print('4.05 not found!')

# 生成新文件
sorted_dates = sorted(news_data.keys(), reverse=True)
output = 'const newsData = ' + json.dumps(news_data, ensure_ascii=False, indent=2) + ';\n\n'
output += 'const availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\n'
output += '''function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }'''

with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(output)

# 验证
r = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'JS语法: {"OK" if r.returncode == 0 else "ERROR: " + str(r.stderr)[:100]}')

# 打印4.05状态
d = news_data.get('2026-04-05', {})
print(f'\n2026-04-05: 悟空={bool(d.get("wukong_judgment"))} 八戒={bool(d.get("bajie_conclusion"))}')
print('完成!')

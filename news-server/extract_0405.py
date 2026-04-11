# -*- coding: utf-8 -*-
"""单独提取4.05的可用数据，写入文件"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import subprocess, re

r = subprocess.run(['git', 'show', '45e69d9:news-data.js'], capture_output=True)
raw = r.stdout.decode('utf-8', errors='replace')

# 找4.05块
idx = raw.find('2026-04-05')
next_idx = raw.find('2026-04-04', idx+10)
block = raw[idx:next_idx]

# 提取所有title
titles = re.findall(r'"title":\s*"([^"]+)"', block)
market_tone = re.search(r'market_tone[\":\s]+([^\n]+)', block)

output = []
output.append('market_tone: ' + (market_tone.group(1)[:100] if market_tone else 'N/A'))
output.append('titles:')
for t in titles:
    output.append('  ' + t[:80])

# 写文件
with open('0405_data.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('OK')

# -*- coding: utf-8 -*-
"""Debug actual data issue"""
import sys, io, os, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.chdir('C:\\Users\\asus\\.qclaw\\workspace\\news-server')

# Load 2026-04-10 data
with open('news_data/news_2026-04-10.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add sangsha_module
data['sangsha_module'] = {'test': 'sangsha_0410'}

# Serialize just this one date
json_str = json.dumps({"2026-04-10": data}, ensure_ascii=False, indent=2)

# Check
idx_0410 = json_str.find('"2026-04-10"')
idx_sg = json_str.find('"sangsha_module"')

print(f'2026-04-10 at: {idx_0410}')
print(f'sangsha_module at: {idx_sg}')
print(f'Order correct: {idx_sg > idx_0410}')

# Now check if there's a nested "2026-04-10" in the data
print(f'\nNumber of "2026-04-10" in JSON: {json_str.count("2026-04-10")}')

# Check all_news items
for i, news in enumerate(data.get('all_news', [])):
    if news.get('date') == '2026-04-10':
        print(f'News item {i} has date 2026-04-10')
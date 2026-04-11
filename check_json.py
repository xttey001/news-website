# -*- coding: utf-8 -*-
"""Check JSON structure"""
import sys, io, os, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.chdir('C:\\Users\\asus\\.qclaw\\workspace\\news-server')

# Load all data
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

# Add dummy sangsha/white_dragon for testing
for date in all_news:
    all_news[date]['sangsha_module'] = {'test': f'sangsha_{date}'}
    all_news[date]['white_dragon'] = {'test': f'white_{date}'}

# Check the dict
print('2026-04-10 keys:', list(all_news['2026-04-10'].keys()))
print('sangsha_module:', all_news['2026-04-10']['sangsha_module'])

# Generate JSON
json_str = json.dumps(all_news, ensure_ascii=False, indent=2)

# Find the 2026-04-10 section
start = json_str.find('"2026-04-10"')
end = json_str.find('"2026-04-09"')
section = json_str[start:end]

print('\n2026-04-10 section (truncated):')
print(section[:500])
print('...')
print(section[-200:])

print(f'\nContains sangsha_module: {"sangsha_module" in section}')
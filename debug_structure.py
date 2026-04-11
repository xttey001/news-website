# -*- coding: utf-8 -*-
"""Debug data structure issue"""
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

print('Dates loaded:')
for d in sorted(all_news.keys(), reverse=True):
    print(f'  {d}')

# Add sangsha and white_dragon
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
except:
    market_data = {}

for date in sorted(all_news.keys(), reverse=True):
    try:
        sg_result = run_sangsha({date: all_news[date]}, date, market_data)
        sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except:
        sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0,
              'avg_panic_prob': 0, 'analysis_results': []}
    
    try:
        wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
        wd = wd_result.get('白龙马决策', {})
    except:
        wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '',
              '是否利用散户': False, '综合建议': '暂无数据'}
    
    all_news[date]['sangsha_module'] = sg
    all_news[date]['white_dragon'] = wd

# Check the order in the dict
print('\nDict order after adding sangsha/white_dragon:')
for d in all_news.keys():
    has_sg = 'sangsha_module' in all_news[d]
    has_wd = 'white_dragon' in all_news[d]
    print(f'  {d}: sangsha={has_sg}, white_dragon={has_wd}')

# Generate JSON and check
sorted_dates = sorted(all_news.keys(), reverse=True)
json_str = json.dumps(all_news, ensure_ascii=False, indent=2)

# Find positions
idx_0410 = json_str.find('"2026-04-10"')
idx_0409 = json_str.find('"2026-04-09"')
idx_sg = json_str.find('"sangsha_module"', idx_0410)

print(f'\nJSON string positions:')
print(f'  2026-04-10 at: {idx_0410}')
print(f'  2026-04-09 at: {idx_0409}')
print(f'  sangsha_module after 0410 at: {idx_sg}')

if idx_sg > idx_0409:
    print('  ERROR: sangsha_module is after 2026-04-09!')
else:
    print('  OK: sangsha_module is before 2026-04-09')
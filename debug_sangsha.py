# -*- coding: utf-8 -*-
"""Debug script to check what's happening with sangsha_module"""
import sys, io, os, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.chdir('C:\\Users\\asus\\.qclaw\\workspace\\news-server')

# Load the news data
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

print(f'Loaded {len(all_news)} dates')

# Check 2026-04-10 before processing
date = '2026-04-10'
if date in all_news:
    print(f'\nBefore processing:')
    print(f'  Keys: {list(all_news[date].keys())}')
    print(f'  Has sangsha_module: {"sangsha_module" in all_news[date]}')
    print(f'  Has white_dragon: {"white_dragon" in all_news[date]}')

# Simulate what generate_full_newsdata.py does
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
    print(f'\nMarket data: {len(market_data)} items')
except Exception as e:
    print(f'Market data error: {e}')
    market_data = {}

# Run for 2026-04-10
try:
    sg_result = run_sangsha({date: all_news[date]}, date, market_data)
    sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    print(f'\nSangsha result keys: {list(sg.keys()) if sg else "None"}')
except Exception as e:
    print(f'Sangsha error: {e}')
    sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0,
          'avg_panic_prob': 0, 'analysis_results': []}

try:
    wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
    wd = wd_result.get('白龙马决策', {})
    print(f'White dragon result keys: {list(wd.keys()) if wd else "None"}')
except Exception as e:
    print(f'White dragon error: {e}')
    wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '',
          '是否利用散户': False, '综合建议': '📊 暂无数据'}

all_news[date]['sangsha_module'] = sg
all_news[date]['white_dragon'] = wd

print(f'\nAfter processing:')
print(f'  Keys: {list(all_news[date].keys())}')
print(f'  Has sangsha_module: {"sangsha_module" in all_news[date]}')
print(f'  Has white_dragon: {"white_dragon" in all_news[date]}')
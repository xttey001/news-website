# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159871', '159542']
market_data = get_market_data(codes, 7)

# 模拟悟空+原始八戒
wukong = {'market_sentiment': '谨慎偏多', 'operations': [{'type': '可做', 'content': 'AI算力ETF'}]}
orig_bajie = {'win_rate': '~62%', 'optimal_action': '轻仓观望'}
sangsha = {'analysis_results': [{'买入概率': 55}, {'买入概率': 40}, {'买入概率': 30}]}

result = run_white_dragon(market_data, sangsha, wukong, orig_bajie)
wd = result.get('白龙马决策', {})

print(f"总体状态: {wd.get('主力状态')} | 阶段: {wd.get('阶段')}")
print(f"可信度: {wd.get('可信度')}")
print(f"矛盾ETF数: {wd.get('矛盾ETF数', 0)}")
print()

# 单个ETF详情
etfs = result.get('ETF分析', [])
for e in etfs:
    vol_r = e.get('单日量比', '?')
    state = e.get('主力状态', '?')
    price_chg = e.get('price_trend', {}).get('change_pct', '?')
    print(f"  {e.get('code')} | 涨跌={price_chg}% | 单日量比={vol_r} | 状态={state} | {e.get('行为解释', '')[:30]}")

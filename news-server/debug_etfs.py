# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.white_dragon_model import WhiteDragonModel

codes = ['512760', '512930', '518880', '588890', '159871', '159542']
market_data = get_market_data(codes, 7)

wukong = {'market_sentiment': '谨慎偏多'}
orig_bajie = {'win_rate': '~62%', 'optimal_action': '轻仓观望'}
sangsha_results = [{'买入概率': 55}, {'买入概率': 40}, {'买入概率': 30}]

model = WhiteDragonModel()
result = model.analyze_multi_etfs(market_data, sangsha_results, wukong, orig_bajie)

etfs = result.get('白龙马决策', {}).get('各ETF分析', [])
print('=== 单ETF判断 ===')
for e in etfs:
    print(f"  {e.get('code')} | 状态={e.get('主力状态')} | 可信度={e.get('可信度')} | 量比={e.get('单日量比')} | {e.get('行为解释', '')[:40]}")

print()
wd = result.get('白龙马决策', {})
print(f'=== 汇总判断 ===')
print(f"  总体状态: {wd.get('主力状态')} | 阶段: {wd.get('阶段')}")
print(f"  可信度: {wd.get('可信度')}")
print(f"  矛盾ETF数: {wd.get('矛盾ETF数', 0)}")
print(f"  建议: {wd.get('综合建议', '')[:60]}")

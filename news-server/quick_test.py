# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import sys
sys.path.insert(0, '.')
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon
from market_agents.data_fetcher import get_market_data

# 测试数据
test_news = {
    '2026-04-08': {
        'date': '2026-04-08',
        'market_tone': 'Test',
        's_level': [
            {'title': 'AI芯片暴涨，创业板AI ETF涨超7%', 'summary': '科创芯片ETF涨停，中际旭创涨停', 'emoji': '🔴', 'etfs': [{'name': '512760', 'sentiment': '利好'}], 'stocks': ['中际旭创']}
        ],
        'a_level': [],
        'douyin': []
    },
    '2026-04-07': {
        'date': '2026-04-07',
        'market_tone': 'Test2',
        's_level': [
            {'title': 'COMEX黄金突破70000美元创历史新高', 'summary': '黄金创历史新高', 'emoji': '🔴', 'etfs': [{'name': '518880', 'sentiment': '利好'}], 'stocks': ['黄金股']}
        ],
        'a_level': [],
        'douyin': []
    }
}

# 获取市场数据
codes = ['512760', '512930', '518880']
market_data = get_market_data(codes, 7)

# 沙僧
sg = run_sangsha(test_news, '2026-04-09', market_data)
sg_module = sg.get('沙僧模块', sg.get('sengseng', {}))

# 白龙马
wd = run_white_dragon(market_data, sg_module.get('analysis_results', []))
wd_decision = wd.get('白龙马决策', {})

# 输出
output = {
    'sangsha_module': sg_module,
    'white_dragon': wd_decision
}

print('=== Test Output ===')
print('Sangsha sentiment:', sg_module.get('overall_sentiment'))
print('Sangsha advice:', sg_module.get('advice'))
print('Sangsha top news:')
for r in sg_module.get('analysis_results', [])[:2]:
    print('  -', r.get('title', '')[:25], 'buy_prob=', r.get('买入概率'), '%')
print('WhiteDragon state:', wd_decision.get('主力状态'))
print('WhiteDragon stage:', wd_decision.get('阶段'))
print('WhiteDragon using_retail:', wd_decision.get('是否利用散户'))
print('WhiteDragon advice:', wd_decision.get('综合建议'))

# 保存
with open('github-pages-deploy/test_market_agents.js', 'w', encoding='utf-8') as f:
    f.write('const marketAgentsOutput = ' + json.dumps(output, ensure_ascii=False, indent=2) + ';\n')
print('Saved!')
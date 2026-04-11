# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data

# 只取512930的K线数据
codes = ['512930']
data = get_market_data(codes, 7)
klines = data.get('512930', {}).get('klines', [])
print(f'K线条数: {len(klines)}')
for k in klines:
    print(f"  date={k.get('date','?')} close={k.get('close','?')} vol={k.get('volume','?')} vol_ratio={k.get('volume_ratio','?')}")

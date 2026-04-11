# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data

# Check what fields are in klines
codes = ['512930']
data = get_market_data(codes, 7)
klines = data.get('512930', {}).get('klines', [])
print('=== 512930 K线数据 ===')
for k in klines:
    print(dict(k))

# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data

codes = ['512760', '512930', '518880', '588890', '159871', '159542']
raw = get_market_data(codes, 5)
for code, info in raw.items():
    klines = info.get('klines', [])
    if len(klines) >= 2:
        today = klines[-1]
        yest = klines[-2]
        chg = 'N/A'
        vol_r = 'N/A'
        if today.get('close') and yest.get('close') and yest['close'] > 0:
            chg = f"{((today['close']-yest['close'])/yest['close']*100):.2f}%"
        if today.get('volume') and yest.get('volume') and yest['volume'] > 0:
            vol_r = f"{today['volume']/yest['volume']:.2f}"
        label = {'512760':'芯片','512930':'AI算力','518880':'黄金','588890':'科创芯片','159871':'电池','159542':'电网'}
        print((label.get(code,code)) + ' (' + code + '): 收盘=' + str(today.get('close','?')) + ' 涨跌=' + chg + ' 量比=' + vol_r)
    elif len(klines) == 1:
        print(code + ': 今日仅1条数据，收盘=' + str(klines[0].get('close','?')))
    else:
        print(code + ': 无K线数据')

# -*- coding: utf-8 -*-
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['news_data/news_2026-04-09.json', 'news_data/news_2026-04-10.json']:
    try:
        with open(fname, encoding='utf-8') as f:
            d = json.load(f)
        print('\n=== ' + fname + ' ===')
        print('has wukong: ' + str('wukong_judgment' in d))
        print('has bajie: ' + str('bajie_conclusion' in d))
        print('s_level count: ' + str(len(d.get('s_level',[]))))
        print('a_level count: ' + str(len(d.get('a_level',[]))))
        print('all_news count: ' + str(len(d.get('all_news',[]))))
        wk = d.get('wukong_judgment',{})
        sentiment = wk.get('market_sentiment', wk.get('emotion',''))
        print('悟空情绪: ' + sentiment)
        ops = wk.get('operations', wk.get('strategy',[]))
        for o in ops[:3]:
            print('  操作: ' + str(o))
        bj = d.get('bajie_conclusion',{})
        print('八戒行动: ' + bj.get('optimal_action',''))
        print('八戒胜率: ' + bj.get('win_rate',''))
    except FileNotFoundError:
        print(fname + ' not found')

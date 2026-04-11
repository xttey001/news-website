# -*- coding: utf-8 -*-
import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

def search_news(keyword):
    url = 'http://localhost:19000/proxy/prosearch/search'
    payload = {'keyword': keyword, 'industry': 'news'}
    try:
        r = requests.post(url, json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {'success': False, 'error': str(e)}

keywords = [
    'A股 收盘 涨跌 2026年4月8日 今天',
    '美股 纳指 道指 最新行情',
    '黄金 金价 现货黄金 2026年4月',
    '原油 布油 WTI 最新',
    '半导体 芯片 存储器 涨价',
    'AI 人工智能 大模型 最新',
    '特朗普 对等关税 中国 反制',
    '降息 美联储 利率 最新'
]

all_results = []
for kw in keywords:
    result = search_news(kw)
    if result.get('success'):
        docs = result.get('data', {}).get('docs', [])
        for doc in docs[:6]:
            all_results.append({
                'title': doc.get('title', ''),
                'passage': doc.get('passage', ''),
                'date': doc.get('date', ''),
                'site': doc.get('site', '')
            })

print(json.dumps(all_results, ensure_ascii=False, indent=2))

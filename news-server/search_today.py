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
    'A股行情 上证指数 创业板 2026年4月',
    '黄金 原油 美股 最新行情',
    '芯片 半导体 AI人工智能 最新消息',
    '新能源 锂电池 光伏 储能',
    '医药 创新药 生物医药',
    '央行 利率 货币政策 最新',
    '特朗普 关税 贸易政策'
]

all_results = []
for kw in keywords:
    result = search_news(kw)
    if result.get('success'):
        docs = result.get('data', {}).get('docs', [])
        for doc in docs[:8]:
            all_results.append({
                'title': doc.get('title', ''),
                'passage': doc.get('passage', ''),
                'date': doc.get('date', ''),
                'site': doc.get('site', '')
            })

print(json.dumps(all_results, ensure_ascii=False, indent=2))

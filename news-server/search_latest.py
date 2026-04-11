# -*- coding: utf-8 -*-
import requests
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = '19000'
FROM_TIME = int(time.time() - 86400)  # 最近24小时

keywords = [
    'A股 财经新闻 2026年4月2日',
    '美股 纳斯达克 道琼斯 4月2日',
    '芯片 人工智能 机器人 科技股 4月2日',
    '医药板块 白酒 消费 4月2日',
    '黄金 原油 大宗商品 4月2日'
]

all_results = []

for kw in keywords:
    try:
        r = requests.post(f'http://localhost:{PORT}/proxy/prosearch/search',
                         json={'keyword': kw, 'from_time': FROM_TIME}, timeout=20)
        data = r.json()
        if data.get('success'):
            print(f'\n=== {kw} ===')
            docs = data.get('data', {}).get('docs', [])
            for doc in docs[:5]:
                title = doc.get('title', '')
                site = doc.get('site', '')
                date = doc.get('date', '')
                url = doc.get('url', '')
                passage = doc.get('passage', '')[:200]
                print(f'{title} | {site} | {date}')
                print(f'  {passage}')
                all_results.append({
                    'keyword': kw,
                    'title': title,
                    'site': site,
                    'date': date,
                    'url': url,
                    'passage': passage
                })
        else:
            print(f'\n=== {kw} === failed')
    except Exception as e:
        print(f'Error: {e}')

# Save results
with open('latest_news_042.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'\nSaved {len(all_results)} results')

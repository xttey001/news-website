# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

# Set UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

PORT = 19000
FROM_TIME = int(1774232589)

keywords = [
    "A股 股市 最新行情 2026",
    "新能源 电动车 储能 最新动态",
    "金融 科技 AI 人工智能 最新资讯"
]

for kw in keywords:
    try:
        data = json.dumps({'keyword': kw, 'from_time': FROM_TIME}).encode('utf-8')
        req = urllib.request.Request(
            f'http://localhost:{PORT}/proxy/prosearch/search',
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        r = urllib.request.urlopen(req, timeout=15)
        result = r.read().decode('utf-8')
        print(f"\n{'='*60}\nSEARCH: {kw}\n{'='*60}")
        print(result)
    except Exception as e:
        print(f"Error searching '{kw}': {e}")

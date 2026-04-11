# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

PORT = 19000
FROM_TIME = 1774232589

data = json.dumps({'keyword': '抖音热点 爆款视频 热搜 2026', 'from_time': FROM_TIME}).encode('utf-8')
req = urllib.request.Request(
    'http://localhost:{}/proxy/prosearch/search'.format(PORT),
    data=data,
    headers={'Content-Type': 'application/json'}
)
r = urllib.request.urlopen(req, timeout=15)
result = r.read().decode('utf-8')
print(result)

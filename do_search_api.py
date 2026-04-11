# -*- coding: utf-8 -*-
import sys, json, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

# Get port from environment
port = os.environ.get('AUTH_GATEWAY_PORT', '19000')
print(f"Port: {port}")

import requests

url = f"http://127.0.0.1:{port}/proxy/prosearch/search"

# Today's news - last 24 hours
params = {
    "keyword": "财经新闻 2026年4月10日",
    "from_time": 1775704003,
    "to_time": 1775790403
}

try:
    r = requests.post(url, json=params, timeout=15)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
# -*- coding: utf-8 -*-
import sys, json, os, requests
sys.stdout.reconfigure(encoding='utf-8')

port = os.environ.get('AUTH_GATEWAY_PORT', '19000')
url = f"http://127.0.0.1:{port}/proxy/prosearch/search"

# Multiple search queries for comprehensive coverage
queries = [
    # Today's financial news
    {"keyword": "财经新闻 2026年4月10日", "from_time": 1775704003, "to_time": 1775790403},
    {"keyword": "A股 股市 今日要闻", "from_time": 1775704003, "to_time": 1775790403},
    {"keyword": "中国股市 收盘 2026年4月", "from_time": 1775617603, "to_time": 1775790403},
    {"keyword": "基金 理财 今日", "from_time": 1775704003, "to_time": 1775790403},
    {"keyword": "黄金 原油 大宗商品 2026年4月", "from_time": 1775617603, "to_time": 1775790403},
]

all_results = []

for q in queries:
    try:
        r = requests.post(url, json=q, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data.get('success'):
                all_results.append(data)
                print(f"✓ {q['keyword']}: {data.get('totalResults', 'N/A')}")
            else:
                print(f"✗ {q['keyword']}: {data.get('message')}")
        else:
            print(f"✗ {q['keyword']}: HTTP {r.status_code}")
    except Exception as e:
        print(f"✗ {q['keyword']}: {e}")

print(f"\n=== Total queries: {len(all_results)} ===")

# Save raw results
with open('news_data/today_search_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print("Saved to news_data/today_search_results.json")
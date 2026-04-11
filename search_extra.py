# -*- coding: utf-8 -*-
import sys, json, os, requests
sys.stdout.reconfigure(encoding='utf-8')

port = os.environ.get('AUTH_GATEWAY_PORT', '19000')
url = f"http://127.0.0.1:{port}/proxy/prosearch/search"

queries = [
    {"keyword": "美伊谈判 停火 霍尔木兹 2026年4月", "from_time": 1775617603, "to_time": 1775790403},
    {"keyword": "A股 半导体 AI 芯片 科技 2026年4月10日", "from_time": 1775704003, "to_time": 1775790403},
    {"keyword": "人民币汇率 美联储 美元 2026年4月", "from_time": 1775704003, "to_time": 1775790403},
]

for q in queries:
    try:
        r = requests.post(url, json=q, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data.get('success'):
                # Save each result
                fname = q['keyword'][:20].replace(' ', '_') + '.json'
                fname = 'news_data/extra_' + fname + '.json'
                with open(fname, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"✓ {q['keyword'][:30]}: saved to {fname}")
            else:
                print(f"✗ {q['keyword']}: {data.get('message')}")
        else:
            print(f"✗ {q['keyword']}: HTTP {r.status_code}")
    except Exception as e:
        print(f"✗ {q['keyword']}: {e}")
import urllib.request, json, time, os
from datetime import datetime, timedelta

port = os.environ.get('AUTH_GATEWAY_PORT', '19000')
ppid = os.getppid()
print(f"[QClaw] AUTH_GATEWAY_PORT: {port}")
print(f"[QClaw] Parent PID: {ppid}")

# 计算最近24小时时间戳
from_time = int((datetime.now() - timedelta(days=1)).timestamp())
print(f"[QClaw] from_time: {from_time}")

queries = [
    "A股 今日股市 财经新闻 2026年3月30日",
    "新能源 股票 热点 2026年3月",
    "金融 科技 财经要闻 2026年3月30日"
]

results = {}
for q in queries:
    try:
        payload = json.dumps({"keyword": q, "from_time": from_time}).encode('utf-8')
        req = urllib.request.Request(
            f"http://localhost:{port}/proxy/prosearch/search",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results[q] = data
            print(f"\n=== 搜索: {q} ===")
            if data.get('success'):
                print(data.get('message', ''))
            else:
                print(f"失败: {data.get('message', 'unknown error')}")
    except Exception as e:
        print(f"错误: {e}")
        results[q] = None

# 保存结果
with open('C:/Users/asus/.qclaw/workspace/search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("\n搜索结果已保存到 search_results.json")

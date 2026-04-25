# -*- coding: utf-8 -*-
import subprocess, json

script = r"D:\QCLaw\resources\openclaw\config\skills\online-search\scripts\prosearch.cjs"
from_t = 1776179776
to_t = 1776266176

kws = [
    "美伊谈判第二轮 2026年4月",
    "亚马逊收购Globalstar 2026年4月",
    "科创板芯片半导体 2026年4月15日",
    "医药板块逆势走强 2026年4月15日",
    "上证指数4000点 2026年4月15日",
]

for kw in kws:
    params = {"keyword": kw, "from_time": from_t, "to_time": to_t}
    r = subprocess.run(["node", script, json.dumps(params, ensure_ascii=False)], capture_output=True)
    try:
        data = json.loads(r.stdout.decode("utf-8", errors="replace"))
        with open(r"C:\Users\asus\.qclaw\workspace\news_today.txt", "a", encoding="utf-8") as f:
            f.write("=== " + kw + " ===\n")
            f.write(data.get("message", "") + "\n\n")
    except Exception as e:
        with open(r"C:\Users\asus\.qclaw\workspace\news_today.txt", "a", encoding="utf-8") as f:
            f.write("=== " + kw + " ===\nERROR: " + str(e) + "\n\n")
print("done")

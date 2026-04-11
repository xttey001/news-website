# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    data = json.load(f)

sl = data.get('s_level', [])
al = data.get('a_level', [])
dy = data.get('douyin', [])

print("=== S级 (%d条) ===" % len(sl))
if sl:
    print("字段:", list(sl[0].keys()))
    print("bayes_analysis:", "有" if 'bayes_analysis' in sl[0] else "无")
    for i, item in enumerate(sl):
        print("S[%d] title: %s" % (i, item.get('title', '')[:50]))
        print("S[%d] key_point: %s" % (i, item.get('key_point', '')[:50]))
        print("S[%d] signal: %s" % (i, item.get('signal', '')[:50]))
        print("S[%d] bayes: %s" % (i, item.get('bayes_analysis', '无')))

print()
print("=== A级 (%d条) ===" % len(al))
if al:
    print("字段:", list(al[0].keys()))
    for i, item in enumerate(al[:2]):
        print("A[%d] title: %s" % (i, item.get('title', '')[:50]))
        print("A[%d] key_point: %s" % (i, item.get('key_point', '')[:50]))

print()
print("=== 抖音 (%d条) ===" % len(dy))
print("douyin 字段:", list(dy[0].keys()) if dy else "空")

# 检查 index.html 里渲染 S/A 用的字段名
print()
print("=== index.html 渲染字段检查 ===")
with open('github-pages-deploy/index.html', encoding='utf-8') as f:
    html = f.read()
# 找 s_level 渲染部分
idx = html.find('s_level.forEach')
if idx > 0:
    chunk = html[idx:idx+2000]
    # 找所有 ${xxx} 变量引用
    import re
    vars_used = re.findall(r'\$\{([^}]+)\}', chunk)
    print("S级渲染用的字段:", vars_used[:20])

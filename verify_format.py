# -*- coding: utf-8 -*-
import json

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JSON
json_str = content.replace('const newsData = ', '').split(';\n\nconst availableDates')[0]
data = json.loads(json_str)

# Check 2026-04-10 format
d = data['2026-04-10']

print('=== 2026-04-10 格式验证 ===')
print(f"\n1. wukong_judgment 格式:")
print(f"   类型: {type(d['wukong_judgment']).__name__}")
if isinstance(d['wukong_judgment'], dict):
    print(f"   字段: {list(d['wukong_judgment'].keys())}")
    print(f"   market_sentiment: {d['wukong_judgment'].get('market_sentiment', 'MISSING')}")

print(f"\n2. bajie_conclusion 格式:")
print(f"   类型: {type(d['bajie_conclusion']).__name__}")
if isinstance(d['bajie_conclusion'], dict):
    print(f"   字段: {list(d['bajie_conclusion'].keys())}")
    print(f"   optimal_action: {d['bajie_conclusion'].get('optimal_action', 'MISSING')[:50]}...")

print(f"\n3. S级新闻 bayes_analysis:")
for i, item in enumerate(d['s_level']):
    has_bayes = 'bayes_analysis' in item
    print(f"   S-{i+1}: {item['title'][:40]}... | bayes: {has_bayes}")

print(f"\n4. A级新闻 bayes_analysis:")
for i, item in enumerate(d['a_level']):
    has_bayes = 'bayes_analysis' in item
    print(f"   A-{i+1}: {item['title'][:40]}... | bayes: {has_bayes}")

print(f"\n5. 沙僧模块:")
print(f"   类型: {type(d.get('sangsha_module')).__name__}")
if isinstance(d.get('sangsha_module'), dict):
    sg = d['sangsha_module']
    print(f"   overall_sentiment: {sg.get('overall_sentiment')}")
    print(f"   avg_buy_prob: {sg.get('avg_buy_prob')}")

print(f"\n6. 白龙马模块:")
print(f"   类型: {type(d.get('white_dragon')).__name__}")
if isinstance(d.get('white_dragon'), dict):
    wd = d['white_dragon']
    print(f"   主力状态: {wd.get('主力状态')}")
    print(f"   综合建议: {wd.get('综合建议')}")
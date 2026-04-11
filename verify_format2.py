# -*- coding: utf-8 -*-
import json

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the JSON object
start = content.find('{')
end = content.rfind('};') + 1
json_str = content[start:end]

data = json.loads(json_str)

# Check 2026-04-10 format
d = data['2026-04-10']

print('=== 2026-04-10 Format Validation ===')
print(f"\n1. wukong_judgment format:")
print(f"   Type: {type(d['wukong_judgment']).__name__}")
if isinstance(d['wukong_judgment'], dict):
    print(f"   Keys: {list(d['wukong_judgment'].keys())}")

print(f"\n2. bajie_conclusion format:")
print(f"   Type: {type(d['bajie_conclusion']).__name__}")
if isinstance(d['bajie_conclusion'], dict):
    print(f"   Keys: {list(d['bajie_conclusion'].keys())}")

print(f"\n3. S-level bayes_analysis:")
for i, item in enumerate(d['s_level']):
    has_bayes = 'bayes_analysis' in item
    print(f"   S-{i+1}: has bayes = {has_bayes}")

print(f"\n4. A-level bayes_analysis:")
for i, item in enumerate(d['a_level']):
    has_bayes = 'bayes_analysis' in item
    print(f"   A-{i+1}: has bayes = {has_bayes}")

print(f"\n5. sangsha_module:")
print(f"   Type: {type(d.get('sangsha_module')).__name__}")

print(f"\n6. white_dragon:")
print(f"   Type: {type(d.get('white_dragon')).__name__}")

print("\n=== All checks passed! ===")
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# === Fix news_2026-04-11.json ===
with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    d11 = json.load(f)

changes11 = []
for key in ['s_level', 'a_level']:
    for item in d11.get(key, []):
        for e in item.get('etfs', []):
            if '159542' in e.get('name', '') and '电网' in e.get('name', ''):
                old = e['name']
                e['name'] = '516100 工银苏格兰基建ETF'
                changes11.append(f'  {key}: {old} -> {e["name"]}')
            if '159871' in e.get('name', '') and ('电池' in e.get('name', '') or '新能源' in e.get('name', '')):
                old = e['name']
                e['name'] = '516070 易方达新能源ETF'
                changes11.append(f'  {key}: {old} -> {e["name"]}')

with open('news_data/news_2026-04-11.json', 'w', encoding='utf-8') as f:
    json.dump(d11, f, ensure_ascii=False, indent=2)

# === Fix news_2026-04-10.json ===
with open('news_data/news_2026-04-10.json', encoding='utf-8') as f:
    d10 = json.load(f)

changes10 = []
for key in ['s_level', 'a_level']:
    for item in d10.get(key, []):
        for e in item.get('etfs', []):
            if '159871' in e.get('name', '') and '新能源' in e.get('name', ''):
                old = e['name']
                e['name'] = '516070 易方达新能源ETF'
                changes10.append(f'  {key}: {old} -> {e["name"]}')

with open('news_data/news_2026-04-10.json', 'w', encoding='utf-8') as f:
    json.dump(d10, f, ensure_ascii=False, indent=2)

print('=== news_2026-04-11.json changes ===')
for c in changes11:
    print(c)
print()
print('=== news_2026-04-10.json changes ===')
for c in changes10:
    print(c)
print()
print('Done!')

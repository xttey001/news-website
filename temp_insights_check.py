import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights.json', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total patterns: {len(data)}')
print()

# Check ETF-related patterns
for item in data:
    name = item.get('name', '')
    item_str = str(item)
    if 'ETF' in name or any(x in item_str for x in ['159542', '159871']):
        print(f'Name: {name}')
        print(f'  Status: {item.get("status")}')
        print(f'  Confidence: {item.get("confidence")}')
        print()

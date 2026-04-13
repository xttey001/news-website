import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('insights.json', encoding='utf-8') as f:
    d = json.load(f)

for p in d['patterns']:
    pid = p.get('id','')
    if 'ETF' in pid:
        print(f'Pattern: {pid}')
        for r in p.get('trading_rules', []):
            print(f'  RULE: {r}')
        print()

print('=== etf_knowledge ===')
for ek in d.get('etf_knowledge', []):
    print(f'{ek["id"]}: wrong={ek["wrong_code"]}/{ek["wrong_name"]} -> correct={ek["correct_code"]}/{ek["correct_name"]}')

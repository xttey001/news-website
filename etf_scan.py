import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'
all_etf_refs = {}  # code -> list of (date, news_title, claimed_name, sentiment)
all_stock_refs = {}  # code -> list of (date, news_title, claimed_name)

files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and f >= 'news_2026-03-25.json' and f <= 'news_2026-04-11.json'])

print(f'Files to scan: {len(files)}')
print()

for fname in files:
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    date = d.get('date', fname)
    
    # Check all relevant fields
    for key in ['all_news', 's_level', 'a_level', 'market_tone']:
        items = d.get(key, [])
        if isinstance(items, str):
            items = [{'title': date, 'content': items}]
        elif not isinstance(items, list):
            items = [items] if items else []
        
        for item in items:
            if not isinstance(item, dict):
                continue
            
            # Extract ETFs
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                sentiment = e.get('sentiment', '')
                title = item.get('title', '')
                
                # Extract code (6-digit number)
                import re
                codes = re.findall(r'\b(\d{6})\b', name)
                for code in codes:
                    if code not in all_etf_refs:
                        all_etf_refs[code] = []
                    all_etf_refs[code].append({
                        'date': date,
                        'title': title[:60],
                        'claimed_name': name,
                        'sentiment': sentiment,
                        'source': key
                    })
            
            # Extract stocks
            for s in item.get('stocks', []):
                if not isinstance(s, str):
                    continue
                import re
                codes = re.findall(r'\((\d{6})\)', s)
                for code in codes:
                    title = item.get('title', '')
                    if code not in all_stock_refs:
                        all_stock_refs[code] = []
                    all_stock_refs[code].append({
                        'date': date,
                        'title': title[:60],
                        'claimed_name': s
                    })

# Print ETF report
print('=' * 80)
print('ETF REFERENCES FOUND:')
print('=' * 80)
for code in sorted(all_etf_refs.keys()):
    refs = all_etf_refs[code]
    print(f'\n[Code: {code}]')
    for r in refs:
        print(f'  {r["date"]} | {r["source"]} | {r["claimed_name"]} ({r["sentiment"]})')
        print(f'    -> {r["title"]}')

print()
print('=' * 80)
print('STOCK REFERENCES FOUND:')
print('=' * 80)
for code in sorted(all_stock_refs.keys()):
    refs = all_stock_refs[code]
    print(f'\n[Code: {code}]')
    for r in refs:
        print(f'  {r["date"]} | {r["claimed_name"]}')
        print(f'    -> {r["title"]}')

print()
print(f'Total ETF codes: {len(all_etf_refs)}')
print(f'Total stock codes: {len(all_stock_refs)}')

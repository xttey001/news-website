import json, re

path = r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js'
with open(path, 'r', encoding='utf-8') as f:
    raw = f.read()

# Extract the JSON part (after "const newsData = ")
m = re.search(r'const newsData = (.+);?\s*$', raw, re.DOTALL)
if not m:
    print('Pattern not found')
    exit()
data_str = m.group(1).strip()
if data_str.endswith(';'):
    data_str = data_str[:-1]

# Parse JSON
obj = json.loads(data_str)

# For each date, upgrade stocks arrays from string[] to object[]
for date_key, date_data in obj.items():
    for category in ['s_level', 'a_level', 'douyin']:
        if category not in date_data:
            continue
        for item in date_data[category]:
            if 'stocks' not in item:
                continue
            new_stocks = []
            for s in item['stocks']:
                if isinstance(s, dict):
                    new_stocks.append(s)
                elif isinstance(s, str):
                    # Infer sentiment from related ETFs
                    related_etf = None
                    if item.get('etfs') and len(item['etfs']) > 0:
                        related_etf = item['etfs'][0]
                    
                    if related_etf:
                        sentiment = related_etf.get('sentiment', 'neutral')
                    else:
                        sentiment = 'neutral'
                    
                    new_stocks.append({
                        'name': s,
                        'sentiment': sentiment,
                        'reason': '受益于' if sentiment == '利好' else '受限于' if sentiment == '利空' else '板块联动'
                    })
            item['stocks'] = new_stocks

# Re-serialize with indent
new_json = json.dumps(obj, ensure_ascii=False, indent=2)
new_file = 'const newsData = ' + new_json + ';\n'

with open(path, 'w', encoding='utf-8') as f:
    f.write('// 新闻数据 - 自动生成\n')
    f.write(new_file)

print('Done. Dates processed:', list(obj.keys()))
for k, v in obj.items():
    count = sum(len(v.get(c, [])) for c in ['s_level', 'a_level', 'douyin'])
    print(f'  {k}: {count} news items')

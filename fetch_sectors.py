import urllib.request, json

url = 'https://push2.eastmoney.com/api/qt/clist/get?cb=&pn=1&pz=10&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:2+f:!50&fields=f2,f3,f4,f12,f14&_=1711440000000'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read().decode('utf-8'))

print('3月26日 申万行业板块 涨幅TOP10:')
print('-' * 50)
sectors = []
for i, item in enumerate(data['data']['diff'][:10], 1):
    name = item['f14']
    change = item['f3']
    index = item['f2']
    print(f'{i}. {name}  涨幅: {change:+.2f}%  指数: {index}')
    sectors.append({'name': name, 'change': change, 'index': index})

# 输出JSON供后续使用
print('\n--- JSON ---')
print(json.dumps(sectors[:5], ensure_ascii=False))

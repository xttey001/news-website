# -*- coding: utf-8 -*-
import requests, sys, json
sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 财经新闻源
sources = {
    'sina': 'https://finance.sina.com.cn/',
    'tencent': 'https://finance.qq.com/',
    'eastmoney': 'https://www.eastmoney.com/',
    'cls': 'https://www.cls.cn/',
}

print('=== 测试新闻源可访问性 ===')
for name, url in sources.items():
    try:
        r = requests.get(url, timeout=10, headers=headers)
        print(f'{name}: {r.status_code}')
    except Exception as e:
        print(f'{name}: 错误 - {e}')

# 尝试获取新浪财经首页内容
print('\n=== 获取新浪财经首页 ===')
r = requests.get('https://finance.sina.com.cn/', timeout=10, headers=headers)
print(f'Status: {r.status_code}')
print(f'Content length: {len(r.text)}')

# 简单提取标题
import re
titles = re.findall(r'<a[^>]*title="([^"]+)"[^>]*>([^<]+)</a>', r.text)
print(f'\n找到 {len(titles)} 个标题')
for t in titles[:10]:
    print(f'  - {t[0][:60]}')
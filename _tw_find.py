# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('  "2026-04-02"')
end = content.find('  "2026-04-01"')
print(f'Start: {start}, End: {end}')
if start >= 0 and end >= 0:
    print(f'Block: {end - start} chars, {content[start:end].count(chr(10))} lines')

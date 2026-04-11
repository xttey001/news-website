# -*- coding: utf-8 -*-
import re

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the 2026-04-10 section
match = re.search(r'"2026-04-10":\s*\{', content)
if match:
    start = match.end()
    # Find the matching closing brace
    brace_count = 1
    i = start
    while brace_count > 0 and i < len(content):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
        i += 1
    section = content[start:i]
    # Extract field names
    fields = re.findall(r'"(\w+)":', section[:3000])
    print('Fields in 2026-04-10:')
    for f in sorted(set(fields)):
        print(f'  - {f}')
else:
    print('Not found')
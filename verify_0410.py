# -*- coding: utf-8 -*-
import re

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find sangsha_module for 2026-04-10
match = re.search(r'"2026-04-10":\s*\{', content)
if match:
    start = match.start()
    section = content[start:start+8000]
    has_sangsha = 'sangsha_module' in section
    has_white = 'white_dragon' in section
    print(f'Has sangsha_module: {has_sangsha}')
    print(f'Has white_dragon: {has_white}')
    
    # Show first occurrence of each
    if has_sangsha:
        idx = section.find('sangsha_module')
        print(f'\nsangsha_module snippet:')
        print(section[idx:idx+200])
else:
    print('2026-04-10 not found')
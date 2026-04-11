# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('github-pages-deploy/news-data.js', encoding='utf-8') as f:
    content = f.read()

for date in ['2026-04-11']:
    start = content.find(f'"{date}": {{')
    if start == -1:
        print(f'{date}: NOT FOUND')
        continue
    
    brace_count = 0
    in_block = False
    end = start
    for i in range(start, len(content)):
        if content[i] == '{':
            brace_count += 1
            in_block = True
        elif content[i] == '}':
            brace_count -= 1
            if in_block and brace_count == 0:
                end = i + 1
                break
    block = content[start:end]
    
    print(f'=== {date} 字段检查 ===')
    for field in ['wukong_judgment', 'bajie_conclusion', 'sangsha_module', 'white_dragon', 'tang_sanzang', 's_level', 'a_level', 'all_news']:
        if f'"{field}":' in block:
            # Show first 200 chars
            idx = block.find(f'"{field}":')
            print(f'  ✅ {field}: FOUND')
            print(f'     preview: {block[idx:idx+200].strip()[:200]}')
        else:
            print(f'  ❌ {field}: MISSING')
    print()
    
    # Check original bajie fields vs fusion fields
    bj_start = block.find('"bajie_conclusion":')
    if bj_start >= 0:
        bj_block = block[bj_start:bj_start+800]
        print('=== bajie_conclusion 全部字段 ===')
        fields = re.findall(r'"(\w+)":', bj_block)
        for f in fields:
            print(f'  - {f}')

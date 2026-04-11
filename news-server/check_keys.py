# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('github-pages-deploy/news-data.js', encoding='utf-8') as f:
    content = f.read()

start = content.find('"2026-04-11": {')
if start == -1:
    print('04-11 NOT FOUND')
else:
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

    keys = re.findall(r'"(bajie_conclusion|sangsha_module|white_dragon|tang_sanzang|wukong_judgment)":', block)
    print('Keys in 04-11:', sorted(set(keys)))

    # Show sangsha_module
    sg_start = block.find('"sangsha_module":')
    if sg_start >= 0:
        print('\n=== sangsha_module (first 300 chars) ===')
        print(block[sg_start:sg_start+300])
    else:
        print('\nsangsha_module: NOT FOUND')

    # Show bajie_conclusion
    bj_start = block.find('"bajie_conclusion":')
    if bj_start >= 0:
        print('\n=== bajie_conclusion (first 400 chars) ===')
        print(block[bj_start:bj_start+400])
    else:
        print('\nbajie_conclusion: NOT FOUND')

    # Show tang_sanzang
    ts_start = block.find('"tang_sanzang":')
    if ts_start >= 0:
        print('\ntang_sanzang: FOUND')
    else:
        print('\ntang_sanzang: NOT FOUND')

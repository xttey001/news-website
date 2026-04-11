# -*- coding: utf-8 -*-
import re

with open('recovered_data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 找4.05块
m = re.search(r'"2026-04-05":\s*\{', raw)
if m:
    brace = raw.find('{', m.start())
    depth = 0
    end_pos = brace
    for i in range(brace, len(raw)):
        c = raw[i]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end_pos = i + 1
                break
    
    block = raw[brace:end_pos]
    # 清理
    clean = block.replace("'", '"').replace('\u201c', '"').replace('\u201d', '"')
    clean = re.sub(r'//.*', '', clean)
    clean = re.sub(r',(\s*[}\]])', r'\1', clean)
    
    import json
    try:
        data = json.loads(clean)
        print('Parsed OK:', data.get('date'))
        # 保存
        with open('orig_20260405.json', 'w', encoding='utf-8') as f2:
            json.dump(data, f2, ensure_ascii=False, indent=2)
        print('Saved orig_20260405.json')
    except json.JSONDecodeError as e:
        print('Error at pos', e.pos)
        print('Context:', repr(clean[max(0,e.pos-50):e.pos+100]))

# -*- coding: utf-8 -*-
"""正确提取原始 news-data.js 中的数据"""
import re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 找到每个日期块的起始和结束位置
# 策略：找到 "date": "YYYY-MM-DD" 模式，向前找到 { ，向后找到配对的 }

def extract_date_blocks(raw):
    """提取每个日期的JSON块"""
    blocks = {}
    
    # 找所有 "date": "2026-XX-XX" 位置
    pattern = re.compile(r'"date":\s*"(2026-\d{2}-\d{2})"')
    
    for m in pattern.finditer(raw):
        date = m.group(1)
        if date in blocks:  # 已处理
            continue
        
        # 向前找到这个日期的 { 开始
        start = m.start()
        while start > 0 and raw[start] != '{':
            start -= 1
        
        # 向后找到匹配的 } 结束（简单策略：找下一个 "date": 或 availableDates）
        # 先尝试找下一层闭合
        depth = 0
        end = m.start()
        found_end = None
        
        # 找 { 和 } 平衡
        search_start = m.start()
        in_string = False
        i = search_start
        while i < len(raw):
            c = raw[i]
            if c == '"' and (i == 0 or raw[i-1] != '\\'):
                in_string = not in_string
            elif not in_string:
                if c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        found_end = i + 1
                        break
            i += 1
        
        if found_end:
            blocks[date] = raw[start:found_end]
    
    return blocks

blocks = extract_date_blocks(raw)
print(f'提取到 {len(blocks)} 个日期块: {list(blocks.keys())}')

# 只取4.04-4.08范围
target_dates = ['2026-04-08', '2026-04-07', '2026-04-04', '2026-04-05', '2026-04-06']
found_dates = {d: blocks.get(d) for d in target_dates if d in blocks}
print(f'目标日期: {list(found_dates.keys())}')

# 解析每个块
for date, block in found_dates.items():
    try:
        # 替换单引号为双引号（如果需要）
        clean = block
        data = json.loads(clean)
        print(f'  {date}: OK')
        print(f'    has wukong: {"wukong_judgment" in data}')
        print(f'    has bajie: {"bajie_conclusion" in data}')
        print(f'    S-level: {len(data.get("s_level", []))}')
    except json.JSONDecodeError as e:
        print(f'  {date}: JSON error: {e}')
        # 尝试修复
        try:
            # 替换中文引号、单引号
            clean = block.replace("'", '"').replace('\u201c', '"').replace('\u201d', '"')
            data = json.loads(clean)
            print(f'    FIXED: OK after quote replacement')
            print(f'    has wukong: {"wukong_judgment" in data}')
            print(f'    has bajie: {"bajie_conclusion" in data}')
            print(f'    S-level: {len(data.get("s_level", []))}')
            found_dates[date] = clean  # 更新为clean版本
        except:
            print(f'    Still broken')

# 保存提取的数据供后续使用
with open('extracted_missing_dates.json', 'w', encoding='utf-8') as f:
    json.dump(found_dates, f, ensure_ascii=False, indent=2)
print('\nSaved to extracted_missing_dates.json')

# -*- coding: utf-8 -*-
"""用正则提取原始 news-data.js 中的日期块，修复格式错误"""
import re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 用正则提取 "bajie_conclusion" 等可能含中文引号的关键区块
# 策略：分别提取每个日期的 wukong_judgment, bajie_conclusion, s_level 等部分

target_dates = ['2026-04-08', '2026-04-07']

def extract_field_block(raw, date, field_name):
    """提取指定日期的指定字段块"""
    # 找字段开始: "field_name": {
    pattern = rf'"{re.escape(field_name)}":\s*\{{'
    m = re.search(pattern, raw)
    if not m:
        return None
    
    start = m.start()
    depth = 0
    in_str = False
    i = start
    while i < len(raw):
        c = raw[i]
        if c == '"' and (i == 0 or raw[i-1] != '\\'):
            in_str = not in_str
        elif not in_str:
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return raw[start:i+1]
        i += 1
    return None

for date in target_dates:
    print(f'\n=== {date} ===')
    
    # 提取基础信息
    date_pattern = rf'"{re.escape(date)}":\s*\{{'
    m = re.search(date_pattern, raw)
    if not m:
        print('  Date not found')
        continue
    
    # 向前找到 {
    obj_start = m.start()
    while obj_start > 0 and raw[obj_start] != '{{':
        obj_start -= 1
    
    # 找到 } 闭合
    depth = 0
    in_str = False
    obj_end = m.start()
    for i in range(m.start(), len(raw)):
        c = raw[i]
        if c == '"' and (i == 0 or raw[i-1] != '\\'):
            in_str = not in_str
        elif not in_str:
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    obj_end = i + 1
                    break
    
    block = raw[obj_start:obj_end]
    
    # 尝试解析
    try:
        data = json.loads(block)
        print(f'  Direct parse: OK')
    except json.JSONDecodeError as e:
        print(f'  Direct parse failed: {e}')
        
        # 修复：替换中文引号
        block2 = block.replace(''', '"').replace(''', '"').replace('「', '"').replace('」', '"')
        try:
            data = json.loads(block2)
            print(f'  Fixed with Chinese quotes: OK')
        except json.JSONDecodeError as e2:
            print(f'  Still failed: {e2}')
            
            # 深度修复：处理所有可能的编码问题
            # 逐字符检查
            cleaned = []
            i = 0
            while i < len(block2):
                c = block2[i]
                code = ord(c)
                # 保留ASCII、可打印Unicode、中文
                if code < 0x80 or (0x4E00 <= code <= 0x9FFF) or (0x3000 <= code <= 0x303F) or c in ' \n\t{}[]:,"':
                    cleaned.append(c)
                else:
                    cleaned.append(' ')  # 替换不可见字符
                i += 1
            block3 = ''.join(cleaned)
            
            # 移除多余逗号
            block3 = re.sub(r',\s*}', '}', block3)
            block3 = re.sub(r',\s*]', ']', block3)
            
            try:
                data = json.loads(block3)
                print(f'  Deep cleaned: OK')
            except json.JSONDecodeError as e3:
                print(f'  Deep clean failed: {e3}')
                # 输出问题区域
                lines = block3.split('\n')
                if 'line' in str(e3):
                    try:
                        line_num = int(str(e3).split('line ')[1].split()[0])
                        print(f'  Problem area (line {line_num}):')
                        for i in range(max(0,line_num-3), min(len(lines), line_num+2)):
                            print(f'    {i+1}: {lines[i][:80]}')
                    except:
                        pass
                data = None
    
    if data:
        print(f'  Fields: date={data.get("date")}, has_wukong={bool(data.get("wukong_judgment"))}, has_bajie={bool(data.get("bajie_conclusion"))}, s_count={len(data.get("s_level",[]))}')
        # 保存
        with open(f'extracted_{date.replace("-","")}.json', 'w', encoding='utf-8') as f2:
            json.dump(data, f2, ensure_ascii=False, indent=2)
        print(f'  Saved to extracted_{date.replace("-","")}.json')

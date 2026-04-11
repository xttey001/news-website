# -*- coding: utf-8 -*-
"""用node验证+提取原始数据"""
import re, sys, io, json, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 用node验证原始文件
result = subprocess.run(['node', '--check', 'news-data.js'], 
                       capture_output=True, text=True, 
                       cwd='C:\\Users\\asus\\.qclaw\\workspace\\news-server')
print('Node check:', result.returncode)
if result.stderr:
    print('  Error:', result.stderr[:200])

# 读取原始文件（作为纯文本）
with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 直接用文本方式提取4.08和4.07
# 找 "2026-04-08": { 开头，向后找闭合
def find_json_object(raw, start_pattern):
    """从start_pattern开始，找到对应的JSON对象"""
    idx = raw.find(start_pattern)
    if idx == -1:
        return None, -1
    
    # 找到 { 的位置
    brace = raw.find('{', idx)
    if brace == -1:
        return None, -1
    
    # 平衡括号
    depth = 0
    i = brace
    while i < len(raw):
        if raw[i] == '{':
            depth += 1
        elif raw[i] == '}':
            depth -= 1
            if depth == 0:
                return raw[brace:i+1], i+1
        i += 1
    return None, -1

# 提取4.08
obj_04_08, end_04_08 = find_json_object(raw, '"2026-04-08":')
obj_04_07, end_04_07 = find_json_object(raw, '"2026-04-07":')

for name, obj in [('2026-04-08', obj_04_08), ('2026-04-07', obj_04_07)]:
    if obj:
        print(f'\n{name}: found {len(obj)} chars')
        
        # 清理并解析
        clean = obj.replace(''', '"').replace(''', '"')
        clean = re.sub(r'//.*', '', clean)  # 移除注释
        
        try:
            data = json.loads(clean)
            print(f'  Parsed OK: has_wukong={bool(data.get("wukong_judgment"))}, s_count={len(data.get("s_level",[]))}')
            
            # 保存
            fname = f'orig_{name.replace("-","")}.json'
            with open(fname, 'w', encoding='utf-8') as f2:
                json.dump(data, f2, ensure_ascii=False, indent=2)
            print(f'  Saved: {fname}')
        except json.JSONDecodeError as e:
            print(f'  Parse error: {e}')
            # 输出问题附近
            print(f'  Preview: {clean[max(0,e.pos-50):e.pos+50]}')
    else:
        print(f'\n{name}: NOT FOUND')

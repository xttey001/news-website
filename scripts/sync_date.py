#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
同步指定日期的数据从 news-data.js 到独立 JSON 文件

使用方法:
    python scripts/sync_date.py 2026-05-20
"""

import json
import re
import sys
from pathlib import Path


def extract_date_from_js(js_content, date_str):
    """从 JS 内容中提取指定日期的数据"""
    # 找到日期键的位置
    date_key = f'"{date_str}"'
    date_start = js_content.find(date_key)
    
    if date_start == -1:
        print(f"❌ 未找到日期 {date_str}")
        return None
    
    # 找到这个日期数据的开始（跳过键名和冒号）
    data_start = js_content.find('{', date_start)
    
    # 找到这个日期数据的结束（匹配的大括号）
    brace_count = 0
    pos = data_start
    in_string = False
    string_char = None
    escape_next = False
    
    while pos < len(js_content):
        char = js_content[pos]
        
        if escape_next:
            escape_next = False
            pos += 1
            continue
        
        if char == '\\':
            escape_next = True
            pos += 1
            continue
        
        if not in_string and char in '"\'`':
            in_string = True
            string_char = char
        elif in_string and char == string_char:
            in_string = False
            string_char = None
        elif not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # 找到结束位置
                    data_end = pos + 1
                    break
        
        pos += 1
    
    # 提取数据
    date_content = js_content[data_start:data_end]
    
    # 移除 trailing commas
    date_content = re.sub(r',(\s*[}\]])', r'\1', date_content)
    
    # 确保所有 key 都有引号
    date_content = re.sub(r'([{,]\s*)([a-zA-Z_\u4e00-\u9fa5][a-zA-Z0-9_\u4e00-\u9fa5]*)\s*:', r'\1"\2":', date_content)
    
    try:
        data = json.loads(date_content)
        data['date'] = date_str
        return data
    except json.JSONDecodeError as e:
        print(f"⚠ JSON 解析失败: {e}")
        # 尝试使用 ast.literal_eval
        try:
            import ast
            data = ast.literal_eval(date_content)
            data['date'] = date_str
            return data
        except Exception as e2:
            print(f"❌ 完全失败: {e2}")
            return None


def main():
    if len(sys.argv) < 2:
        print("用法: python scripts/sync_date.py <日期>")
        print("示例: python scripts/sync_date.py 2026-05-20")
        return
    
    date_str = sys.argv[1]
    
    # 路径配置
    workspace_dir = Path(__file__).parent.parent
    news_data_js = workspace_dir / 'news-data.js'
    target_file = workspace_dir / 'news-data' / f"{date_str}.json"
    
    print(f"=" * 50)
    print(f"同步日期数据: {date_str}")
    print(f"=" * 50)
    
    # 读取 JS 文件
    with open(news_data_js, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # 提取数据
    data = extract_date_from_js(js_content, date_str)
    
    if data:
        # 保存到目标文件
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 已同步到: {target_file}")
        print(f"✓ 数据大小: {len(json.dumps(data, ensure_ascii=False))} 字符")
    else:
        print(f"❌ 同步失败")


if __name__ == '__main__':
    main()

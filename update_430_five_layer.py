# -*- coding: utf-8 -*-
import json

# 读取完整数据
with open('news-evolution/complete_430_data.json', 'r', encoding='utf-8') as f:
    new_data = json.load(f)

# 读取现有news-data.js
with open('news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到2026-04-30的位置
start_marker = '"2026-04-30": {'
start_idx = content.find(start_marker)

if start_idx != -1:
    # 找到结束位置（下一个日期）
    end_marker = ',\n  "2026-04-29"'
    end_idx = content.find(end_marker, start_idx)
    
    if end_idx != -1:
        # 构建新的数据
        new_data_str = json.dumps(new_data, ensure_ascii=False, indent=2)
        new_content = content[:start_idx] + '"2026-04-30": ' + new_data_str + content[end_idx:]
        
        # 写回文件
        with open('news-data.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print('✅ news-data.js 更新成功')
    else:
        print('❌ 未找到结束标记')
else:
    print('❌ 未找到2026-04-30数据')

# -*- coding: utf-8 -*-
import json
import re
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/asus/temp-news-website/news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'newsData\s*=\s*(\{[\s\S]*?\});\s*const availableDates', content)
if match:
    # 替换 JS 布尔值为 Python 布尔值
    import re
    json_str = match[1]
    json_str = re.sub(r'\btrue\b', 'True', json_str)
    json_str = re.sub(r'\bfalse\b', 'False', json_str)
    json_str = re.sub(r'\bnull\b', 'None', json_str)
    news_data = eval(json_str)
    dates = ['2026-04-14', '2026-04-15', '2026-04-16', '2026-04-17', '2026-04-18']
    
    summary = []
    for d in dates:
        if d in news_data:
            day = news_data[d]
            wj = day.get('wukong_judgment', {})
            sent = 'N/A'
            if wj:
                sent = wj.get('market_sentiment') or wj.get('emotion') or 'N/A'
            tone = day.get('market_tone', {})
            tone_str = 'N/A'
            if isinstance(tone, dict):
                tone_str = tone.get('晚报', 'N/A')[:60] if tone.get('晚报') else 'N/A'
            
            summary.append({
                'date': d,
                'sentiment': sent[:50] if sent else 'N/A',
                'tone': tone_str
            })
    
    print(json.dumps(summary, ensure_ascii=False, indent=2))

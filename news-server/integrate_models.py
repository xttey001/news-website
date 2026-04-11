# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""集成沙僧和白龙马模型到news-data.js"""

import sys
sys.path.insert(0, '.')
import json
import re

# ========== 1. 加载新闻数据 ==========
with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 移除注释
content = re.sub(r'//.*', '', content)
# 替换单引号为双引号
content = content.replace("'", '"')
# 移除尾随逗号
content = re.sub(r',(\s*[}\])])', r'\1', content)

# 提取newsData
start = content.find('const newsData = ')
end = content.find(';const availableDates', start)
json_str = content[start+len('const newsData = '):end]

try:
    news_data = json.loads(json_str)
    print('OK - News data loaded')
except:
    news_data = eval(json_str)
    print('OK - News data loaded (eval)')

# ========== 2. 获取市场数据 ==========
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
market_data = get_market_data(codes, 7)
print(f'OK - Market data: {len(market_data)} codes')

# ========== 3. 运行沙僧模型 ==========
sangsha_result = run_sangsha(news_data, '2026-04-09', market_data)
print(f'OK - Sangsha: {sangsha_result.get("沙僧模块", {}).get("overall_sentiment", "N/A")}')

# ========== 4. 运行白龙马模型 ==========
sg = sangsha_result.get('沙僧模块', {})
dragon_result = run_white_dragon(market_data, sg.get('analysis_results', []))
print(f'OK - WhiteDragon: {dragon_result.get("白龙马决策", {}).get("主力状态", "N/A")}')

# ========== 5. 把结果添加到新闻数据（每个日期） ==========
for date in news_data:
    if date == 'availableDates':
        continue
    news_data[date]['sangsha_module'] = sg
    news_data[date]['white_dragon'] = dragon_result.get('白龙马决策', {})

# ========== 6. 生成新的news-data.js ==========
output_js = 'const newsData = ' + json.dumps(news_data, ensure_ascii=False, indent=2) + ';\n\nconst availableDates = ' + json.dumps(news_data.get('availableDates', ['2026-04-09', '2026-04-08', '2026-04-07', '2026-04-03', '2026-04-02']), ensure_ascii=False) + ';\n\n// 获取指定日期的新闻\nfunction getNews(date) {\n    return newsData[date] || null;\n}\n\n// 获取前一天\nfunction getPreviousDate(date) {\n    const idx = availableDates.indexOf(date);\n    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;\n}\n\n// 获取后一天\nfunction getNextDate(date) {\n    const idx = availableDates.indexOf(date);\n    return idx > 0 ? availableDates[idx - 1] : null;\n}'

# 保存
with open('github-pages-deploy/news-data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print('OK - Saved to github-pages-deploy/news-data.js')
print('\n=== Done ===')
"""
GitHub Pages 部署方案
方案：将动态新闻转换为静态 HTML，推送到 GitHub Pages
"""
import json
import os
from datetime import datetime

# 读取今天的新闻数据
news_file = "news_data/news_2026-03-29.json"
with open(news_file, 'r', encoding='utf-8') as f:
    news = json.load(f)

# 生成静态 HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>财经新闻速览 - {news["date"]}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        h1 {{
            color: #4CAF50;
            font-size: 28px;
            margin-bottom: 10px;
        }}
        .date {{
            color: #888;
            font-size: 14px;
        }}
        .market-tone {{
            background: rgba(255,193,7,0.1);
            border-left: 4px solid #FFC107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
        }}
        .market-tone strong {{
            color: #FFC107;
        }}
        .section {{
            margin: 30px 0;
        }}
        .section-title {{
            font-size: 22px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid;
        }}
        .s-level .section-title {{ color: #f44336; border-color: #f44336; }}
        .a-level .section-title {{ color: #FFC107; border-color: #FFC107; }}
        .douyin .section-title {{ color: #2196F3; border-color: #2196F3; }}
        .news-item {{
            background: rgba(255,255,255,0.05);
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s;
        }}
        .news-item:hover {{
            background: rgba(255,255,255,0.08);
            transform: translateX(5px);
        }}
        .news-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 12px;
            color: #fff;
        }}
        .news-row {{
            margin: 8px 0;
            font-size: 14px;
        }}
        .label {{
            color: #888;
            margin-right: 8px;
        }}
        .bullish {{ color: #f44336; }}
        .bearish {{ color: #4CAF50; }}
        .etf-tag {{
            display: inline-block;
            background: rgba(76,175,80,0.2);
            color: #4CAF50;
            padding: 3px 10px;
            border-radius: 12px;
            margin: 3px;
            font-size: 12px;
        }}
        .stock-tag {{
            display: inline-block;
            background: rgba(33,150,243,0.2);
            color: #2196F3;
            padding: 3px 10px;
            border-radius: 12px;
            margin: 3px;
            font-size: 12px;
        }}
        footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 今日财经新闻速览</h1>
            <div class="date">{news["date"]}</div>
        </header>

        <div class="market-tone">
            <strong>⚠️ 今日市场总基调：</strong>{news["market_tone"]}
        </div>

        <div class="section s-level">
            <h2 class="section-title">🔴 S级 - 主线级</h2>
'''

# 添加 S 级新闻
for item in news["s_level"]:
    etf_html = " ".join([f'<span class="etf-tag">{e["name"]}({e["sentiment"]})</span>' for e in item["etfs"]])
    stock_html = " ".join([f'<span class="stock-tag">{s}</span>' for s in item["stocks"]])

    html += f'''
            <div class="news-item">
                <div class="news-title">{item["emoji"]} {item["title"]}</div>
                <div class="news-row"><span class="label">📌 要点：</span>{item["summary"]}</div>
                <div class="news-row"><span class="label">⏱️ 影响时长：</span>{item["duration"]}</div>
                <div class="news-row"><span class="label">📈 映射ETF：</span>{etf_html}</div>
                <div class="news-row"><span class="label">✨ 映射个股：</span>{stock_html}</div>
                <div class="news-row"><span class="label">💡 资金信号：</span>{item["signal"]}</div>
            </div>
'''

html += '''
        </div>

        <div class="section a-level">
            <h2 class="section-title">🟡 A级 - 轮动级</h2>
'''

# 添加 A 级新闻
for item in news["a_level"]:
    etf_html = " ".join([f'<span class="etf-tag">{e["name"]}({e["sentiment"]})</span>' for e in item["etfs"]])
    stock_html = " ".join([f'<span class="stock-tag">{s}</span>' for s in item["stocks"]])

    html += f'''
            <div class="news-item">
                <div class="news-title">{item["emoji"]} {item["title"]}</div>
                <div class="news-row"><span class="label">📌 要点：</span>{item["summary"]}</div>
                <div class="news-row"><span class="label">⏱️ 影响时长：</span>{item["duration"]}</div>
                <div class="news-row"><span class="label">📈 映射ETF：</span>{etf_html}</div>
                <div class="news-row"><span class="label">✨ 映射个股：</span>{stock_html}</div>
                <div class="news-row"><span class="label">💡 资金信号：</span>{item["signal"]}</div>
            </div>
'''

html += '''
        </div>

        <div class="section douyin">
            <h2 class="section-title">📱 抖音相关</h2>
'''

# 添加抖音相关新闻
for item in news["douyin"]:
    etf_html = " ".join([f'<span class="etf-tag">{e["name"]}({e["sentiment"]})</span>' for e in item["etfs"]])
    stock_html = " ".join([f'<span class="stock-tag">{s}</span>' for s in item["stocks"]])

    html += f'''
            <div class="news-item">
                <div class="news-title">{item["emoji"]} {item["title"]}</div>
                <div class="news-row"><span class="label">📌 要点：</span>{item["summary"]}</div>
                <div class="news-row"><span class="label">⏱️ 影响时长：</span>{item["duration"]}</div>
                <div class="news-row"><span class="label">📈 映射ETF：</span>{etf_html}</div>
                <div class="news-row"><span class="label">✨ 映射个股：</span>{stock_html}</div>
                <div class="news-row"><span class="label">💡 资金信号：</span>{item["signal"]}</div>
            </div>
'''

html += f'''
        </div>

        <footer>
            <p>生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p>数据来源：网易财经、权威财经媒体</p>
        </footer>
    </div>
</body>
</html>
'''

# 保存静态 HTML
output_file = "index.html"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"[OK] Static HTML generated: {output_file}")
print(f"[OK] File size: {len(html)} bytes")
print("\nNext: Push to GitHub Pages")

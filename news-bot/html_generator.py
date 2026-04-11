#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经新闻 HTML 生成器
将原始新闻数据转换为专业 HTML 格式
"""

import json
import os
from datetime import datetime

def generate_html_news(news_data, output_path=None):
    """
    生成 HTML 格式的新闻页面
    
    Args:
        news_data: 新闻数据字典，包含 s_level, a_level, douyin 等键
        output_path: 输出文件路径，如果为 None 则使用时间戳
    
    Returns:
        生成的 HTML 文件路径
    """
    
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"news-output-{timestamp}.html"
    
    # 获取今天日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 构建 HTML
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>财经新闻速览 · {today}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary: #1a1a2e;
            --secondary: #16213e;
            --accent-red: #e74c3c;
            --accent-gold: #f39c12;
            --accent-green: #27ae60;
            --text-primary: #ecf0f1;
            --text-secondary: #bdc3c7;
            --border: #2c3e50;
            --bg-gradient: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        }}

        body {{
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: var(--bg-gradient);
            color: var(--text-primary);
            line-height: 1.8;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        .header {{
            text-align: center;
            margin-bottom: 50px;
            animation: slideDown 0.8s ease-out;
        }}

        .header-title {{
            font-size: 2.5em;
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #f39c12, #e74c3c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .header-date {{
            font-size: 1.1em;
            color: var(--text-secondary);
            letter-spacing: 1px;
        }}

        .market-tone {{
            background: rgba(231, 76, 60, 0.1);
            border-left: 4px solid var(--accent-red);
            padding: 25px;
            margin-bottom: 40px;
            border-radius: 8px;
            animation: slideUp 0.8s ease-out 0.2s both;
        }}

        .market-tone-label {{
            font-size: 0.9em;
            color: var(--accent-red);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }}

        .market-tone-content {{
            font-size: 1.1em;
            line-height: 1.8;
            color: var(--text-primary);
        }}

        .section {{
            margin-bottom: 50px;
        }}

        .section-title {{
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 2px solid var(--border);
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .section-title.s-level {{
            color: var(--accent-red);
        }}

        .section-title.a-level {{
            color: var(--accent-gold);
        }}

        .section-title.douyin-level {{
            color: #3498db;
        }}

        .news-item {{
            background: rgba(44, 62, 80, 0.3);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 25px;
            transition: all 0.3s ease;
            animation: fadeInUp 0.6s ease-out both;
        }}

        .news-item:hover {{
            background: rgba(44, 62, 80, 0.5);
            border-color: var(--accent-gold);
            transform: translateY(-5px);
        }}

        .news-title {{
            font-size: 1.4em;
            font-weight: 700;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .news-title-emoji {{
            font-size: 1.3em;
        }}

        .news-field {{
            margin-bottom: 18px;
            display: flex;
            gap: 15px;
        }}

        .news-field-label {{
            font-weight: 600;
            color: var(--text-secondary);
            min-width: 100px;
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }}

        .news-field-content {{
            flex: 1;
            color: var(--text-primary);
            line-height: 1.7;
        }}

        .etf-item {{
            display: inline-block;
            background: rgba(52, 152, 219, 0.15);
            padding: 6px 12px;
            border-radius: 20px;
            margin-right: 10px;
            margin-bottom: 8px;
            font-size: 0.95em;
            border: 1px solid rgba(52, 152, 219, 0.3);
        }}

        .etf-item.bullish {{
            background: rgba(231, 76, 60, 0.15);
            border-color: rgba(231, 76, 60, 0.3);
        }}

        .etf-item.bearish {{
            background: rgba(39, 174, 96, 0.15);
            border-color: rgba(39, 174, 96, 0.3);
        }}

        .stock-item {{
            display: inline-block;
            background: rgba(155, 89, 182, 0.15);
            padding: 6px 12px;
            border-radius: 20px;
            margin-right: 10px;
            margin-bottom: 8px;
            font-size: 0.95em;
            border: 1px solid rgba(155, 89, 182, 0.3);
        }}

        .signal-box {{
            background: rgba(243, 156, 18, 0.1);
            border-left: 3px solid var(--accent-gold);
            padding: 15px;
            margin-top: 15px;
            border-radius: 6px;
            font-size: 0.95em;
            color: var(--text-secondary);
        }}

        @keyframes slideDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes slideUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 20px 15px;
            }}

            .header-title {{
                font-size: 1.8em;
            }}

            .news-item {{
                padding: 20px;
            }}

            .news-title {{
                font-size: 1.2em;
            }}

            .news-field {{
                flex-direction: column;
                gap: 8px;
            }}

            .news-field-label {{
                min-width: auto;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-title">📊 今日新闻速览</div>
            <div class="header-date">{today}</div>
        </div>

        <div class="market-tone">
            <div class="market-tone-label">⚠️ 今日市场总基调</div>
            <div class="market-tone-content">
                {news_data.get('market_tone', '市场基调待更新')}
            </div>
        </div>

        {_generate_section(news_data.get('s_level', []), 'S级 — 主线级', 's-level', '🔴')}
        {_generate_section(news_data.get('a_level', []), 'A级 — 轮动级', 'a-level', '🟡')}
        {_generate_section(news_data.get('douyin', []), '抖音相关', 'douyin-level', '📱')}
    </div>
</body>
</html>"""

    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_path


def _generate_section(items, title, css_class, emoji):
    """生成新闻分类段落"""
    if not items:
        return ""
    
    html = f'<div class="section">\n'
    html += f'    <div class="section-title {css_class}">\n'
    html += f'        <span>{emoji}</span>\n'
    html += f'        <span>{title}</span>\n'
    html += f'    </div>\n'
    
    for i, item in enumerate(items):
        html += _generate_news_item(item, i)
    
    html += '</div>\n'
    return html


def _generate_news_item(item, index):
    """生成单条新闻"""
    html = f'    <div class="news-item" style="animation-delay: {0.3 + index * 0.1}s">\n'
    
    # 标题
    emoji = item.get('emoji', '📰')
    title = item.get('title', '未命名新闻')
    html += f'        <div class="news-title">\n'
    html += f'            <span class="news-title-emoji">{emoji}</span>\n'
    html += f'            <span>{title}</span>\n'
    html += f'        </div>\n'
    
    # 要点
    if item.get('summary'):
        html += f'        <div class="news-field">\n'
        html += f'            <div class="news-field-label">📌 要点</div>\n'
        html += f'            <div class="news-field-content">{item["summary"]}</div>\n'
        html += f'        </div>\n'
    
    # 影响时长
    if item.get('duration'):
        html += f'        <div class="news-field">\n'
        html += f'            <div class="news-field-label">⏱️ 影响时长</div>\n'
        html += f'            <div class="news-field-content">{item["duration"]}</div>\n'
        html += f'        </div>\n'
    
    # ETF
    if item.get('etfs'):
        html += f'        <div class="news-field">\n'
        html += f'            <div class="news-field-label">📈 映射ETF</div>\n'
        html += f'            <div class="news-field-content">\n'
        for etf in item['etfs']:
            etf_class = 'bullish' if etf.get('sentiment') == '利好' else 'bearish'
            html += f'                <div class="etf-item {etf_class}">{etf["name"]} · {etf.get("sentiment", "中性")}</div>\n'
        html += f'            </div>\n'
        html += f'        </div>\n'
    
    # 个股
    if item.get('stocks'):
        html += f'        <div class="news-field">\n'
        html += f'            <div class="news-field-label">✨ 映射个股</div>\n'
        html += f'            <div class="news-field-content">\n'
        for stock in item['stocks']:
            html += f'                <div class="stock-item">{stock}</div>\n'
        html += f'            </div>\n'
        html += f'        </div>\n'
    
    # 资金信号
    if item.get('signal'):
        html += f'        <div class="signal-box">\n'
        html += f'            💡 <strong>资金信号：</strong>{item["signal"]}\n'
        html += f'        </div>\n'
    
    html += '    </div>\n'
    return html


if __name__ == '__main__':
    # 示例数据
    sample_data = {
        'market_tone': '地缘风险主导，机构避险情绪升温',
        's_level': [
            {
                'emoji': '🔥',
                'title': '霍尔木兹海峡局势：全线大涨',
                'summary': '美以伊冲突升温，原油/能源板块全线暴涨',
                'duration': '1-3天',
                'etfs': [
                    {'name': '159407 豆粕', 'sentiment': '利空'},
                    {'name': '518880 黄金', 'sentiment': '利好'},
                ],
                'stocks': ['600028 中国石化', '601857 中国石油'],
                'signal': '避险资金流入能源/黄金'
            }
        ],
        'a_level': [],
        'douyin': []
    }
    
    output = generate_html_news(sample_data)
    print(f"✅ HTML 生成成功: {output}")

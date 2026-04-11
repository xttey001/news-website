#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成支持历史新闻查看的静态网站
包含：时间线、日期切换、历史新闻存档
"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# 读取所有可用的新闻文件
news_dir = Path("news_data")
news_data = {}
available_dates = []

# 扫描 news_data 目录中的所有 JSON 文件
if news_dir.exists():
    for file in sorted(news_dir.glob("news_*.json"), reverse=True):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                date = data.get("date")
                if date:
                    news_data[date] = data
                    available_dates.append(date)
                    print(f"[OK] Loaded {date}")
        except Exception as e:
            print(f"[ERROR] Failed to load {file}: {e}")

# 如果没有找到任何新闻文件，使用默认的 3.29
if not news_data:
    print("[WARNING] No news files found, using default data")
    news_file = "news_data/news_2026-03-29.json"
    if os.path.exists(news_file):
        with open(news_file, 'r', encoding='utf-8') as f:
            today_news = json.load(f)
            news_data["2026-03-29"] = today_news
            available_dates = ["2026-03-29"]

# 按日期排序（最新的在前）
available_dates.sort(reverse=True)

print(f"[OK] Total dates: {len(available_dates)}")
print(f"[OK] Available dates: {available_dates}")

# 生成 JavaScript 数据文件
js_data = f"""// 新闻数据 - 自动生成
const newsData = {json.dumps(news_data, ensure_ascii=False, indent=2)};

// 获取所有可用日期
const availableDates = {json.dumps(available_dates, ensure_ascii=False)};

// 获取指定日期的新闻
function getNews(date) {{
    return newsData[date] || null;
}}

// 获取前一天
function getPreviousDate(date) {{
    const idx = availableDates.indexOf(date);
    return idx > 0 ? availableDates[idx - 1] : null;
}}

// 获取后一天
function getNextDate(date) {{
    const idx = availableDates.indexOf(date);
    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;
}}
"""

# 保存 JS 数据文件
with open("news-data.js", 'w', encoding='utf-8') as f:
    f.write(js_data)

print("[OK] Generated news-data.js")

# 生成主 HTML 文件
html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>财经新闻速览 - 历史查看</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #00d4ff, #0099ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            color: #888;
            font-size: 1.1em;
        }
        
        /* 时间线 */
        .timeline {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 40px;
            flex-wrap: wrap;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            overflow-x: auto;
        }
        
        .timeline-item {
            padding: 10px 15px;
            background: rgba(0, 212, 255, 0.1);
            border: 2px solid rgba(0, 212, 255, 0.3);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
            position: relative;
        }
        
        .timeline-item:hover {
            background: rgba(0, 212, 255, 0.2);
            border-color: rgba(0, 212, 255, 0.6);
            transform: translateY(-2px);
        }
        
        .timeline-item.active {
            background: rgba(0, 212, 255, 0.3);
            border-color: #00d4ff;
            color: #00d4ff;
            font-weight: bold;
        }
        
        /* 控制按钮 */
        .controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .btn {
            padding: 10px 20px;
            background: rgba(0, 212, 255, 0.2);
            border: 2px solid rgba(0, 212, 255, 0.5);
            color: #00d4ff;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1em;
        }
        
        .btn:hover:not(:disabled) {
            background: rgba(0, 212, 255, 0.3);
            border-color: #00d4ff;
            transform: translateY(-2px);
        }
        
        .btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }
        
        /* 日期输入 */
        .date-input-group {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        .date-input-group input {
            padding: 10px 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(0, 212, 255, 0.3);
            color: #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
        }
        
        .date-input-group input:focus {
            outline: none;
            border-color: #00d4ff;
            background: rgba(0, 212, 255, 0.1);
        }
        
        /* 新闻内容 */
        .news-container {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 30px;
            border: 1px solid rgba(0, 212, 255, 0.2);
        }
        
        .news-date {
            font-size: 1.3em;
            color: #00d4ff;
            margin-bottom: 10px;
            font-weight: bold;
        }
        
        .market-tone {
            color: #888;
            margin-bottom: 20px;
            padding: 15px;
            background: rgba(0, 212, 255, 0.05);
            border-left: 3px solid #00d4ff;
            border-radius: 5px;
        }
        
        .news-section {
            margin-bottom: 30px;
        }
        
        .section-title {
            font-size: 1.2em;
            color: #00d4ff;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
        }
        
        .news-item {
            background: rgba(0, 212, 255, 0.05);
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
            border-left: 3px solid #00d4ff;
        }
        
        .news-title {
            font-size: 1.1em;
            color: #e0e0e0;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        .news-summary {
            color: #aaa;
            margin-bottom: 10px;
            line-height: 1.6;
        }
        
        .news-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            font-size: 0.9em;
            color: #888;
        }
        
        .meta-item {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        .meta-label {
            color: #666;
            font-size: 0.85em;
        }
        
        .meta-value {
            color: #00d4ff;
        }
        
        .etf-list, .stock-list {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        
        .etf-tag, .stock-tag {
            padding: 5px 10px;
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 5px;
            font-size: 0.9em;
        }
        
        .sentiment-good {
            color: #ff4444;
        }
        
        .sentiment-bad {
            color: #44ff44;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8em;
            }
            
            .news-container {
                padding: 20px;
            }
            
            .timeline {
                gap: 8px;
            }
            
            .timeline-item {
                padding: 8px 12px;
                font-size: 0.9em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 财经新闻速览</h1>
            <p>实时财经新闻 · 历史查看 · 智能分类</p>
        </div>
        
        <div class="timeline" id="timeline"></div>
        
        <div class="controls">
            <button class="btn" id="prevBtn" onclick="showPreviousDate()">← 前一天</button>
            <button class="btn" id="todayBtn" onclick="showToday()">📅 今天</button>
            <button class="btn" id="nextBtn" onclick="showNextDate()">后一天 →</button>
            <button class="btn" onclick="toggleAllDates()">📋 查看所有日期</button>
        </div>
        
        <div class="date-input-group">
            <input type="text" id="dateInput" placeholder="输入日期 (YYYY-MM-DD)" onkeypress="handleDateInput(event)">
            <button class="btn" onclick="jumpToDate()">跳转</button>
        </div>
        
        <div class="news-container" id="newsContainer">
            <p style="text-align: center; color: #888;">加载中...</p>
        </div>
    </div>
    
    <script src="news-data.js"></script>
    <script>
        let currentDate = availableDates[0];
        
        function initTimeline() {
            const timeline = document.getElementById('timeline');
            timeline.innerHTML = '';
            
            availableDates.forEach(date => {
                const item = document.createElement('div');
                item.className = 'timeline-item' + (date === currentDate ? ' active' : '');
                item.textContent = date;
                item.onclick = () => showDate(date);
                timeline.appendChild(item);
            });
        }
        
        function showDate(date) {
            if (!availableDates.includes(date)) return;
            currentDate = date;
            updateUI();
        }
        
        function showPreviousDate() {
            const prev = getPreviousDate(currentDate);
            if (prev) showDate(prev);
        }
        
        function showNextDate() {
            const next = getNextDate(currentDate);
            if (next) showDate(next);
        }
        
        function showToday() {
            showDate(availableDates[0]);
        }
        
        function jumpToDate() {
            const input = document.getElementById('dateInput').value;
            if (availableDates.includes(input)) {
                showDate(input);
                document.getElementById('dateInput').value = '';
            } else {
                alert('日期不存在');
            }
        }
        
        function handleDateInput(event) {
            if (event.key === 'Enter') {
                jumpToDate();
            }
        }
        
        function toggleAllDates() {
            const dates = availableDates.join('\\n');
            alert('可用日期:\\n' + dates);
        }
        
        function updateUI() {
            initTimeline();
            updateButtons();
            renderNews();
        }
        
        function updateButtons() {
            document.getElementById('prevBtn').disabled = !getPreviousDate(currentDate);
            document.getElementById('nextBtn').disabled = !getNextDate(currentDate);
        }
        
        function renderNews() {
            const news = getNews(currentDate);
            if (!news) {
                document.getElementById('newsContainer').innerHTML = '<p style="text-align: center; color: #888;">该日期暂无新闻</p>';
                return;
            }
            
            let html = `
                <div class="news-date">${news.date}</div>
                <div class="market-tone">📈 ${news.market_tone}</div>
            `;
            
            if (news.s_level && news.s_level.length > 0) {
                html += '<div class="news-section">';
                html += '<div class="section-title">🔴 S级新闻（主线级）</div>';
                news.s_level.forEach(item => {
                    html += renderNewsItem(item);
                });
                html += '</div>';
            }
            
            if (news.a_level && news.a_level.length > 0) {
                html += '<div class="news-section">';
                html += '<div class="section-title">🟡 A级新闻（轮动级）</div>';
                news.a_level.forEach(item => {
                    html += renderNewsItem(item);
                });
                html += '</div>';
            }
            
            if (news.douyin && news.douyin.length > 0) {
                html += '<div class="news-section">';
                html += '<div class="section-title">📱 抖音相关</div>';
                news.douyin.forEach(item => {
                    html += renderNewsItem(item);
                });
                html += '</div>';
            }
            
            document.getElementById('newsContainer').innerHTML = html;
        }
        
        function renderNewsItem(item) {
            let etfHtml = '';
            if (item.etfs && item.etfs.length > 0) {
                etfHtml = '<div class="meta-item"><span class="meta-label">📈 映射ETF</span><div class="etf-list">';
                item.etfs.forEach(etf => {
                    const sentiment = etf.sentiment === '利好' ? 'sentiment-good' : 'sentiment-bad';
                    etfHtml += `<span class="etf-tag"><span class="${sentiment}">${etf.sentiment}</span> ${etf.name}</span>`;
                });
                etfHtml += '</div></div>';
            }
            
            let stockHtml = '';
            if (item.stocks && item.stocks.length > 0) {
                stockHtml = '<div class="meta-item"><span class="meta-label">✨ 映射个股</span><div class="stock-list">';
                item.stocks.forEach(stock => {
                    stockHtml += `<span class="stock-tag">${stock}</span>`;
                });
                stockHtml += '</div></div>';
            }
            
            return `
                <div class="news-item">
                    <div class="news-title">${item.emoji} ${item.title}</div>
                    <div class="news-summary">${item.summary}</div>
                    <div class="news-meta">
                        <div class="meta-item">
                            <span class="meta-label">⏱️ 影响时长</span>
                            <span class="meta-value">${item.duration}</span>
                        </div>
                        ${etfHtml}
                        ${stockHtml}
                        <div class="meta-item">
                            <span class="meta-label">💡 资金信号</span>
                            <span class="meta-value">${item.signal}</span>
                        </div>
                    </div>
                </div>
            `;
        }
        
        // 初始化
        initTimeline();
        updateButtons();
        renderNews();
    </script>
</body>
</html>
'''

# 保存 HTML 文件
with open("index.html", 'w', encoding='utf-8') as f:
    f.write(html)

print("[OK] Generated index.html")
print(f"[OK] Total size: {len(html) + len(js_data)} bytes")
print()
print("Files created:")
print("  - index.html (main page)")
print("  - news-data.js (news data)")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经新闻网站服务器
支持日期切换、历史新闻查看、数据持久化
"""

from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

app = Flask(__name__)

# 配置
NEWS_DATA_DIR = Path("news_data")
NEWS_DATA_DIR.mkdir(exist_ok=True)

def get_news_file(date_str=None):
    """获取指定日期的新闻文件路径"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    return NEWS_DATA_DIR / f"news_{date_str}.json"

def load_news(date_str=None):
    """加载指定日期的新闻数据"""
    news_file = get_news_file(date_str)
    if news_file.exists():
        with open(news_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "date": date_str or datetime.now().strftime("%Y-%m-%d"),
        "market_tone": "暂无数据",
        "s_level": [],
        "a_level": [],
        "douyin": []
    }

def save_news(news_data, date_str=None):
    """保存新闻数据"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    news_file = get_news_file(date_str)
    with open(news_file, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)

def get_available_dates():
    """获取所有可用的新闻日期"""
    dates = []
    for file in sorted(NEWS_DATA_DIR.glob("news_*.json"), reverse=True):
        date_str = file.stem.replace("news_", "")
        dates.append(date_str)
    return dates

@app.route('/')
def index():
    """主页 - 显示今天的新闻"""
    today = datetime.now().strftime("%Y-%m-%d")
    news_data = load_news(today)
    available_dates = get_available_dates()
    
    return render_template('index.html', 
                         news_data=news_data,
                         available_dates=available_dates,
                         current_date=today)

@app.route('/api/news/<date_str>')
def get_news(date_str):
    """API: 获取指定日期的新闻"""
    news_data = load_news(date_str)
    return jsonify(news_data)

@app.route('/api/dates')
def get_dates():
    """API: 获取所有可用日期"""
    dates = get_available_dates()
    return jsonify({"dates": dates})

@app.route('/api/news', methods=['POST'])
def save_news_api():
    """API: 保存新闻数据"""
    data = request.json
    date_str = data.get('date', datetime.now().strftime("%Y-%m-%d"))
    
    news_data = {
        "date": date_str,
        "market_tone": data.get('market_tone', ''),
        "s_level": data.get('s_level', []),
        "a_level": data.get('a_level', []),
        "douyin": data.get('douyin', [])
    }
    
    save_news(news_data, date_str)
    return jsonify({"status": "success", "date": date_str})

@app.route('/api/news/<date_str>', methods=['DELETE'])
def delete_news(date_str):
    """API: 删除指定日期的新闻"""
    news_file = get_news_file(date_str)
    if news_file.exists():
        news_file.unlink()
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "File not found"}), 404

if __name__ == '__main__':
    # 开发模式
    app.run(debug=True, host='0.0.0.0', port=5000)

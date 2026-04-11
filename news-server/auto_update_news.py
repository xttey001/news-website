#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动财经新闻更新系统
每天自动抓取新闻、生成网站、推送到 GitHub
"""

import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# 配置
NEWS_DIR = Path(__file__).parent / "news_data"
GITHUB_DEPLOY_DIR = Path(__file__).parent / "github-pages-deploy"

def get_today_news():
    """
    获取今天的新闻数据
    这里可以集成真实的新闻 API 或爬虫
    """
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 示例：返回今天的新闻模板
    news_template = {
        "date": today,
        "market_tone": "A股震荡调整，市场情绪谨慎",
        "s_level": [],
        "a_level": [],
        "douyin": []
    }
    
    return news_template

def save_news(news_data):
    """保存新闻数据到 JSON 文件"""
    date = news_data["date"]
    filepath = NEWS_DIR / f"news_{date}.json"
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Saved news for {date}")
    return filepath

def generate_website():
    """生成静态网站"""
    result = subprocess.run(
        ["python", "generate_static_with_history.py"],
        cwd=Path(__file__).parent,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("[OK] Generated website")
        return True
    else:
        print(f"[ERROR] Failed to generate website: {result.stderr}")
        return False

def push_to_github():
    """推送到 GitHub"""
    os.chdir(GITHUB_DEPLOY_DIR)
    
    # 检查是否有更改
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    
    if not result.stdout.strip():
        print("[*] No changes to commit")
        return True
    
    # 提交并推送
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(
            ["git", "commit", "-m", f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"],
            check=True
        )
        subprocess.run(["git", "push"], check=True)
        print("[OK] Pushed to GitHub")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Git operation failed: {e}")
        return False

def auto_update():
    """自动更新流程"""
    print("=" * 60)
    print("自动财经新闻更新系统")
    print("=" * 60)
    print()
    
    # 1. 获取新闻
    print("[*] Fetching news...")
    news = get_today_news()
    
    # 2. 保存新闻
    print("[*] Saving news...")
    save_news(news)
    
    # 3. 生成网站
    print("[*] Generating website...")
    if not generate_website():
        print("[ERROR] Failed to generate website")
        return False
    
    # 4. 推送到 GitHub
    print("[*] Pushing to GitHub...")
    if not push_to_github():
        print("[ERROR] Failed to push to GitHub")
        return False
    
    print()
    print("=" * 60)
    print("✅ 自动更新完成！")
    print("=" * 60)
    print()
    print(f"网站地址：https://xttey001.github.io/news-website/")
    print(f"更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return True

if __name__ == "__main__":
    auto_update()

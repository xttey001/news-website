"""
每日自动更新新闻并推送到 GitHub Pages
"""
import json
import os
import subprocess
from datetime import datetime

def add_today_news():
    """添加今天的新闻到历史记录"""
    
    # 读取今天的新闻
    today = datetime.now().strftime("%Y-%m-%d")
    news_file = f"news_data/news_{today}.json"
    
    if not os.path.exists(news_file):
        print(f"[ERROR] News file not found: {news_file}")
        return False
    
    with open(news_file, 'r', encoding='utf-8') as f:
        today_news = json.load(f)
    
    # 读取现有的历史数据
    history_file = "news_history.json"
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = {}
    
    # 添加今天的新闻
    history[today] = today_news
    
    # 只保留最近 30 天的新闻
    dates = sorted(history.keys(), reverse=True)[:30]
    history = {date: history[date] for date in dates}
    
    # 保存历史数据
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Added today's news to history")
    print(f"[OK] Total dates in history: {len(history)}")
    
    return True

def regenerate_website():
    """重新生成网站"""
    print("[*] Regenerating website...")
    result = subprocess.run(["python", "generate_static_with_history.py"], 
                          capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"[ERROR] {result.stderr}")
        return False
    return True

def push_to_github():
    """推送到 GitHub — 只更新 news-data.js，不碰 index.html"""
    print("[*] Pushing to GitHub...")
    
    os.chdir("github-pages-deploy")
    
    # 只复制数据文件，index.html 样式固定不动
    import shutil
    shutil.copy("../news-data.js", "news-data.js")
    
    # Git 操作
    subprocess.run(["git", "add", "news-data.js"], capture_output=True)
    subprocess.run(["git", "commit", "-m", f"Update news-data - {datetime.now().strftime('%Y-%m-%d %H:%M')}"], 
                  capture_output=True)
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    
    os.chdir("..")
    
    if result.returncode == 0:
        print("[OK] Pushed to GitHub successfully")
        return True
    else:
        print(f"[ERROR] Push failed: {result.stderr}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("Daily News Update & GitHub Push")
    print("="*60 + "\n")
    
    # 1. 添加今天的新闻
    if not add_today_news():
        exit(1)
    
    # 2. 重新生成网站
    if not regenerate_website():
        exit(1)
    
    # 3. 推送到 GitHub
    if not push_to_github():
        exit(1)
    
    print("\n" + "="*60)
    print("Update completed successfully!")
    print("="*60)
    print(f"\nYour website: https://xttey001.github.io/news-website/")

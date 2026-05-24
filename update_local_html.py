# -*- coding: utf-8 -*-
"""
更新本地版本脚本 - 新版
将 index.html 和 news-data/ 目录下的数据合并为 local_news.html
"""

import json
import os

# 路径配置
INDEX_PATH = r'd:\.qclaw\workspace\index.html'
DATA_DIR = r'd:\.qclaw\workspace\news-data'
INDEX_JSON_PATH = r'd:\.qclaw\workspace\news-data-index.json'
OUTPUT_PATH = r'd:\.qclaw\workspace\local_news.html'

def load_all_news_data():
    """加载所有新闻数据"""
    # 读取索引
    with open(INDEX_JSON_PATH, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    available_dates = index['availableDates']
    news_data = {}
    
    for date in available_dates:
        file_path = os.path.join(DATA_DIR, f'{date}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                news_data[date] = json.load(f)
            print(f"[OK] 已加载: {date}.json")
        else:
            print(f"[WARN] 文件不存在: {file_path}")
    
    return available_dates, news_data

def create_local_version():
    """创建本地版本"""
    print("="*60)
    print("[创建本地版本 - 新版]")
    print("="*60)
    
    # 读取 index.html
    try:
        with open(INDEX_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"[OK] 已读取: {INDEX_PATH}")
    except Exception as e:
        print(f"[ERROR] 读取失败: {e}")
        return False
    
    # 加载所有新闻数据
    available_dates, news_data = load_all_news_data()
    print(f"[OK] 已加载 {len(news_data)} 个日期的新闻数据")
    
    # 创建数据脚本
    news_data_js = f"""
// 内嵌新闻数据（本地版）
const newsData = {json.dumps(news_data, ensure_ascii=False, indent=2)};

const availableDates = {json.dumps(available_dates, ensure_ascii=False)};

// 模拟 NewsDataLoader
const NewsDataLoader = {{
    cache: newsData,
    index: {{ availableDates: availableDates }},
    
    async loadIndex() {{
        return this.index;
    }},
    
    async loadDate(date) {{
        return this.cache[date] || null;
    }},
    
    async getAvailableDates() {{
        return availableDates;
    }},
    
    async getLatestDate() {{
        return availableDates[0];
    }}
}};
"""
    
    # 替换外部脚本引用
    # 1. 移除 news-data-loader.js 引用
    html_content = html_content.replace(
        '<script src="news-data-loader.js"></script>',
        f'<script>\n{news_data_js}\n</script>'
    )
    
    # 2. 修改页面标题
    html_content = html_content.replace(
        '<title>悟空财经分析</title>',
        '<title>悟空财经分析 - 本地版</title>'
    )
    
    # 3. 添加本地版标记
    local_badge = '''<div style="display:inline-block;margin-top:8px;padding:4px 10px;background:rgba(63,185,80,0.15);border:1px solid rgba(63,185,80,0.3);border-radius:6px;color:#3fb950;font-size:11px;">[本地版] 无需网络</div>'''
    
    if '<div class="local-badge">' not in html_content:
        html_content = html_content.replace(
            '<div class="subtitle">不盲从主流解读，用逻辑和数据说话</div>',
            '<div class="subtitle">不盲从主流解读，用逻辑和数据说话</div>\n            ' + local_badge
        )
    
    # 写入输出文件
    try:
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"[OK] 已保存: {OUTPUT_PATH}")
    except Exception as e:
        print(f"[ERROR] 保存失败: {e}")
        return False
    
    print("="*60)
    print("本地版本创建成功!")
    print(f"包含日期: {', '.join(available_dates[:5])}...")
    print(f"文件位置: {OUTPUT_PATH}")
    print("提示: 双击文件即可在浏览器中打开，无需网络")
    print("="*60)
    return True

if __name__ == '__main__':
    create_local_version()

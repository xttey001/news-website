# -*- coding: utf-8 -*-
"""
更新本地HTML页面脚本
每次运行时会将 news-data.js 中的数据嵌入到 local_news.html 中
"""
import re
from datetime import datetime

# 路径配置
LOCAL_HTML_PATH = r'C:\Users\asus\.qclaw\workspace\local_news.html'
NEWS_DATA_PATH = r'C:\Users\asus\.qclaw\workspace\news-data.js'

def extract_data_as_string(js_content):
    """从news-data.js中提取数据部分作为字符串"""
    # 提取 newsData 对象
    news_data_match = re.search(
        r'const\s+newsData\s*=\s*({[\s\S]*?})\s*;\s*const\s+availableDates',
        js_content
    )
    
    # 提取 availableDates 数组
    dates_match = re.search(
        r'const\s+availableDates\s*=\s*(\[[^\]]*\])',
        js_content
    )
    
    if news_data_match and dates_match:
        return news_data_match.group(1), dates_match.group(1)
    
    return None, None

def update_local_html():
    """更新本地HTML文件"""
    print("="*60)
    print("🔄 更新本地HTML页面")
    print("="*60)
    
    # 读取news-data.js
    try:
        with open(NEWS_DATA_PATH, 'r', encoding='utf-8') as f:
            js_content = f.read()
        print(f"✅ 已读取: {NEWS_DATA_PATH}")
    except Exception as e:
        print(f"❌ 读取 news-data.js 失败: {e}")
        return False
    
    # 提取数据字符串
    news_data_str, dates_str = extract_data_as_string(js_content)
    
    if not news_data_str or not dates_str:
        print("❌ 无法提取数据")
        return False
    
    # 提取日期数量信息
    dates_count = len(re.findall(r'"\d{4}-\d{2}-\d{2}"', dates_str))
    print(f"✅ 提取到 {dates_count} 天数据")
    
    # 读取local_news.html
    try:
        with open(LOCAL_HTML_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"✅ 已读取: {LOCAL_HTML_PATH}")
    except Exception as e:
        print(f"❌ 读取 local_news.html 失败: {e}")
        return False
    
    # 替换占位符
    # 替换 newsData
    html_content = html_content.replace(
        'const newsData = {/*DATA_PLACEHOLDER*/};',
        f'const newsData = {news_data_str};'
    )
    
    # 替换 availableDates
    html_content = html_content.replace(
        'const availableDates = [/*DATES_PLACEHOLDER*/];',
        f'const availableDates = {dates_str};'
    )
    
    # 写入文件
    try:
        with open(LOCAL_HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ 已更新: {LOCAL_HTML_PATH}")
    except Exception as e:
        print(f"❌ 写入失败: {e}")
        return False
    
    print("="*60)
    print(f"🎉 本地HTML页面更新成功!")
    print(f"📅 数据日期: 最近 {dates_count} 天")
    print(f"💡 提示: 双击 local_news.html 即可在浏览器中打开")
    print("="*60)
    return True

if __name__ == '__main__':
    update_local_html()

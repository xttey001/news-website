#!/usr/bin/env python3
"""
财经新闻抓取与分类系统
按照 S/A/B 三级分类，只输出 S+A 级
"""

import requests
from datetime import datetime
import re
import json

# 新闻源配置
NEWS_SOURCES = {
    "网易财经": "https://money.163.com/special/00251U62/news_data.js?callback=data_callback",
    "36氪快讯": "https://36kr.com/newsflashes",
    "财经热点": "https://tophub.today/n/2me3N3xdwj",
    "抖音财经榜": "https://tophub.today/n/2me3N3xdwj"
}

# ETF映射表
ETF_MAPPING = {
    "创新药": ("创新药ETF", "生物医药ETF"),
    "AI": ("AIETF", "半导体ETF"),
    "半导体": ("半导体ETF", "芯片ETF"),
    "存储": ("存储ETF", "半导体ETF"),
    "黄金": ("黄金ETF",),
    "能源": ("油气ETF", "能源ETF"),
    "新能源车": ("新能源车ETF",),
    "自动驾驶": ("自动驾驶ETF",),
    "券商": ("券商ETF",),
    "军工": ("军工ETF",),
    "房地产": ("房地产ETF",),
    "消费": ("消费ETF",),
    "医药": ("医药ETF", "医疗ETF"),
    "科技": ("科技ETF", "纳斯达克ETF"),
    "互联网": ("互联网ETF",),
}

# 个股映射
STOCK_MAPPING = {
    "创新药": ("恒瑞医药", "药明康德", "百济神州"),
    "AI": ("百度", "科大讯飞", "商汤"),
    "半导体": ("中芯国际", "韦尔股份", "北方华创"),
    "存储": ("兆易创新", "北京君正"),
    "黄金": ("中金黄金", "山东黄金", "紫金矿业"),
    "新能源车": ("比亚迪", "小鹏汽车", "理想汽车"),
    "自动驾驶": ("百度", "小马智行"),
    "券商": ("中信证券", "海通证券", "中金公司"),
    "军工": ("中航沈飞", "航发动力", "中国船舶"),
    "原油": ("中国石油", "中国石化"),
}

def classify_news(title, content=""):
    """
    S/A/B 三级分类
    S级：能影响ETF、持续1周以上、能改变资金方向
    A级：阶段性叙事，主线内部资金再分配
    B级：个股/情绪噪音，不改变资金结构
    """
    text = (title + content).lower()
    
    # S级关键词
    s_keywords = [
        "政策", "降息", "加息", "央行", "监管", "制裁", "战争",
        "突破", "拐点", "革命", "变革", "大规模", "历史性",
        "ETF", "板块", "行业", "牛市", "熊市", "资金"
    ]
    
    # A级关键词
    a_keywords = [
        "上涨", "下跌", "利好", "利空", "突破", "反弹",
        "业绩", "合同", "合作", "发布", "推出",
        "首次", "最大", "新高", "新低"
    ]
    
    s_score = sum(1 for k in s_keywords if k in text)
    a_score = sum(1 for k in a_keywords if k in text)
    
    if s_score >= 2:
        return "S"
    elif a_score >= 1:
        return "A"
    else:
        return "B"

def extract_etf_stocks(text):
    """提取相关的ETF和个股"""
    etfs = set()
    stocks = set()
    
    for keyword, etf_list in ETF_MAPPING.items():
        if keyword in text:
            etfs.update(etf_list)
    
    for keyword, stock_list in STOCK_MAPPING.items():
        if keyword in text:
            stocks.update(stock_list)
    
    return list(etfs), list(stocks)

def fetch_163_news():
    """抓取网易财经"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(
            "https://money.163.com/special/00251U62/news_data.js?callback=data_callback",
            headers=headers,
            timeout=10
        )
        text = resp.text
        # 解析JSONP
        match = re.search(r'data_callback\((.*)\)', text, re.DOTALL)
        if match:
            data = json.loads(match.group(1))
            news = []
            for item in data[:20]:
                news.append({
                    "title": item.get("title", ""),
                    "url": item.get("linkurl", ""),
                    "time": item.get("datetime", ""),
                    "source": "网易财经"
                })
            return news
    except Exception as e:
        print(f"网易财经抓取失败: {e}")
    return []

def fetch_36kr_news():
    """抓取36氪快讯"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(
            "https://36kr.com/newsflashes",
            headers=headers,
            timeout=10
        )
        # 简单解析
        titles = re.findall(r'<a[^>]+class="item-title"[^>]*>([^<]+)</a>', resp.text)
        news = []
        for t in titles[:10]:
            news.append({
                "title": t.strip(),
                "url": "https://36kr.com/newsflashes",
                "time": datetime.now().strftime("%H:%M"),
                "source": "36氪"
            })
        return news
    except Exception as e:
        print(f"36氪抓取失败: {e}")
    return []

def process_news():
    """处理所有新闻源"""
    all_news = []
    
    # 抓取各源
    all_news.extend(fetch_163_news())
    all_news.extend(fetch_36kr_news())
    
    # 分类
    classified = {"S": [], "A": []}
    seen_titles = set()
    
    for item in all_news:
        title = item["title"]
        if title in seen_titles:
            continue
        seen_titles.add(title)
        
        level = classify_news(title)
        if level in ["S", "A"]:
            etfs, stocks = extract_etf_stocks(title)
            item["level"] = level
            item["etfs"] = etfs
            item["stocks"] = stocks
            classified[level].append(item)
    
    return classified

def format_news(classified):
    """格式化输出"""
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M")
    output = f"📊 {now} 财经新闻\n\n"
    
    # S级
    if classified["S"]:
        output += "🟥 S级（主线级 | L2）\n\n"
        for i, item in enumerate(classified["S"][:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   • ETF：{', '.join(item['etfs'][:3])}\n"
            if item['stocks']:
                output += f"   • 个股：{', '.join(item['stocks'][:3])}\n"
            output += "\n"
    
    # A级
    if classified["A"]:
        output += "🟧 A级（轮动级 | L3）\n\n"
        for i, item in enumerate(classified["A"][:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   • ETF：{', '.join(item['etfs'][:2])}\n"
            output += "\n"
    
    if not classified["S"] and not classified["A"]:
        output += "暂无重要新闻更新\n"
    
    return output

if __name__ == "__main__":
    print("抓取财经新闻...")
    classified = process_news()
    output = format_news(classified)
    print(output)

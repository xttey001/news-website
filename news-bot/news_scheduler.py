#!/usr/bin/env python3
"""
财经新闻推送系统 - OpenClaw Cron 任务
每天 09:00、13:00、22:00 自动推送 S/A 级新闻到微信
"""

import requests
import re
import json
from datetime import datetime

# ============ 配置区 ============
USER_ID = "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"
PUSH_TIME = datetime.now().strftime("%Y年%m月%d日 %H:%M")

# ETF映射表
ETF_MAPPING = {
    "创新药": ("创新药ETF", "生物医药ETF"),
    "AI": ("AIETF", "半导体ETF"),
    "半导体": ("半导体ETF", "芯片ETF"),
    "存储": ("存储ETF", "半导体ETF"),
    "黄金": ("黄金ETF",),
    "原油": ("油气ETF", "能源ETF"),
    "新能源车": ("新能源车ETF",),
    "自动驾驶": ("自动驾驶ETF",),
    "券商": ("券商ETF",),
    "军工": ("军工ETF",),
    "医药": ("医药ETF", "医疗ETF"),
    "科技": ("科技ETF", "纳斯达克ETF"),
    "互联网": ("互联网ETF",),
    "房地产": ("房地产ETF",),
    "消费": ("消费ETF",),
    "光伏": ("光伏ETF",),
    "风电": ("风电ETF",),
}

# 个股映射
STOCK_MAPPING = {
    "创新药": ("恒瑞医药", "药明康德", "百济神州"),
    "AI": ("百度", "科大讯飞", "商汤"),
    "半导体": ("中芯国际", "韦尔股份", "北方华创"),
    "存储": ("兆易创新", "北京君正"),
    "黄金": ("中金黄金", "山东黄金", "紫金矿业"),
    "原油": ("中国石油", "中国石化"),
    "新能源车": ("比亚迪", "小鹏汽车", "理想汽车"),
    "自动驾驶": ("百度", "小马智行"),
    "券商": ("中信证券", "海通证券", "中金公司"),
    "军工": ("中航沈飞", "航发动力", "中国船舶"),
}

# ============ 新闻源 ============
def fetch_news():
    """抓取并分类新闻"""
    all_news = []
    
    # 1. 网易财经
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resp = requests.get(
            "https://money.163.com/special/00251U62/news_data.js?callback=data_callback",
            headers=headers, timeout=10
        )
        match = re.search(r'data_callback\((.*)\)', resp.text, re.DOTALL)
        if match:
            data = json.loads(match.group(1))
            for item in data[:15]:
                all_news.append({
                    "title": item.get("title", ""),
                    "url": item.get("linkurl", ""),
                    "time": item.get("datetime", ""),
                    "source": "网易财经"
                })
    except Exception as e:
        print(f"网易财经失败: {e}")
    
    # 2. 36氪快讯
    try:
        resp = requests.get("https://36kr.com/newsflashes", headers=headers, timeout=10)
        titles = re.findall(r'<a[^>]+class="[^"]*item-title[^"]*"[^>]*>([^<]+)</a>', resp.text)
        for t in titles[:8]:
            all_news.append({
                "title": t.strip(),
                "url": "https://36kr.com/newsflashes",
                "time": datetime.now().strftime("%H:%M"),
                "source": "36氪"
            })
    except Exception as e:
        print(f"36氪失败: {e}")
    
    return all_news

def classify(title, content=""):
    """S/A/B 三级分类"""
    text = (title + content).lower()
    
    # S级：政策、央行、重大突破、战争、制裁
    s_kw = ["政策", "央行", "降息", "加息", "监管", "制裁", "战争", "突破", "拐点", 
            "重大", "历史", "板块", "ETF", "牛市", "熊市", "资金"]
    # A级：业绩、涨跌、合同、发布
    a_kw = ["上涨", "下跌", "利好", "利空", "业绩", "合同", "发布", "推出",
            "新高", "新低", "首次", "最大", "融资", "合作"]
    
    s_cnt = sum(1 for k in s_kw if k in text)
    a_cnt = sum(1 for k in a_kw if k in text)
    
    if s_cnt >= 2:
        return "S"
    elif a_cnt >= 1:
        return "A"
    return "B"

def get_etf_stocks(text):
    """提取ETF和个股"""
    etfs, stocks = [], []
    for kw, e in ETF_MAPPING.items():
        if kw in text:
            etfs.extend(e)
    for kw, s in STOCK_MAPPING.items():
        if kw in text:
            stocks.extend(s)
    return list(set(etfs))[:3], list(set(stocks))[:3]

def process_news():
    """处理新闻，返回分类结果"""
    news = fetch_news()
    s_list, a_list = [], []
    seen = set()
    
    for item in news:
        title = item["title"]
        if title in seen or len(title) < 8:
            continue
        seen.add(title)
        
        level = classify(title)
        if level in ["S", "A"]:
            etfs, stocks = get_etf_stocks(title)
            item["level"] = level
            item["etfs"] = etfs
            item["stocks"] = stocks
            if level == "S":
                s_list.append(item)
            else:
                a_list.append(item)
    
    return s_list, a_list

def format_push():
    """格式化推送内容"""
    s_list, a_list = process_news()
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M")
    
    output = f"📊 {now} 财经新闻\n"
    output += "━━━━━━━━━━━━━━━━\n\n"
    
    if s_list:
        output += "🟥 S级（主线级 | L2）\n\n"
        for i, item in enumerate(s_list[:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   📈 ETF：{' / '.join(item['etfs'])}\n"
            if item['stocks']:
                output += f"   🏢 个股：{' / '.join(item['stocks'])}\n"
            output += "\n"
    
    if a_list:
        output += "🟧 A级（轮动级 | L3）\n\n"
        for i, item in enumerate(a_list[:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   📈 ETF：{' / '.join(item['etfs'][:2])}\n"
            output += "\n"
    
    if not s_list and not a_list:
        output += "暂无重要新闻更新\n\n"
        output += "📍 来源：网易财经 / 36氪\n"
    
    output += "\n━━━━━━━━━━━━━━━━\n"
    output += "🤖 自动推送 | S/A分级"
    
    return output

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 40)
    print("[NEWS] Financial News Bot")
    print(f"[TIME] {PUSH_TIME}")
    print("=" * 40)
    result = format_push()
    print(result)
    
    # 保存结果供OpenClaw推送
    with open("C:/Users/asus/.qclaw/workspace/news-bot/latest_news.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("\n[OK] News saved, ready to push...")

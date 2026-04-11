#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经新闻抓取系统 - 支持多源
按照 S/A/B 三级分类，只推送 S+A 级
"""

import requests
import re
import json
from datetime import datetime

# ============ 配置 ============
USER_ID = "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"

# ETF 映射表
ETF_MAPPING = {
    "创新药": ("创新药ETF", "生物医药ETF"),
    "AI": ("AIETF", "半导体ETF"),
    "大模型": ("AIETF", "科技ETF"),
    "半导体": ("半导体ETF", "芯片ETF"),
    "存储": ("存储ETF", "半导体ETF"),
    "黄金": ("黄金ETF",),
    "原油": ("油气ETF", "能源ETF"),
    "石油": ("油气ETF",),
    "新能源车": ("新能源车ETF",),
    "电动车": ("新能源车ETF",),
    "自动驾驶": ("自动驾驶ETF",),
    "智能驾驶": ("自动驾驶ETF",),
    "券商": ("券商ETF",),
    "军工": ("军工ETF",),
    "医药": ("医药ETF", "医疗ETF"),
    "科技": ("科技ETF", "纳斯达克ETF"),
    "互联网": ("互联网ETF",),
    "房地产": ("房地产ETF",),
    "消费": ("消费ETF",),
    "光伏": ("光伏ETF",),
    "风电": ("风电ETF",),
    "芯片": ("芯片ETF", "半导体ETF"),
    "算力": ("算力ETF", "AIETF"),
}

# 个股映射
STOCK_MAPPING = {
    "创新药": ("恒瑞医药", "药明康德", "百济神州"),
    "AI": ("百度", "科大讯飞", "商汤"),
    "大模型": ("百度", "阿里", "腾讯"),
    "半导体": ("中芯国际", "韦尔股份", "北方华创"),
    "存储": ("兆易创新", "北京君正"),
    "黄金": ("中金黄金", "山东黄金", "紫金矿业"),
    "原油": ("中国石油", "中国石化"),
    "新能源车": ("比亚迪", "小鹏汽车", "理想汽车"),
    "自动驾驶": ("百度", "小马智行"),
    "券商": ("中信证券", "海通证券", "中金公司"),
    "军工": ("中航沈飞", "航发动力", "中国船舶"),
    "苹果": ("立讯精密", "歌尔股份", "蓝思科技"),
}

# ============ 新闻源 ============
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_163_news():
    """网易财经"""
    news = []
    try:
        resp = requests.get(
            "https://money.163.com/special/00251U62/news_data.js?callback=data_callback",
            headers=HEADERS, timeout=10
        )
        match = re.search(r'data_callback\((.*)\)', resp.text, re.DOTALL)
        if match:
            data = json.loads(match.group(1))
            for item in data[:20]:
                news.append({
                    "title": item.get("title", ""),
                    "url": item.get("linkurl", ""),
                    "time": item.get("datetime", ""),
                    "source": "网易财经"
                })
    except Exception as e:
        print(f"  [-] 网易财经失败: {e}")
    return news

def fetch_36kr_news():
    """36氪快讯"""
    news = []
    try:
        resp = requests.get("https://36kr.com/newsflashes", headers=HEADERS, timeout=10)
        titles = re.findall(r'<a[^>]+class="[^"]*item-title[^"]*"[^>]*>([^<]+)</a>', resp.text)
        for t in titles[:10]:
            news.append({
                "title": t.strip(),
                "url": "https://36kr.com/newsflashes",
                "time": datetime.now().strftime("%H:%M"),
                "source": "36氪"
            })
    except Exception as e:
        print(f"  [-] 36氪失败: {e}")
    return news

def fetch_sina_news():
    """新浪财经"""
    news = []
    try:
        resp = requests.get(
            "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2516&num=20&versionNumber=1.2.4&page=1",
            headers=HEADERS, timeout=10
        )
        data = resp.json()
        for item in data.get("result", {}).get("data", [])[:15]:
            news.append({
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "time": item.get("ctime", ""),
                "source": "新浪财经"
            })
    except Exception as e:
        print(f"  [-] 新浪财经失败: {e}")
    return news

def fetch_eastmoney():
    """东方财富"""
    news = []
    try:
        resp = requests.get(
            "https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&fields=f12,f14&secids=90.BK0715,90.BK0101,90.BK0428,90.BK0728",
            headers=HEADERS, timeout=10
        )
        # 解析板块涨跌
        data = resp.json()
        for item in data.get("data", {}).get("diff", [])[:5]:
            name = item.get("f14", "")
            change = item.get("f3", 0)
            if change > 2:
                news.append({
                    "title": f"{name}板块涨超{change}%",
                    "url": "https://www.eastmoney.com",
                    "time": datetime.now().strftime("%H:%M"),
                    "source": "东方财富"
                })
    except Exception as e:
        print(f"  [-] 东方财富失败: {e}")
    return news

def fetch_all_news():
    """抓取所有新闻源"""
    print("[*] 开始抓取新闻...")
    all_news = []
    all_news.extend(fetch_163_news())
    print(f"  [+] 网易财经: {len(all_news)} 条")
    all_news.extend(fetch_36kr_news())
    print(f"  [+] 36氪: {len(all_news)} 条")
    all_news.extend(fetch_sina_news())
    print(f"  [+] 新浪: {len(all_news)} 条")
    all_news.extend(fetch_eastmoney())
    print(f"  [+] 东方财富: {len(all_news)} 条")
    print(f"[*] 共抓取 {len(all_news)} 条新闻")
    return all_news

# ============ 分类逻辑 ============
def classify(title, content=""):
    """
    S/A/B 三级分类
    S级：能影响ETF、持续1周以上、能改变资金方向
    A级：阶段性叙事，主线内部资金再分配
    B级：个股/情绪噪音，不改变资金结构
    """
    text = (title + content)
    
    # S级关键词
    s_kw = [
        "政策", "央行", "降息", "加息", "监管", "制裁", "战争",
        "突破", "拐点", "变革", "大规模", "历史性",
        "ETF", "板块", "行业", "牛市", "熊市", "资金",
        "禁止", "要求", "发布", "规定", "调整"
    ]
    
    # A级关键词
    a_kw = [
        "上涨", "下跌", "利好", "利空", "业绩", "合同", "签约",
        "发布", "推出", "新高", "新低", "首次", "最大",
        "融资", "合作", "战略", "投资", "收购"
    ]
    
    s_cnt = sum(1 for k in s_kw if k in text)
    a_cnt = sum(1 for k in a_kw if k in text)
    
    if s_cnt >= 2:
        return "S"
    elif a_cnt >= 1:
        return "A"
    return "B"

def get_etf_stocks(text):
    """提取ETF和个股"""
    etfs, stocks = set(), set()
    for kw, e in ETF_MAPPING.items():
        if kw in text:
            etfs.update(e)
    for kw, s in STOCK_MAPPING.items():
        if kw in text:
            stocks.update(s)
    return list(etfs)[:3], list(stocks)[:3]

# ============ 处理和输出 ============
def process_news(news_list):
    """处理新闻，返回分类结果"""
    s_list, a_list = [], []
    seen = set()
    
    for item in news_list:
        title = item.get("title", "").strip()
        if not title or title in seen or len(title) < 8:
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
    # 抓取
    all_news = fetch_all_news()
    s_list, a_list = process_news(all_news)
    
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M")
    
    output = f"📊 {now} 财经新闻\n"
    output += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    # S级
    if s_list:
        output += "🟥 S级（主线级 | L2）\n\n"
        for i, item in enumerate(s_list[:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   📈 ETF：{' / '.join(item['etfs'])}\n"
            if item['stocks']:
                output += f"   🏢 个股：{' / '.join(item['stocks'])}\n"
            output += "\n"
    
    # A级
    if a_list:
        output += "🟧 A级（轮动级 | L3）\n\n"
        for i, item in enumerate(a_list[:5], 1):
            output += f"{i}️⃣ {item['title']}\n"
            if item['etfs']:
                output += f"   📈 ETF：{' / '.join(item['etfs'][:2])}\n"
            output += "\n"
    
    if not s_list and not a_list:
        output += "暂无重要新闻更新\n\n"
        output += "📍 来源：网易财经 / 36氪 / 新浪 / 东方财富\n"
    
    output += "\n━━━━━━━━━━━━━━━━━━━━\n"
    output += "🤖 自动推送 | S/A分级"
    
    return output

# ============ 主程序 ============
if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 50)
    print("   财经新闻推送系统 v2.0")
    print(f"   时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    result = format_push()
    print("\n" + result)
    
    # 保存
    save_path = r"C:\Users\asus\.qclaw\workspace\news-bot\latest_news.txt"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    print(f"\n[OK] 已保存到: {save_path}")

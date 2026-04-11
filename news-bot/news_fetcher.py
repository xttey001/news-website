# -*- coding: utf-8 -*-
"""
财经新闻抓取器 v4.0 - 带利好/利空判断和要点摘要
"""
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import random
import json
import re

# 用户代理池
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
]

def get_headers():
    """随机获取请求头"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

def fetch_with_retry(url, max_retries=3):
    """带重试的请求"""
    for i in range(max_retries):
        try:
            time.sleep(random.uniform(1, 3))
            response = requests.get(url, headers=get_headers(), timeout=10)
            response.encoding = 'utf-8'
            return response
        except Exception as e:
            if i < max_retries - 1:
                time.sleep(2)
            else:
                return None

def fetch_163_finance():
    """网易财经"""
    try:
        url = "https://money.163.com/"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        links = soup.select('a[href*="money.163.com"]')[:15]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 5:
                news_items.append({
                    'title': title,
                    'url': link.get('href', ''),
                    'source': '网易财经'
                })
        return news_items
    except:
        return []

def fetch_eastmoney():
    """东方财富"""
    try:
        url = "https://www.eastmoney.com/"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        links = soup.select('a[href*="eastmoney.com"]')[:15]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 5:
                news_items.append({
                    'title': title,
                    'url': link.get('href', ''),
                    'source': '东方财富'
                })
        return news_items
    except:
        return []

def fetch_sina_finance():
    """新浪财经"""
    try:
        url = "https://finance.sina.com.cn/"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        links = soup.select('a[href*="sina.com.cn"]')[:15]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 5:
                news_items.append({
                    'title': title,
                    'url': link.get('href', ''),
                    'source': '新浪财经'
                })
        return news_items
    except:
        return []

def fetch_36kr():
    """36氪"""
    try:
        url = "https://36kr.com/newsflashes"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        items = soup.select('.newsflash-item, .item-content')[:10]
        
        for item in items:
            title = item.get_text(strip=True)
            if title and len(title) > 5:
                news_items.append({
                    'title': title[:100],
                    'url': 'https://36kr.com/newsflashes',
                    'source': '36氪'
                })
        return news_items
    except:
        return []

def classify_news(title):
    """S/A/B 分级"""
    title_lower = title.lower()
    
    # S级关键词（主线级）
    s_keywords = ['政策', '央行', '美联储', '利率', '降息', '加息', '监管', '改革', 
                  '突破', '暴跌', '暴涨', '崩盘', '熔断', '战争', '制裁', '关税',
                  'ETF', '板块', '龙头', '拐点', '反转']
    
    # A级关键词（轮动级）
    a_keywords = ['签约', '合作', '收购', '并购', '融资', '上市', 'IPO', 
                  '业绩', '盈利', '亏损', '增长', '下降', '发布', '推出',
                  '创新', '研发', '投资', '扩张']
    
    for kw in s_keywords:
        if kw in title_lower:
            return 'S'
    
    for kw in a_keywords:
        if kw in title_lower:
            return 'A'
    
    return 'B'

def analyze_sentiment(title):
    """利好/利空判断"""
    title_lower = title.lower()
    
    # 利好关键词
    bullish = ['利好', '增长', '盈利', '上涨', '突破', '新高', '翻倍', '大赚',
               '订单', '中标', '签约', '合作', '获批', '授权', '增持', '回购',
               '降息', '宽松', '刺激', '扶持', '补贴', '减税', '降准',
               '创新高', '历史新高', '超预期', '爆发', '大增']
    
    # 利空关键词
    bearish = ['利空', '亏损', '下跌', '暴跌', '崩盘', '破位', '新低', '腰斩',
               '违约', '债务', '破产', '退市', '调查', '处罚', '罚款', '诉讼',
               '加息', '紧缩', '制裁', '关税', '打压', '监管', '叫停',
               '下降', '减少', '裁员', '关闭', '终止', '失败']
    
    # 中性/观望
    neutral = ['发布', '推出', '计划', '预计', '或', '可能', '拟', '将']
    
    bull_score = sum(1 for kw in bullish if kw in title_lower)
    bear_score = sum(1 for kw in bearish if kw in title_lower)
    
    if bull_score > bear_score:
        return '利好', '🟢'
    elif bear_score > bull_score:
        return '利空', '🔴'
    elif bull_score == bear_score and bull_score > 0:
        return '中性', '🟡'
    else:
        return '观望', '⚪'

def estimate_impact_duration(title):
    """估计影响时长（具体化）"""
    title_lower = title.lower()
    
    # 长期影响（1年以上）
    long_term = ['政策', '改革', '监管', '制度', '法律', '法规', '战略', 
                 '转型', '并购', '收购', '重组', 'IPO', '上市', '退市']
    
    # 中期影响（1-6个月）
    mid_term = ['业绩', '盈利', '订单', '签约', '合作', '发布', '推出',
                '研发', '创新', '投资', '扩张', '降息', '加息']
    
    # 短期影响（1个月内）
    short_term = ['暴涨', '暴跌', '涨停', '跌停', '异动', '利好', '利空',
                  '上涨', '下跌', '突破', '新高', '新低']
    
    # 即时影响（几天内）
    instant = ['今日', '明日', '本周', '盘中', '收盘', '开盘', '紧急']
    
    if any(kw in title_lower for kw in instant):
        return '1-3天', '⚡'
    elif any(kw in title_lower for kw in short_term):
        return '1-4周', '📅'
    elif any(kw in title_lower for kw in mid_term):
        return '1-6月', '📆'
    elif any(kw in title_lower for kw in long_term):
        return '1年以上', '🗓️'
    else:
        return '1-4周', '📅'

def extract_key_point(title):
    """提取一句话要点"""
    # 移除常见噪音词和垃圾文本
    noise_patterns = [
        r'\d+分钟前', r'\d+小时前', r'\d+天前',
        r'分享至', r'打开微信', r'扫一扫', r'点击屏幕', r'右上角', r'分享按钮',
        r'打开网页后', r'原文', r'""', r'“”'
    ]
    clean_title = title
    for pattern in noise_patterns:
        clean_title = re.sub(pattern, '', clean_title)
    
    clean_title = clean_title.strip()
    
    # 检测并移除重复内容（如 "xxx，xxx" 格式）
    # 按常见分隔符分割
    for sep in ['，', ',', '：', ':', '——']:
        if sep in clean_title:
            parts = [p.strip() for p in clean_title.split(sep) if p.strip()]
            if len(parts) >= 2:
                # 检查是否有重复
                first = parts[0]
                for p in parts[1:]:
                    # 如果后一部分包含前一部分的核心内容，只保留前一部分
                    if first in p or p in first:
                        clean_title = first
                        break
                break
    
    # 如果太长，智能截断
    if len(clean_title) > 50:
        for sep in ['。', '，', '：', ':', '|', '-', '——']:
            if sep in clean_title:
                parts = clean_title.split(sep)
                if len(parts[0]) > 10 and len(parts[0]) < len(clean_title):
                    clean_title = parts[0]
                    break
        else:
            clean_title = clean_title[:47] + '...'
    
    return clean_title.strip()

def map_targets(title):
    """映射ETF和个股"""
    # ETF映射
    etf_map = {
        # 科技
        'AI': ['AIETF', '科技ETF', '科创50ETF'],
        '人工智能': ['AIETF', '科技ETF', '科创50ETF'],
        '半导体': ['半导体ETF', '芯片ETF'],
        '芯片': ['芯片ETF', '半导体ETF'],
        '光刻机': ['半导体ETF', '芯片ETF'],
        '算力': ['AIETF', '云计算ETF'],
        '云计算': ['云计算ETF', '科技ETF'],
        '数据中心': ['大数据ETF', '云计算ETF'],
        
        # 新能源
        '新能源': ['新能源ETF', '光伏ETF'],
        '光伏': ['光伏ETF', '新能源ETF'],
        '锂电': ['锂电池ETF', '新能源车ETF'],
        '锂电池': ['锂电池ETF', '新能源车ETF'],
        '新能源车': ['新能源车ETF', '汽车ETF'],
        '电动车': ['新能源车ETF', '汽车ETF'],
        '储能': ['储能ETF', '新能源ETF'],
        '风电': ['风电ETF', '新能源ETF'],
        
        # 医药
        '创新药': ['创新药ETF', '生物医药ETF'],
        '医药': ['医药ETF', '生物医药ETF'],
        '生物': ['生物医药ETF', '医药ETF'],
        '疫苗': ['生物医药ETF', '医药ETF'],
        '医疗': ['医疗ETF', '医药ETF'],
        
        # 金融
        '券商': ['券商ETF', '证券ETF'],
        '证券': ['证券ETF', '券商ETF'],
        '银行': ['银行ETF', '金融ETF'],
        '保险': ['保险ETF', '金融ETF'],
        
        # 消费
        '消费': ['消费ETF', '消费50ETF'],
        '白酒': ['酒ETF', '消费ETF'],
        '酒': ['酒ETF', '消费ETF'],
        '食品': ['食品饮料ETF', '消费ETF'],
        
        # 资源
        '黄金': ['黄金ETF', '黄金股ETF'],
        '石油': ['油气ETF', '能源ETF'],
        '煤炭': ['煤炭ETF', '能源ETF'],
        '有色': ['有色金属ETF', '资源ETF'],
        '稀土': ['稀土ETF', '有色金属ETF'],
        '锂矿': ['有色金属ETF', '新能源ETF'],
        
        # 其他
        '军工': ['军工ETF', '国防军工ETF'],
        '房地产': ['房地产ETF', '地产ETF'],
        '地产': ['房地产ETF', '地产ETF'],
        '基建': ['基建ETF', '建材ETF'],
        '传媒': ['传媒ETF', '游戏ETF'],
        '游戏': ['游戏ETF', '传媒ETF'],
    }
    
    # 个股映射（重要龙头）
    stock_map = {
        # 科技龙头
        '华为': ['华为概念股'],
        '苹果': ['苹果产业链', '立讯精密', '歌尔股份'],
        '特斯拉': ['特斯拉产业链', '宁德时代'],
        '英伟达': ['英伟达概念股', 'AI算力'],
        'OpenAI': ['AI概念股', '算力'],
        '微软': ['AI概念股', '云计算'],
        '谷歌': ['AI概念股', '云计算'],
        
        # 新能源龙头
        '宁德时代': ['宁德时代', '锂电池龙头'],
        '比亚迪': ['比亚迪', '新能源车龙头'],
        
        # 消费龙头
        '茅台': ['贵州茅台', '白酒龙头'],
        '贵州茅台': ['贵州茅台', '白酒龙头'],
        '五粮液': ['五粮液', '白酒'],
        
        # 金融龙头
        '中信证券': ['中信证券', '券商龙头'],
        '东方财富': ['东方财富', '券商'],
        
        # 医药龙头
        '恒瑞医药': ['恒瑞医药', '创新药龙头'],
        '药明康德': ['药明康德', 'CRO龙头'],
    }
    
    etf_result = None
    stock_result = None
    
    for keyword, etfs in etf_map.items():
        if keyword in title:
            etf_result = etfs
            break
    
    for keyword, stocks in stock_map.items():
        if keyword in title:
            stock_result = stocks
            break
    
    return etf_result, stock_result

def format_news_for_push():
    """格式化新闻用于推送"""
    print("=" * 50)
    print("   财经新闻推送系统 v4.0")
    print(f"   时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # 抓取新闻
    print("[*] 开始抓取新闻...")
    
    all_news = []
    
    print("  [+] 网易财经...", end=" ")
    news = fetch_163_finance()
    print(f"{len(news)} 条")
    all_news.extend(news)
    
    time.sleep(2)
    
    print("  [+] 东方财富...", end=" ")
    news = fetch_eastmoney()
    print(f"{len(news)} 条")
    all_news.extend(news)
    
    time.sleep(2)
    
    print("  [+] 新浪财经...", end=" ")
    news = fetch_sina_finance()
    print(f"{len(news)} 条")
    all_news.extend(news)
    
    time.sleep(2)
    
    print("  [+] 36氪...", end=" ")
    news = fetch_36kr()
    print(f"{len(news)} 条")
    all_news.extend(news)
    
    # 去重
    seen = set()
    unique_news = []
    for item in all_news:
        if item['title'] not in seen:
            seen.add(item['title'])
            unique_news.append(item)
    
    print(f"[*] 共抓取 {len(unique_news)} 条新闻（去重后）")
    
    # 分级并分析
    s_news = []
    a_news = []
    
    for item in unique_news:
        level = classify_news(item['title'])
        sentiment, emoji = analyze_sentiment(item['title'])
        key_point = extract_key_point(item['title'])
        duration, duration_emoji = estimate_impact_duration(item['title'])
        etf, stocks = map_targets(item['title'])
        
        item['level'] = level
        item['sentiment'] = sentiment
        item['sentiment_emoji'] = emoji
        item['key_point'] = key_point
        item['duration'] = duration
        item['duration_emoji'] = duration_emoji
        item['etf'] = etf
        item['stocks'] = stocks
        
        # S级必须是明确的利好或利空，否则降级为A级
        if level == 'S' and sentiment in ['观望', '中性']:
            level = 'A'
            item['level'] = 'A'
        
        if level == 'S':
            s_news.append(item)
        elif level == 'A':
            a_news.append(item)
    
    # 格式化输出
    output = []
    output.append(f"📊 {datetime.now().strftime('%Y年%m月%d日 %H:%M')} 财经新闻")
    output.append("━" * 30)
    output.append("")
    
    if s_news:
        output.append("🟥 S级（主线级 | L2）")
        output.append("")
        for i, item in enumerate(s_news[:5], 1):
            output.append(f"{i}️⃣ {item['sentiment_emoji']}【{item['sentiment']}】{item['duration_emoji']}{item['duration']}")
            output.append(f"   📌 {item['key_point']}")
            targets = []
            if item['etf']:
                targets.append('ETF: ' + ' / '.join(item['etf'][:2]))
            if item['stocks']:
                targets.append('个股: ' + ' / '.join(item['stocks'][:2]))
            if targets:
                output.append(f"   📈 {' | '.join(targets)}")
        output.append("")
    
    if a_news:
        output.append("🟧 A级（轮动级 | L3）")
        output.append("")
        for i, item in enumerate(a_news[:5], 1):
            output.append(f"{i}️⃣ {item['sentiment_emoji']}【{item['sentiment']}】{item['duration_emoji']}{item['duration']}")
            output.append(f"   📌 {item['key_point']}")
            targets = []
            if item['etf']:
                targets.append('ETF: ' + ' / '.join(item['etf'][:2]))
            if item['stocks']:
                targets.append('个股: ' + ' / '.join(item['stocks'][:2]))
            if targets:
                output.append(f"   📈 {' | '.join(targets)}")
        output.append("")
    
    output.append("━" * 30)
    output.append("🤖 自动推送")
    
    result = "\n".join(output)
    
    # 保存
    save_path = r"C:\Users\asus\.qclaw\workspace\news-bot\latest_news.txt"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(result)
    
    print(f"\n[OK] 已保存到: {save_path}")
    
    return result

if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    result = format_news_for_push()
    print("\n" + result)

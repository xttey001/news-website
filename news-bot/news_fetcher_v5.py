# -*- coding: utf-8 -*-
"""
财经新闻抓取器 v5.0 - 按 S/A 级格式推送
包含：抖音财经新闻源、利好利空具体映射
"""
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import random
import re
import json

# 用户代理池
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
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
            time.sleep(random.uniform(1.5, 3.5))
            response = requests.get(url, headers=get_headers(), timeout=15)
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
        links = soup.select('a[href*="money.163.com"]')[:20]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 8:
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
        links = soup.select('a[href*="eastmoney.com"]')[:20]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 8:
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
        links = soup.select('a[href*="sina.com.cn"]')[:20]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 8:
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
        items = soup.select('.newsflash-item, .item-content, a[href*="36kr.com"]')[:15]
        
        for item in items:
            title = item.get_text(strip=True)
            if title and len(title) > 8:
                news_items.append({
                    'title': title[:150],
                    'url': 'https://36kr.com/newsflashes',
                    'source': '36氪'
                })
        return news_items
    except:
        return []

def fetch_douyin_finance():
    """抖音财经 - 通过今日头条财经频道获取"""
    try:
        # 使用今日头条财经频道（与抖音同源）
        url = "https://www.toutiao.com/c/finance/"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        
        # 尝试解析JSON数据
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'news' in str(script.string).lower():
                try:
                    # 尝试提取新闻标题
                    text = script.string
                    titles = re.findall(r'"title":"([^"]+)"', text)
                    for title in titles[:10]:
                        if len(title) > 8:
                            news_items.append({
                                'title': title,
                                'url': 'https://www.toutiao.com/c/finance/',
                                'source': '抖音财经'
                            })
                    break
                except:
                    pass
        
        # 如果JSON解析失败，尝试HTML解析
        if not news_items:
            links = soup.select('a[href*="toutiao.com"]')[:15]
            for link in links:
                title = link.get_text(strip=True)
                if title and len(title) > 8:
                    news_items.append({
                        'title': title[:100],
                        'url': link.get('href', 'https://www.toutiao.com/c/finance/'),
                        'source': '抖音财经'
                    })
        
        return news_items
    except:
        return []

def fetch_wallstreetcn():
    """华尔街见闻"""
    try:
        url = "https://wallstreetcn.com/news/global"
        response = fetch_with_retry(url)
        if not response:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = []
        links = soup.select('a[href*="wallstreetcn.com"]')[:15]
        
        for link in links:
            title = link.get_text(strip=True)
            if title and len(title) > 8:
                news_items.append({
                    'title': title[:100],
                    'url': link.get('href', ''),
                    'source': '华尔街见闻'
                })
        return news_items
    except:
        return []

# ============ 新闻分析与映射 ============

def classify_news(title):
    """S/A/B 分级 - 基于影响范围和持续性"""
    title_lower = title.lower()
    
    # S级：主线级 - 影响整个市场或主要板块，持续1周以上
    s_keywords = [
        '政策', '央行', '美联储', '利率', '降息', '加息', '监管', '改革', 
        '突破', '暴跌', '暴涨', '崩盘', '熔断', '战争', '制裁', '关税',
        '板块', '龙头', '拐点', '反转', '牛市', '熊市', '通胀', '通缩',
        'GDP', '经济', '财政', '货币', '汇率', '人民币', '美元',
        '全面', '整体', '系统性', '重大', '历史性'
    ]
    
    # A级：轮动级 - 影响细分赛道，中期催化
    a_keywords = [
        '签约', '合作', '收购', '并购', '融资', '上市', 'IPO', 
        '业绩', '盈利', '亏损', '增长', '下降', '发布', '推出',
        '创新', '研发', '投资', '扩张', '订单', '中标', '获批',
        '首单', '突破', '第一', '龙头'
    ]
    
    for kw in s_keywords:
        if kw in title:
            return 'S'
    
    for kw in a_keywords:
        if kw in title:
            return 'A'
    
    return 'B'

def analyze_sentiment(title):
    """利好/利空判断 - 更精确的映射"""
    title_lower = title.lower()
    
    # 利好关键词 - 按影响程度分类
    strong_bullish = ['暴涨', '涨停', '翻倍', '历史新高', '大赚', '暴赚', 
                      '重大利好', '超预期', '爆发', '井喷', '重大突破']
    
    normal_bullish = ['利好', '增长', '盈利', '上涨', '突破', '新高', 
                      '订单', '中标', '签约', '合作', '获批', '授权', 
                      '增持', '回购', '降息', '宽松', '刺激', '扶持', 
                      '补贴', '减税', '降准', '创新高', '大增', '增长',
                      '首发', '首创', '领先', '第一']
    
    # 利空关键词 - 按影响程度分类
    strong_bearish = ['暴跌', '跌停', '崩盘', '腰斩', '破产', '退市',
                      '重大利空', '黑天鹅', '暴雷', '崩塌']
    
    normal_bearish = ['利空', '亏损', '下跌', '破位', '新低',
                      '违约', '债务', '调查', '处罚', '罚款', '诉讼',
                      '加息', '紧缩', '制裁', '关税', '打压', '监管',
                      '下降', '减少', '裁员', '关闭', '终止', '失败',
                      '下滑', '缩水', '受挫']
    
    # 中性关键词
    neutral = ['发布', '推出', '计划', '预计', '或', '可能', '拟', '将', 
               '称', '表示', '宣布', '调整', '变化']
    
    # 计算得分
    strong_bull_score = sum(2 for kw in strong_bullish if kw in title_lower)
    normal_bull_score = sum(1 for kw in normal_bullish if kw in title_lower)
    strong_bear_score = sum(2 for kw in strong_bearish if kw in title_lower)
    normal_bear_score = sum(1 for kw in normal_bearish if kw in title_lower)
    
    bull_score = strong_bull_score + normal_bull_score
    bear_score = strong_bear_score + normal_bear_score
    
    if bull_score > bear_score:
        if strong_bull_score > 0:
            return '重大利好', '🟢🟢'
        return '利好', '🟢'
    elif bear_score > bull_score:
        if strong_bear_score > 0:
            return '重大利空', '🔴🔴'
        return '利空', '🔴'
    elif bull_score == bear_score and bull_score > 0:
        return '中性', '🟡'
    else:
        return '观望', '⚪'

def estimate_impact_duration(title):
    """估计影响时长"""
    title_lower = title.lower()
    
    # 1年以上
    long_term = ['政策', '改革', '监管', '制度', '法律', '法规', '战略', 
                 '转型', '并购', '收购', '重组', 'IPO', '上市', '退市',
                 '央行', '美联储', '利率', '汇率']
    
    # 1-6个月
    mid_term = ['业绩', '盈利', '订单', '签约', '合作', '发布', '推出',
                '研发', '创新', '投资', '扩张', '降息', '加息', '财报',
                '季报', '年报', '预期']
    
    # 1-4周
    short_term = ['暴涨', '暴跌', '涨停', '跌停', '异动', '突破', '新高', '新低']
    
    # 1-7天
    instant = ['今日', '明日', '本周', '盘中', '收盘', '开盘', '紧急', '突发']
    
    if any(kw in title_lower for kw in instant):
        return '1-7天'
    elif any(kw in title_lower for kw in short_term):
        return '1-4周'
    elif any(kw in title_lower for kw in mid_term):
        return '1-6个月'
    elif any(kw in title_lower for kw in long_term):
        return '1年以上'
    else:
        return '1-4周'

def map_detailed_targets(title):
    """详细映射ETF和个股"""
    # ETF映射 - 更详细
    etf_map = {
        # ===== 科技/AI =====
        'AI': {'etf': ['AIETF(515070)', '科创50ETF(588000)'], 'direction': '资金流入'},
        '人工智能': {'etf': ['AIETF(515070)', '科技ETF(515000)'], 'direction': '资金流入'},
        '半导体': {'etf': ['半导体ETF(512480)', '芯片ETF(512760)'], 'direction': '关注'},
        '芯片': {'etf': ['芯片ETF(512760)', '半导体ETF(512480)'], 'direction': '关注'},
        '光刻机': {'etf': ['半导体ETF(512480)'], 'direction': '资金流入'},
        '算力': {'etf': ['AIETF(515070)', '云计算ETF(516510)'], 'direction': '资金流入'},
        '云计算': {'etf': ['云计算ETF(516510)', '科技ETF(515000)'], 'direction': '关注'},
        '数据中心': {'etf': ['大数据ETF(515700)'], 'direction': '关注'},
        '华为': {'etf': ['华为概念ETF'], 'direction': '资金流入'},
        '鸿蒙': {'etf': ['华为概念ETF', '科技ETF'], 'direction': '资金流入'},
        
        # ===== 新能源 =====
        '新能源': {'etf': ['新能源ETF(516160)', '光伏ETF(515790)'], 'direction': '关注'},
        '光伏': {'etf': ['光伏ETF(515790)', '新能源ETF(516160)'], 'direction': '关注'},
        '锂电': {'etf': ['锂电池ETF(159871)', '新能源车ETF(515030)'], 'direction': '关注'},
        '锂电池': {'etf': ['锂电池ETF(159871)'], 'direction': '关注'},
        '新能源车': {'etf': ['新能源车ETF(515030)', '汽车ETF(516110)'], 'direction': '关注'},
        '电动车': {'etf': ['新能源车ETF(515030)'], 'direction': '关注'},
        '储能': {'etf': ['储能ETF'], 'direction': '资金流入'},
        '风电': {'etf': ['风电ETF(159611)'], 'direction': '关注'},
        '充电桩': {'etf': ['充电桩ETF'], 'direction': '关注'},
        
        # ===== 医药 =====
        '创新药': {'etf': ['创新药ETF(159992)', '生物医药ETF(512290)'], 'direction': '关注'},
        '医药': {'etf': ['医药ETF(512010)', '生物医药ETF(512290)'], 'direction': '关注'},
        '生物': {'etf': ['生物医药ETF(512290)'], 'direction': '关注'},
        '疫苗': {'etf': ['生物医药ETF(512290)'], 'direction': '关注'},
        '医疗': {'etf': ['医疗ETF(159828)'], 'direction': '关注'},
        'CRO': {'etf': ['生物医药ETF(512290)'], 'direction': '关注'},
        
        # ===== 金融 =====
        '券商': {'etf': ['券商ETF(512000)', '证券ETF(512880)'], 'direction': '资金流入(牛市信号)'},
        '证券': {'etf': ['证券ETF(512880)', '券商ETF(512000)'], 'direction': '资金流入'},
        '银行': {'etf': ['银行ETF(512800)', '金融ETF(510820)'], 'direction': '防御'},
        '保险': {'etf': ['保险ETF(512880)'], 'direction': '关注'},
        
        # ===== 消费 =====
        '消费': {'etf': ['消费ETF(159928)', '消费50ETF(515650)'], 'direction': '关注'},
        '白酒': {'etf': ['酒ETF(512690)', '消费ETF(159928)'], 'direction': '关注'},
        '酒': {'etf': ['酒ETF(512690)'], 'direction': '关注'},
        '食品': {'etf': ['食品饮料ETF(515170)'], 'direction': '关注'},
        '旅游': {'etf': ['旅游ETF(159766)'], 'direction': '资金流入'},
        
        # ===== 资源/周期 =====
        '黄金': {'etf': ['黄金ETF(518880)', '黄金股ETF(517520)'], 'direction': '避险流入'},
        '石油': {'etf': ['油气ETF(159307)', '能源ETF(159945)'], 'direction': '关注'},
        '煤炭': {'etf': ['煤炭ETF(515220)'], 'direction': '关注'},
        '有色': {'etf': ['有色金属ETF(512400)'], 'direction': '关注'},
        '稀土': {'etf': ['稀土ETF(516780)'], 'direction': '关注'},
        '锂矿': {'etf': ['有色金属ETF(512400)'], 'direction': '关注'},
        '钢铁': {'etf': ['钢铁ETF(515210)'], 'direction': '关注'},
        
        # ===== 其他 =====
        '军工': {'etf': ['军工ETF(512660)', '国防军工ETF(512810)'], 'direction': '资金流入'},
        '房地产': {'etf': ['房地产ETF(512200)'], 'direction': '观望'},
        '地产': {'etf': ['房地产ETF(512200)'], 'direction': '观望'},
        '基建': {'etf': ['基建ETF(159619)'], 'direction': '关注'},
        '传媒': {'etf': ['传媒ETF(512980)'], 'direction': '关注'},
        '游戏': {'etf': ['游戏ETF(516010)'], 'direction': '关注'},
    }
    
    # 个股映射 - 重要龙头
    stock_map = {
        '华为': ['华为概念: 赛力斯', '立讯精密', '欧菲光'],
        '苹果': ['苹果链: 立讯精密', '歌尔股份', '蓝思科技'],
        '特斯拉': ['特斯拉链: 拓普集团', '三花智控', '宁德时代'],
        '英伟达': ['英伟达链: 工业富联', '浪潮信息', '中际旭创'],
        'OpenAI': ['AI: 科大讯飞', '昆仑万维', '三六零'],
        '微软': ['AI: 科大讯飞', '金山办公'],
        '宁德时代': ['宁德时代', '亿纬锂能'],
        '比亚迪': ['比亚迪', '长城汽车'],
        '茅台': ['贵州茅台', '五粮液'],
        '贵州茅台': ['贵州茅台', '五粮液'],
        '中芯国际': ['中芯国际', '华虹半导体'],
    }
    
    # 利空映射
    bearish_map = {
        'AI': {'etf': ['AIETF(515070)'], 'direction': '资金流出'},
        '半导体': {'etf': ['半导体ETF(512480)'], 'direction': '资金流出'},
        '新能源': {'etf': ['新能源ETF(516160)'], 'direction': '资金流出'},
        '医药': {'etf': ['医药ETF(512010)'], 'direction': '资金流出'},
        '消费': {'etf': ['消费ETF(159928)'], 'direction': '资金流出'},
        '房地产': {'etf': ['房地产ETF(512200)'], 'direction': '继续承压'},
        '银行': {'etf': ['银行ETF(512800)'], 'direction': '风险关注'},
    }
    
    sentiment, _ = analyze_sentiment(title)
    
    result = {'etf': None, 'stocks': None, 'direction': None}
    
    # 查找ETF映射
    for keyword, mapping in etf_map.items():
        if keyword in title:
            if '利空' in sentiment:
                result['etf'] = bearish_map.get(keyword, {}).get('etf', mapping['etf'])
                result['direction'] = bearish_map.get(keyword, {}).get('direction', '资金流出')
            else:
                result['etf'] = mapping['etf']
                result['direction'] = mapping['direction']
            break
    
    # 查找个股映射
    for keyword, stocks in stock_map.items():
        if keyword in title:
            result['stocks'] = stocks
            break
    
    return result

def extract_key_point(title):
    """提取一句话要点"""
    noise_patterns = [
        r'\d+分钟前', r'\d+小时前', r'\d+天前',
        r'分享至', r'打开微信', r'扫一扫', r'点击屏幕', r'右上角', r'分享按钮',
        r'打开网页后', r'原文', r'""', r'“”', r'【.*?】'
    ]
    
    clean_title = title
    for pattern in noise_patterns:
        clean_title = re.sub(pattern, '', clean_title)
    
    clean_title = clean_title.strip()
    
    # 按分隔符截取最核心部分
    for sep in ['。', '，', '：', ':', '|', '-', '——']:
        if sep in clean_title:
            parts = [p.strip() for p in clean_title.split(sep) if p.strip()]
            if parts and len(parts[0]) > 8:
                clean_title = parts[0]
                break
    
    if len(clean_title) > 50:
        clean_title = clean_title[:47] + '...'
    
    return clean_title.strip()

# ============ 主函数 ============

def format_news_for_push():
    """格式化新闻用于推送 - 按用户要求的格式"""
    print("=" * 50)
    print("   财经新闻推送系统 v5.0")
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
    
    time.sleep(2)
    
    print("  [+] 抖音财经...", end=" ")
    news = fetch_douyin_finance()
    print(f"{len(news)} 条")
    all_news.extend(news)
    
    time.sleep(2)
    
    print("  [+] 华尔街见闻...", end=" ")
    news = fetch_wallstreetcn()
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
        sentiment, sentiment_emoji = analyze_sentiment(item['title'])
        key_point = extract_key_point(item['title'])
        duration = estimate_impact_duration(item['title'])
        target_info = map_detailed_targets(item['title'])
        
        item['level'] = level
        item['sentiment'] = sentiment
        item['sentiment_emoji'] = sentiment_emoji
        item['key_point'] = key_point
        item['duration'] = duration
        item['etf'] = target_info['etf']
        item['stocks'] = target_info['stocks']
        item['direction'] = target_info['direction']
        
        # S级必须是明确的利好或利空，否则降级为A级
        if level == 'S' and '观望' in sentiment:
            level = 'A'
            item['level'] = 'A'
        
        if level == 'S':
            s_news.append(item)
        elif level == 'A':
            a_news.append(item)
    
    # 按格式输出
    today = datetime.now()
    date_str = today.strftime('%m月%d日')
    
    output = []
    output.append(f"📊 **财经新闻 S/A 级精选 {date_str}**")
    output.append("")
    output.append("---")
    output.append("")
    
    # S级新闻
    if s_news:
        output.append("🔥 **S级（主线级）**")
        output.append("")
        for item in s_news[:3]:
            output.append(f"**{item['key_point']}**")
            output.append(f"📌 要点：{item['sentiment']}，影响时长{item['duration']}")
            
            targets = []
            if item['etf']:
                targets.append('📈 映射ETF：' + '、'.join(item['etf'][:2]))
            if item['direction']:
                targets.append(f"💡 资金信号：{item['direction']}")
            if item['stocks']:
                targets.append('🎯 个股：' + '、'.join(item['stocks'][:2]))
            
            if targets:
                output.extend(targets)
            output.append("")
    
    # A级新闻
    if a_news:
        output.append("---")
        output.append("")
        output.append("🌐 **A级（轮动级）**")
        output.append("")
        for item in a_news[:4]:
            output.append(f"**{item['key_point']}**")
            output.append(f"📌 要点：{item['sentiment']}，影响时长{item['duration']}")
            
            targets = []
            if item['etf']:
                targets.append('📈 映射ETF：' + '、'.join(item['etf'][:2]))
            if item['direction']:
                targets.append(f"💡 资金信号：{item['direction']}")
            
            if targets:
                output.extend(targets)
            output.append("")
    
    # 分类说明
    output.append("---")
    output.append("📋 **分类说明**")
    output.append("S级 = 影响ETF + 持续1周以上 + 改变资金方向")
    output.append("A级 = 主线内部资金再分配，细分赛道催化")
    output.append("B级 = 个股/噪音（已过滤）")
    
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

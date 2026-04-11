# -*- coding: utf-8 -*-
"""
沙僧韭菜直觉模型 - 预测散户行为

核心任务：预测散户看到新闻后的行为
输出四种概率：
1. 追高买入概率 (FOMO) - 怕踏空
2. 抄底买入概率 (左侧幻想) - 超跌反弹幻想
3. 恐慌卖出概率 - 风险厌恶
4. 观望概率 - 无感

心理机制驱动：
- FOMO: 暴涨、创新高、主升浪
- 贪婪: 翻倍、目标价、业绩暴增
- 安全错觉: 政策支持、机构背书、龙头
- 抄底冲动: 超跌、错杀、黄金坑
- 恐慌: 暴跌、爆雷、崩盘
- 理解难度: 越简单越容易触发韭菜
"""

import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any

# 时间衰减因子
TIME_DECAY = {
    0: 1.0,   # 今天
    1: 0.7,   # 昨天
    2: 0.5,   # 前天
    3: 0.35,  # 3天前
    4: 0.25,  # 4天前
    5: 0.18,  # 5天前
    6: 0.12,  # 6天前
}

# 长期新闻类型（无视时间衰减）
LONG_TERM_KEYWORDS = [
    '黄金', '白银', '原油', '地缘', '政治', '战争', '冲突',
    '美联储', '央行', '利率', '降息', '加息', '通胀',
    '经济', '衰退', '危机', '萧条'
]


class SangshaModel:
    """沙僧韭菜直觉模型"""
    
    def __init__(self):
        # 关键词权重配置
        self.keyword_weights = {
            # === 追高买入 (FOMO) ===
            'fomo_keywords': {
                # 暴涨信号
                '暴涨': 90, '狂涨': 90, '飙升': 85, '大涨': 80, '涨停': 85,
                '创新高': 88, '历史新高': 90, '再创新高': 88,
                '主升浪': 85, '加速上涨': 82, '强势上涨': 78,
                '突破': 70, '放量突破': 80, '强势突破': 75,
                # 利润诱惑
                '翻倍': 92, '暴涨': 90, '暴富': 95, '盈利': 65,
                '目标价': 75, '看涨': 70, '强烈推荐': 80, '上调评级': 78,
                '业绩大增': 75, '业绩暴增': 85, '超预期': 72,
            },
            
            # === 抄底买入 (左侧幻想) ===
            'bottom_fishing_keywords': {
                '超跌': 80, '错杀': 82, '黄金坑': 88, '底部': 75,
                '反弹': 70, '反转': 78, '回升': 72, '修复': 68,
                '低估': 75, '价值洼地': 85, '估值修复': 72,
                '逢低': 65, '低吸': 68, '布局': 60,
                '业绩拐点': 78, '困境反转': 80,
            },
            
            # === 恐慌卖出 ===
            'panic_keywords': {
                '暴跌': 90, '狂跌': 92, '崩盘': 95, '闪崩': 88,
                '爆雷': 85, '违约': 82, '破产': 90, '退市': 88,
                '大跌': 80, '重挫': 82, '跳水': 78,
                '利空': 70, '风险': 65, '恐慌': 75,
                '裁员': 72, '亏损': 68, '造假': 85,
                '制裁': 75, '限制': 68, '禁令': 72,
            },
            
            # === 观望 (复杂难懂) ===
            'confusing_keywords': {
                '逆回购': -30, '麻辣粉': -25, 'SLF': -25,
                '量化宽松': -20, 'M2': -25, '社融': -20,
                '汇率': -15, '中美关系': -10,
                '宏观': -20, '政策': -10, '改革': -15,
            }
        }
        
        # 简单易懂加分（越简单越容易触发韭菜）
        self.simple_keywords = {
            '涨': 15, '跌': 15, '涨了': 18, '跌了': 18,
            '买': 12, '卖': 12, '赚钱': 20, '亏钱': 20,
            '涨停': 25, '跌停': 25,
            '牛市': 22, '熊市': 20,
            '暴富': 30, '翻倍': 28,
        }
        
    def _calculate_keyword_score(self, text: str, keyword_dict: Dict[str, int]) -> float:
        """计算文本中关键词的加权得分"""
        score = 0
        text_lower = text.lower()
        for keyword, weight in keyword_dict.items():
            if keyword in text:
                # 计算出现次数
                count = text.count(keyword)
                score += weight * min(count, 3)  # 最多计算3次
        return score
    
    def _is_long_term_news(self, title: str, summary: str = '') -> bool:
        """判断是否为长期新闻（无视时间衰减）"""
        text = title + ' ' + summary
        for keyword in LONG_TERM_KEYWORDS:
            if keyword in text:
                return True
        return False
    
    def _calculate_time_decay(self, news_date: str, current_date: str) -> float:
        """计算时间衰减因子"""
        try:
            news_dt = datetime.strptime(news_date, '%Y-%m-%d')
            curr_dt = datetime.strptime(current_date, '%Y-%m-%d')
            days_diff = (curr_dt - news_dt).days
            return TIME_DECAY.get(days_diff, 0.1)
        except:
            return 1.0
    
    def analyze_single_news(self, news_item: Dict[str, Any], 
                           price_change: float = 0,
                           volume_change: float = 0,
                           is_long_term: bool = False) -> Dict[str, Any]:
        """
        分析单条新闻的散户行为概率
        
        Args:
            news_item: 新闻 dict，需包含 title, summary 等
            price_change: 价格变动百分比
            volume_change: 成交量变化百分比
            is_long_term: 是否为长期新闻
        
        Returns:
            dict: {
                'news': str,
                '追高买入概率': 0-100,
                '抄底买入概率': 0-100,
                '恐慌卖出概率': 0-100,
                '观望概率': 0-100,
                '情绪标签': [...],
                '韭菜行为总结': str,
                '市场含义': str,
                '买入概率': 0-100,  # 追高+抄底的加权
            }
        """
        title = news_item.get('title', '')
        summary = news_item.get('summary', '')
        text = f"{title} {summary}"
        
        # 1. 计算各维度关键词得分
        fomo_score = self._calculate_keyword_score(text, 
            self.keyword_weights['fomo_keywords'])
        bottom_score = self._calculate_keyword_score(text, 
            self.keyword_weights['bottom_fishing_keywords'])
        panic_score = self._calculate_keyword_score(text, 
            self.keyword_weights['panic_keywords'])
        confuse_score = self._calculate_keyword_score(text, 
            self.keyword_weights['confusing_keywords'])
        
        # 2. 简单易懂加分
        simple_bonus = 0
        for kw, bonus in self.simple_keywords.items():
            if kw in text:
                simple_bonus += bonus
        
        # 3. 市场信号调整
        market_signal = 0
        if price_change > 5:
            market_signal += 15  # 大涨刺激追高
        elif price_change < -5:
            market_signal += 10  # 大跌可能恐慌
        elif abs(price_change) < 1:
            market_signal -= 5   # 横盘让人观望
            
        if volume_change > 50:
            market_signal += 10  # 放量说明情绪活跃
        
        # 4. 归一化到0-100概率
        total_raw = fomo_score + bottom_score + panic_score + abs(confuse_score) + 50
        if total_raw <= 0:
            total_raw = 1
        
        # 基础概率
        base_fomo = min(95, max(5, (fomo_score + simple_bonus + market_signal) * 100 / total_raw))
        base_bottom = min(90, max(5, bottom_score * 100 / total_raw))
        base_panic = min(90, max(5, panic_score * 100 / total_raw))
        base_confuse = min(80, max(10, abs(confuse_score) * 80 / total_raw))
        
        # 观望概率 = 100 - 其他概率的有效部分
        other_prob = (base_fomo * 0.4 + base_bottom * 0.3 + base_panic * 0.3)
        watch_prob = max(10, 100 - other_prob)
        
        # 5. 生成情绪标签
        emotion_tags = []
        if base_fomo > 40:
            emotion_tags.append('FOMO')
        if base_bottom > 30:
            emotion_tags.append('抄底冲动')
        if base_panic > 35:
            emotion_tags.append('恐慌')
        if base_confuse > 30:
            emotion_tags.append('迷茫')
        if simple_bonus > 20:
            emotion_tags.append('易懂')
        
        # 6. 生成韭菜行为总结
        if base_fomo > 60:
            behavior = "散户疯了，都在追！"
            market_meaning = "顶部风险"
        elif base_fomo > 40:
            behavior = "散户开始眼红，想冲进去"
            market_meaning = "分歧加大"
        elif base_bottom > 50:
            behavior = "散户想抄底，认为是机会"
            market_meaning = "可能有反弹"
        elif base_panic > 50:
            behavior = "散户恐慌，想割肉"
            market_meaning = "可能见底"
        elif base_confuse > 40:
            behavior = "散户看不懂，在观望"
            market_meaning = "震荡整理"
        else:
            behavior = "散户情绪平稳"
            market_meaning = "中性"
        
        # 买入概率 = 追高概率*0.6 + 抄底概率*0.4
        buy_prob = int(base_fomo * 0.6 + base_bottom * 0.4)
        
        return {
            'news': title[:30] + '...' if len(title) > 30 else title,
            'title': title,
            'full_title': title,
            'summary': summary[:50] + '...' if len(summary) > 50 else summary,
            '追高买入概率': int(base_fomo),
            '抄底买入概率': int(base_bottom),
            '恐慌卖出概率': int(base_panic),
            '观望概率': int(watch_prob),
            '情绪标签': emotion_tags,
            '韭菜行为总结': behavior,
            '市场含义': market_meaning,
            '买入概率': buy_prob,
            'is_long_term': is_long_term
        }
    
    def analyze_multi_day(self, news_list: List[Dict[str, Any]], 
                         current_date: str = None,
                         market_data: Dict = None) -> List[Dict[str, Any]]:
        """
        分析多天新闻，累积计算散户行为
        
        Args:
            news_list: 多天新闻的列表 [{date, s_level, a_level, douyin}, ...]
            current_date: 当前日期
            market_data: 市场数据 {code: {klines, realtime}}
        
        Returns:
            list: 按买入概率排序的TOP新闻列表
        """
        if current_date is None:
            current_date = datetime.now().strftime('%Y-%m-%d')
        
        all_results = []
        
        for idx, day_news in enumerate(news_list):
            news_date = day_news.get('date', current_date)
            
            # 时间衰减因子（长期新闻无视）
            is_long_term = self._is_long_term_news(
                day_news.get('s_level', [{}])[0].get('title', '') if day_news.get('s_level') else ''
            )
            if is_long_term:
                decay = 1.0
            else:
                decay = self._calculate_time_decay(news_date, current_date)
            
            # 合并所有级别的新闻（包含 all_news 字段的"全部新闻"）
            all_news_items = []
            # 1. 优先使用 all_news 字段（全量新闻）
            raw_all = day_news.get('all_news', [])
            if raw_all:
                all_news_items.extend(raw_all)
            # 2. 再加上 s_level/a_level/douyin（兜底）
            for level in ['s_level', 'a_level', 'douyin']:
                items = day_news.get(level, [])
                if items:
                    # 避免重复添加
                    for item in items:
                        title = item.get('title', '')
                        if not any(n.get('title', '') == title for n in all_news_items):
                            all_news_items.append(item)
            
            # 分析每条新闻
            for item in all_news_items:
                title = item.get('title', '')
                if not title:
                    continue
                
                # 获取相关价格数据（如果有）
                price_change = 0
                volume_change = 0
                if market_data and item.get('stocks'):
                    # 尝试从ETF/个股获取价格变动
                    for stock in item.get('stocks', [])[:1]:
                        # 简单匹配（实际应该更精确）
                        pass
                
                result = self.analyze_single_news(
                    item, price_change, volume_change, is_long_term
                )
                result['date'] = news_date
                result['decay'] = decay
                result['weighted_buy_prob'] = int(result['买入概率'] * decay)
                
                all_results.append(result)
        
        # 7天累积：按加权买入概率排序
        all_results.sort(key=lambda x: x['weighted_buy_prob'], reverse=True)
        
        # 去重并保留TOP
        seen = set()
        unique_results = []
        for r in all_results:
            key = r['title'][:20]  # 按标题去重
            if key not in seen:
                seen.add(key)
                unique_results.append(r)
        
        return unique_results[:10]  # 返回TOP10
    
    def generate_sangsha_output(self, news_data: Dict, 
                                current_date: str = None,
                                market_data: Dict = None) -> Dict[str, Any]:
        """
        生成完整的沙僧模块输出
        
        Args:
            news_data: news-data.js 格式的数据
            current_date: 当前日期
            market_data: 市场行情数据
        
        Returns:
            dict: 沙僧模块输出
        """
        if current_date is None:
            current_date = datetime.now().strftime('%Y-%m-%d')
        
        # 转换news_data为列表格式
        news_list = []
        for date, day_data in news_data.items():
            if date == 'availableDates':
                continue
            news_list.append(day_data)
        
        # 按日期排序
        news_list.sort(key=lambda x: x.get('date', ''), reverse=True)
        
        # 只取最近7天
        news_list = news_list[:7]
        
        # 统计全量新闻数量
        total_news_count = 0
        for day in news_list:
            # 优先用 all_news
            all_n = day.get('all_news', [])
            if all_n:
                total_news_count += len(all_n)
            else:
                # 兜底：统计 s_level + a_level + douyin
                for level in ['s_level', 'a_level', 'douyin']:
                    items = day.get(level, [])
                    if items:
                        total_news_count += len(items)
        
        # 分析
        analysis_results = self.analyze_multi_day(
            news_list, current_date, market_data
        )
        
        # 汇总统计
        total_buy_prob = sum(r['买入概率'] for r in analysis_results) / len(analysis_results) if analysis_results else 0
        total_panic = sum(r['恐慌卖出概率'] for r in analysis_results) / len(analysis_results) if analysis_results else 0
        
        # 市场情绪判断
        if total_buy_prob > 60:
            overall_sentiment = "狂热"
            advice = "风险累积中，注意高位"
        elif total_buy_prob > 45:
            overall_sentiment = "积极"
            advice = "可适度参与，但需谨慎"
        elif total_panic > 50:
            overall_sentiment = "恐慌"
            advice = "可能见底，分批布局"
        else:
            overall_sentiment = "平稳"
            advice = "震荡整理，观望为主"
        
        return {
            "沙僧模块": {
                "overall_sentiment": overall_sentiment,
                "advice": advice,
                "avg_buy_prob": int(total_buy_prob),
                "avg_panic_prob": int(total_panic),
                "analysis_results": analysis_results,
                "total_news_count": total_news_count,
                "time_window": "7天累积（长期新闻除外）"
            }
        }


# 简化调用函数
def run_sangsha(news_data: Dict, current_date: str = None, market_data: Dict = None) -> Dict:
    """运行沙僧模型"""
    model = SangshaModel()
    return model.generate_sangsha_output(news_data, current_date, market_data)


if __name__ == '__main__':
    # 测试
    test_news = {
        "2026-04-08": {
            "date": "2026-04-08",
            "s_level": [
                {
                    "title": "AI芯片/半导体板块暴涨，创业板人工智能ETF涨超7%",
                    "summary": "科创芯片ETF涨超5%，创业板AI ETF涨超7%，中际旭创涨停，光模块继续涨",
                    "etfs": [{"name": "588890 科创芯片ETF", "sentiment": "利好"}],
                    "stocks": ["中际旭创", "新易盛", "天孚通信"]
                }
            ],
            "a_level": [
                {
                    "title": "创业板人工智能ETF南方(159382)涨超7%",
                    "summary": "创业板人工智能ETF涨停附近，跟踪创业板AI指数强势上涨",
                    "etfs": [{"name": "159382 创业板AI ETF", "sentiment": "利好"}],
                    "stocks": ["中际旭创", "新易盛"]
                }
            ],
            "douyin": []
        }
    }
    
    model = SangshaModel()
    result = run_sangsha(test_news, "2026-04-09", None)
    print(json.dumps(result, ensure_ascii=False, indent=2))

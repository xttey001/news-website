"""
每月重大事件影响因子模块
用于将重大事件作为五维智能体分析的衡量因子

功能：
1. 加载每月重大事件数据
2. 计算事件影响因子
3. 与五维智能体分析结果融合
4. 提供事件预警和策略建议
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Any


class MonthlyEventsFactor:
    """每月重大事件影响因子分析器"""
    
    def __init__(self, data_file: str = "../../monthly-events-data.js"):
        """
        初始化事件因子分析器
        
        Args:
            data_file: 事件数据文件路径
        """
        self.data_file = data_file
        self.events_data = {}
        self.load_data()
    
    def load_data(self):
        """加载事件数据"""
        try:
            # 读取JS文件并提取JSON数据
            with open(self.data_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取JSON部分（从const monthlyEventsData = { 到第一个闭合的}）
            # 找到第一个 { 的位置
            start = content.find('{')
            if start == -1:
                raise ValueError("未找到JSON起始位置")
            
            # 使用括号匹配找到对应的闭合位置
            brace_count = 0
            end = start
            for i, char in enumerate(content[start:], start):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end = i + 1
                        break
            
            if end > start:
                json_str = content[start:end]
                self.events_data = json.loads(json_str)
        except Exception as e:
            print(f"加载事件数据失败: {e}")
            self.events_data = {}
    
    def get_month_events(self, year_month: str) -> Optional[Dict]:
        """
        获取指定月份的事件数据
        
        Args:
            year_month: 年月格式 "2026-05"
            
        Returns:
            该月份的事件数据
        """
        return self.events_data.get(year_month)
    
    def get_upcoming_events(self, days: int = 7) -> List[Dict]:
        """
        获取未来N天内的重大事件
        
        Args:
            days: 天数
            
        Returns:
            即将发生的事件列表
        """
        today = datetime.now()
        upcoming = []
        
        for month_key, month_data in self.events_data.items():
            for event in month_data.get('events', []):
                try:
                    event_date = datetime.strptime(event['date'], '%Y-%m-%d')
                    days_diff = (event_date - today).days
                    
                    if 0 <= days_diff <= days:
                        upcoming.append({
                            **event,
                            'days_until': days_diff
                        })
                except:
                    continue
        
        return sorted(upcoming, key=lambda x: x['days_until'])
    
    def calculate_event_impact_factor(self, year_month: str) -> Dict[str, Any]:
        """
        计算指定月份的事件影响因子
        
        Args:
            year_month: 年月格式
            
        Returns:
            事件影响因子分析结果
        """
        month_data = self.get_month_events(year_month)
        if not month_data:
            return {
                "factor_score": 0.5,
                "confidence": "低",
                "description": "无事件数据"
            }
        
        events = month_data.get('events', [])
        
        # 统计事件数量和级别
        s_count = sum(1 for e in events if e.get('impact_level') == 'S级')
        a_count = sum(1 for e in events if e.get('impact_level') == 'A级')
        
        # 计算平均概率
        avg_probability = sum(
            e.get('bajie_factor', {}).get('probability', 50) 
            for e in events
        ) / len(events) if events else 50
        
        # 计算因子得分 (0-1)
        # S级事件权重更高
        factor_score = min(1.0, (
            s_count * 0.15 + 
            a_count * 0.08 + 
            (avg_probability / 100) * 0.3
        ))
        
        # 风险定义统计
        risk_types = {}
        for e in events:
            risk_def = e.get('wukong_factor', {}).get('risk_definition', '未知')
            risk_types[risk_def] = risk_types.get(risk_def, 0) + 1
        
        # 确定主导风险类型
        dominant_risk = max(risk_types, key=risk_types.get) if risk_types else "未知"
        
        return {
            "factor_score": round(factor_score, 2),
            "confidence": "高" if len(events) >= 5 else "中",
            "s_level_count": s_count,
            "a_level_count": a_count,
            "avg_probability": round(avg_probability, 1),
            "dominant_risk_type": dominant_risk,
            "risk_distribution": risk_types,
            "total_events": len(events),
            "description": f"本月{s_count}个S级事件，主导风险类型：{dominant_risk}"
        }
    
    def get_sector_event_exposure(self, year_month: str, sector: str) -> Dict[str, Any]:
        """
        获取特定板块的事件暴露度
        
        Args:
            year_month: 年月格式
            sector: 板块名称
            
        Returns:
            板块事件暴露分析
        """
        month_data = self.get_month_events(year_month)
        if not month_data:
            return {"exposure": 0, "events": []}
        
        related_events = []
        for event in month_data.get('events', []):
            sectors = event.get('affected_sectors', [])
            if sector in sectors:
                related_events.append(event)
        
        # 计算暴露度得分
        exposure_score = sum(
            0.3 if e.get('impact_level') == 'S级' else 0.15
            for e in related_events
        )
        
        return {
            "exposure": min(1.0, exposure_score),
            "event_count": len(related_events),
            "events": related_events,
            "avg_probability": sum(
                e.get('bajie_factor', {}).get('probability', 50)
                for e in related_events
            ) / len(related_events) if related_events else 0
        }
    
    def generate_event_strategy(self, year_month: str) -> Dict[str, Any]:
        """
        生成基于事件的策略建议
        
        Args:
            year_month: 年月格式
            
        Returns:
            策略建议
        """
        factor = self.calculate_event_impact_factor(year_month)
        upcoming = self.get_upcoming_events(14)  # 未来14天
        
        # 根据因子得分生成策略
        if factor['factor_score'] >= 0.7:
            position_suggestion = "高仓位（70-80%）"
            action = "积极布局"
        elif factor['factor_score'] >= 0.5:
            position_suggestion = "中等仓位（50-60%）"
            action = "选择性参与"
        else:
            position_suggestion = "低仓位（30-40%）"
            action = "谨慎观望"
        
        # 生成重点关注板块
        month_data = self.get_month_events(year_month)
        all_sectors = []
        if month_data:
            for event in month_data.get('events', []):
                all_sectors.extend(event.get('affected_sectors', []))
        
        # 统计板块出现频率
        sector_freq = {}
        for s in all_sectors:
            sector_freq[s] = sector_freq.get(s, 0) + 1
        
        top_sectors = sorted(
            sector_freq.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:5]
        
        return {
            "position_suggestion": position_suggestion,
            "action": action,
            "factor_score": factor['factor_score'],
            "dominant_risk": factor['dominant_risk_type'],
            "focus_sectors": [s[0] for s in top_sectors],
            "upcoming_events": upcoming[:3],  # 最近3个事件
            "risk_alerts": self._generate_risk_alerts(factor, upcoming)
        }
    
    def _generate_risk_alerts(self, factor: Dict, upcoming: List) -> List[str]:
        """生成风险预警"""
        alerts = []
        
        if factor['s_level_count'] >= 3:
            alerts.append("⚠️ 本月S级事件密集，市场波动可能加大")
        
        if factor['dominant_risk_type'] == '假风险':
            alerts.append("💡 多个事件被定义为'假风险'，可能存在逆向布局机会")
        
        if factor['dominant_risk_type'] == '真风险':
            alerts.append("🚨 多个事件被定义为'真风险'，建议控制仓位避险")
        
        # 检查即将发生的高影响事件
        high_impact_upcoming = [
            e for e in upcoming 
            if e.get('impact_level') == 'S级' and e.get('days_until', 7) <= 3
        ]
        if high_impact_upcoming:
            alerts.append(f"⏰ 未来3天有{len(high_impact_upcoming)}个S级事件，注意市场反应")
        
        return alerts
    
    def integrate_with_wukong_analysis(self, date_str: str, wukong_data: Dict) -> Dict:
        """
        将事件因子与悟空分析结果融合
        
        Args:
            date_str: 日期字符串 "2026-05-18"
            wukong_data: 悟空分析原始数据
            
        Returns:
            融合后的分析结果
        """
        # 提取年月
        year_month = date_str[:7]
        
        # 获取事件因子
        factor = self.calculate_event_impact_factor(year_month)
        strategy = self.generate_event_strategy(year_month)
        
        # 融合分析
        integrated = {
            "original_wukong": wukong_data,
            "event_factor": factor,
            "event_strategy": strategy,
            "integrated_analysis": {
                "market_sentiment": self._adjust_sentiment(
                    wukong_data.get('emotion', '中性'),
                    factor['factor_score']
                ),
                "position_adjustment": self._calculate_position_adjustment(
                    wukong_data,
                    factor
                ),
                "key_factors": self._merge_key_factors(
                    wukong_data.get('analysis', []),
                    strategy.get('upcoming_events', [])
                ),
                "risk_alerts": (
                    wukong_data.get('risk_alerts', []) + 
                    strategy.get('risk_alerts', [])
                )
            }
        }
        
        return integrated
    
    def _adjust_sentiment(self, base_sentiment: str, factor_score: float) -> str:
        """根据事件因子调整情绪判断"""
        sentiment_map = {
            "强烈看多": 2,
            "偏多": 1,
            "中性偏多": 0.5,
            "中性": 0,
            "中性偏空": -0.5,
            "偏空": -1,
            "强烈看空": -2,
            "谨慎": -0.3
        }
        
        base_score = sentiment_map.get(base_sentiment, 0)
        
        # 根据因子得分调整
        if factor_score >= 0.7:
            adjusted = base_score + 0.5
        elif factor_score >= 0.5:
            adjusted = base_score + 0.2
        elif factor_score <= 0.3:
            adjusted = base_score - 0.3
        else:
            adjusted = base_score
        
        # 映射回情绪标签
        if adjusted >= 1.5:
            return "强烈看多"
        elif adjusted >= 0.8:
            return "偏多"
        elif adjusted >= 0.3:
            return "中性偏多"
        elif adjusted >= -0.3:
            return "中性"
        elif adjusted >= -0.8:
            return "中性偏空"
        else:
            return "偏空"
    
    def _calculate_position_adjustment(self, wukong_data: Dict, factor: Dict) -> str:
        """计算仓位调整建议"""
        # 基础仓位建议
        base_position = "50%"
        
        # 根据悟空情绪
        emotion = wukong_data.get('emotion', '中性')
        if emotion in ['强烈看多', '偏多']:
            base_position = "70%"
        elif emotion in ['偏空', '强烈看空']:
            base_position = "30%"
        elif emotion == '谨慎':
            base_position = "40%"
        
        # 根据事件因子调整
        factor_score = factor['factor_score']
        if factor_score >= 0.7:
            adjustment = "+10%"
        elif factor_score >= 0.5:
            adjustment = "+5%"
        elif factor_score <= 0.3:
            adjustment = "-10%"
        else:
            adjustment = "0%"
        
        return f"{base_position} ({adjustment} 事件因子调整)"
    
    def _merge_key_factors(self, wukong_factors: List, upcoming_events: List) -> List:
        """合并关键因素"""
        merged = wukong_factors.copy()
        
        # 添加即将发生的事件作为关键因素
        for event in upcoming_events[:2]:  # 只添加最近2个
            event_factor = f"【即将发生】{event['title']} ({event['days_until']}天后)"
            if event_factor not in merged:
                merged.insert(0, event_factor)
        
        return merged[:6]  # 最多保留6个


# 便捷函数
def get_event_factor_for_date(date_str: str) -> Dict:
    """
    获取指定日期的事件因子分析
    
    Args:
        date_str: 日期字符串 "2026-05-18"
        
    Returns:
        事件因子分析结果
    """
    analyzer = MonthlyEventsFactor()
    year_month = date_str[:7]
    return analyzer.calculate_event_impact_factor(year_month)


def get_event_strategy_for_date(date_str: str) -> Dict:
    """
    获取指定日期的基于事件的策略建议
    
    Args:
        date_str: 日期字符串
        
    Returns:
        策略建议
    """
    analyzer = MonthlyEventsFactor()
    year_month = date_str[:7]
    return analyzer.generate_event_strategy(year_month)


if __name__ == "__main__":
    # 测试代码
    analyzer = MonthlyEventsFactor()
    
    # 测试5月数据
    test_date = "2026-05-18"
    print(f"\n=== 测试日期: {test_date} ===\n")
    
    factor = analyzer.calculate_event_impact_factor("2026-05")
    print("事件影响因子:")
    print(json.dumps(factor, ensure_ascii=False, indent=2))
    
    print("\n" + "="*50 + "\n")
    
    strategy = analyzer.generate_event_strategy("2026-05")
    print("策略建议:")
    print(json.dumps(strategy, ensure_ascii=False, indent=2))
    
    print("\n" + "="*50 + "\n")
    
    # 测试即将发生的事件
    upcoming = analyzer.get_upcoming_events(7)
    print(f"未来7天内即将发生的事件 ({len(upcoming)}个):")
    for event in upcoming:
        print(f"  - {event['date']} ({event['days_until']}天后): {event['title']}")

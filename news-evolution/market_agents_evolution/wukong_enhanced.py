# -*- coding: utf-8 -*-
"""
悟空经验注入增强 v1

职责：
- 从经验库加载悟空领域的分析经验
- 匹配当前新闻场景
- 自动追加标注（地缘非线性/Trump强度/窗口期/逻辑止损）
- 输出增强后的悟空分析结果

不改变悟空原有的深度分析逻辑，只做「经验标注追加」
"""

import json
import os
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


class WukongEnhanced:
    """悟空经验注入增强"""

    # 地缘事件关键词
    GEO_KEYWORDS = ['战争', '制裁', '冲突', '海峡', '军事', '封锁', '威胁', '通牒',
                    '入侵', '导弹', '军事行动', '霍尔木兹', '台海', '南海', '俄乌']
    # Trump相关关键词
    TRUMP_KEYWORDS = ['Trump', '特朗普', '关税', '禁令', '制裁令', '行政令']
    # 财报相关关键词
    EARNINGS_KEYWORDS = ['业绩', '超预期', '净利润', '营收', '财报', '季报', '年报',
                         '营收增长', '利润增长', '业绩大增']

    def __init__(self, experience_path: str = None):
        if experience_path is None:
            experience_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'data', 'review-experience.json'
            )
        self.experiences = self._load_experiences(experience_path)

    def _load_experiences(self, path: str) -> List[Dict]:
        """加载悟空领域的经验"""
        if not os.path.exists(path):
            return []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                db = json.load(f)
            return [e for e in db.get('wukong_experiences', []) if e.get('active', True)]
        except Exception:
            return []

    def enhance(self, wukong_result: Dict, news_data: Dict = None) -> Dict:
        """
        增强悟空分析结果

        Args:
            wukong_result: 原始悟空分析结果
            news_data: 当日新闻数据（用于场景检测）

        Returns:
            dict: 增强后的悟空结果（添加经验标注+调整建议）
        """
        if not wukong_result:
            return wukong_result

        news_data = news_data or {}
        applied_experiences = []

        # 场景检测
        has_geo = self._detect_geopolitical(wukong_result, news_data)
        trump_intensity = self._detect_trump_intensity(wukong_result, news_data)
        has_earnings = self._detect_earnings(wukong_result, news_data)

        # === WX-001：地缘非线性判断规则 ===
        if has_geo:
            exp = self._find_experience('WX-001')
            if exp:
                wukong_result = self._apply_geo_experience(wukong_result, exp)
                applied_experiences.append('WX-001')

        # === WX-002：Trump喊话强度量化 ===
        if trump_intensity > 0:
            exp = self._find_experience('WX-002')
            if exp:
                wukong_result = self._apply_trump_experience(wukong_result, exp, trump_intensity)
                applied_experiences.append('WX-002')

        # === WX-003：财报季业绩驱动力分级 ===
        if has_earnings:
            exp = self._find_experience('WX-003')
            if exp:
                wukong_result = self._apply_earnings_experience(wukong_result, exp)
                applied_experiences.append('WX-003')

        # 记录已应用的经验
        wukong_result['_experiences_applied'] = applied_experiences
        wukong_result['_scene_tags'] = {
            'has_geopolitical': has_geo,
            'trump_intensity': trump_intensity,
            'has_earnings_news': has_earnings
        }

        return wukong_result

    # ============================================================
    #  场景检测
    # ============================================================

    def _detect_geopolitical(self, wukong_result: Dict, news_data: Dict) -> bool:
        """检测是否有地缘政治事件"""
        # 检查悟空分析结论
        analysis = str(wukong_result.get('core_analysis', ''))
        operations = str(wukong_result.get('operations', ''))
        sentiment = str(wukong_result.get('market_sentiment',
                        wukong_result.get('emotion', '')))

        combined = f'{analysis}{operations}{sentiment}'

        # 检查新闻标题
        news_text = ''
        for key in ['s_news', 'a_news', 'news']:
            items = news_data.get(key, [])
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        news_text += item.get('title', '') + item.get('content', '')
                    elif isinstance(item, str):
                        news_text += item

        all_text = f'{combined}{news_text}'

        return any(kw in all_text for kw in self.GEO_KEYWORDS)

    def _detect_trump_intensity(self, wukong_result: Dict, news_data: Dict) -> int:
        """检测Trump相关新闻强度（0-3）"""
        # 收集所有文本
        all_text = ''
        for key in ['s_news', 'a_news', 'news']:
            items = news_data.get(key, [])
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        all_text += item.get('title', '') + item.get('content', '')
                    elif isinstance(item, str):
                        all_text += item

        # 统计Trump关键词出现次数（不同关键词各计一次）
        trump_hits = sum(1 for kw in self.TRUMP_KEYWORDS if kw in all_text)

        if trump_hits == 0:
            return 0
        elif trump_hits <= 2:
            return 1
        elif trump_hits <= 4:
            return 2
        else:
            return 3

    def _detect_earnings(self, wukong_result: Dict, news_data: Dict) -> bool:
        """检测是否有业绩相关新闻"""
        all_text = ''
        for key in ['s_news', 'a_news', 'news']:
            items = news_data.get(key, [])
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        all_text += item.get('title', '') + item.get('content', '')
                    elif isinstance(item, str):
                        all_text += item

        operations = str(wukong_result.get('operations', ''))
        all_text += operations

        return any(kw in all_text for kw in self.EARNINGS_KEYWORDS)

    # ============================================================
    #  经验应用
    # ============================================================

    def _find_experience(self, exp_id: str) -> Optional[Dict]:
        """按ID查找经验"""
        for exp in self.experiences:
            if exp.get('id') == exp_id:
                return exp
        return None

    def _apply_geo_experience(self, result: Dict, exp: Dict) -> Dict:
        """应用地缘非线性判断规则"""
        adj = exp.get('output_adjustment', {})

        # 追加地缘标注
        existing = result.get('core_analysis', '')
        geo_tag = adj.get('append_tag', '[⚠️ 地缘·非线性格式]')

        if geo_tag not in existing:
            result['core_analysis'] = f'{existing}\n{geo_tag} 窗口期{adj.get("force_window_period", "1-3天")}'

        # 强制添加逻辑止损条件
        if adj.get('force_logic_stop'):
            result['logic_stop_conditions'] = adj.get('logic_stop_conditions', [
                '停火协议达成', '和平声明发布', '海峡开放宣布'
            ])

        # 标记窗口期
        result['window_period'] = adj.get('force_window_period', '1-3天')

        # 标记需要降胜率（由八戒执行，这里只标注）
        result['_geo_win_rate_adjust'] = adj.get('reduce_win_rate', 10)

        return result

    def _apply_trump_experience(self, result: Dict, exp: Dict, intensity: int) -> Dict:
        """应用Trump喊话强度量化"""
        adj = exp.get('output_adjustment', {})
        levels = adj.get('intensity_levels', {})

        level_key = str(intensity)
        level_info = levels.get(level_key, {
            'label': '未知', 'action': '谨慎', 'reversal_prob': 30
        })

        # 追加Trump强度标注
        existing = result.get('core_analysis', '')
        trump_tag = (f'\n[🗣️ Trump强度={intensity}级] '
                     f'{level_info.get("label", "")} '
                     f'反转概率~{level_info.get("reversal_prob", 30)}% '
                     f'建议: {level_info.get("action", "谨慎")}')

        if 'Trump强度' not in existing:
            result['core_analysis'] = f'{existing}{trump_tag}'

        # 标记Trump强度（供白龙马/八戒使用）
        result['trump_intensity'] = intensity
        result['trump_reversal_prob'] = level_info.get('reversal_prob', 30)

        return result

    def _apply_earnings_experience(self, result: Dict, exp: Dict) -> Dict:
        """应用财报季业绩驱动力分级"""
        adj = exp.get('output_adjustment', {})
        levels = adj.get('levels', {})

        # 判断是主线级还是普通利好
        operations = str(result.get('operations', ''))
        core_analysis = str(result.get('core_analysis', ''))

        # 主线级判定：看是否有行业龙头+周期拐点相关描述
        main_level_keywords = ['龙头', '拐点', '周期', '行业共振', '板块联动', '产业趋势']
        is_main_level = any(kw in f'{operations}{core_analysis}' for kw in main_level_keywords)

        level_key = '主线级' if is_main_level else '普通利好'
        level_info = levels.get(level_key, {})

        # 追加分级标注
        existing = result.get('core_analysis', '')
        earnings_tag = f'\n[📊 业绩分级: {level_key}] {level_info.get("criteria", "")}'

        if '业绩分级' not in existing:
            result['core_analysis'] = f'{existing}{earnings_tag}'

        # 标记业绩级别（供八戒使用）
        result['earnings_level'] = level_key
        result['_earnings_win_rate_adjust'] = level_info.get('boost_win_rate', 0)

        return result


def run_wukong_enhanced(wukong_result: Dict, news_data: Dict = None,
                        experience_path: str = None) -> Dict:
    """运行悟空增强"""
    enhancer = WukongEnhanced(experience_path)
    return enhancer.enhance(wukong_result, news_data)


# ============================================================
#  测试
# ============================================================

if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 测试1：地缘事件
    print('=== 测试1：地缘事件场景 ===')
    wk1 = {
        'market_sentiment': '偏多',
        'core_analysis': '伊朗拒绝Trump48小时通牒，局势可能持续升级，油气/黄金维持强势',
        'operations': [{'type': '可做', 'content': '油气ETF'}],
        'emotion': '偏多'
    }
    news1 = {
        's_news': [{'title': '伊朗拒绝Trump通牒 霍尔木兹海峡局势紧张', 'content': '...军事行动...'}]
    }
    result1 = run_wukong_enhanced(wk1, news1)
    print(f"核心分析: {result1['core_analysis'][:100]}...")
    print(f"逻辑止损: {result1.get('logic_stop_conditions', '无')}")
    print(f"窗口期: {result1.get('window_period', '无')}")
    print(f"应用经验: {result1.get('_experiences_applied', [])}")
    print(f"场景标签: {result1.get('_scene_tags', {})}")

    # 测试2：Trump新闻
    print('\n=== 测试2：Trump新闻场景 ===')
    wk2 = {
        'market_sentiment': '谨慎偏多',
        'core_analysis': '科技股受关税威胁影响',
        'operations': [{'type': '可做', 'content': '芯片ETF'}]
    }
    news2 = {
        's_news': [{'title': 'Trump关税制裁', 'content': '特朗普威胁对中国加征关税'}]
    }
    result2 = run_wukong_enhanced(wk2, news2)
    print(f"Trump强度: {result2.get('trump_intensity', 0)}")
    print(f"反转概率: {result2.get('trump_reversal_prob', 0)}%")
    print(f"应用经验: {result2.get('_experiences_applied', [])}")

    # 测试3：财报季
    print('\n=== 测试3：财报季+业绩龙头 ===')
    wk3 = {
        'market_sentiment': '偏多',
        'core_analysis': 'TCL科技业绩超预期，面板行业周期拐点确认',
        'operations': [{'type': '可做', 'content': '面板龙头'}]
    }
    result3 = run_wukong_enhanced(wk3, {})
    print(f"业绩级别: {result3.get('earnings_level', '无')}")
    print(f"应用经验: {result3.get('_experiences_applied', [])}")

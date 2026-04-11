# -*- coding: utf-8 -*-
"""
沙僧经验注入增强 v1

职责：
- 从经验库加载沙僧领域的情绪经验
- FOMO加速度检测→狂热三级提前预警
- 恐慌逆向机会强化标记（质量星级）
- 情绪拐点多因子预判

不改变沙僧原有的情绪计算逻辑，只做「经验标注追加+增强输出」
"""

import json
import os
import re
from typing import Dict, Any, List, Optional


class SangshaEnhanced:
    """沙僧经验注入增强"""

    def __init__(self, experience_path: str = None):
        if experience_path is None:
            experience_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'data', 'review-experience.json'
            )
        self.experiences = self._load_experiences(experience_path)

    def _load_experiences(self, path: str) -> List[Dict]:
        if not os.path.exists(path):
            return []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                db = json.load(f)
            return [e for e in db.get('sangsha_experiences', []) if e.get('active', True)]
        except Exception:
            return []

    def enhance(self, sangsha_result: Dict, news_metadata: Dict = None) -> Dict:
        """
        增强沙僧分析结果

        Args:
            sangsha_result: 原始沙僧分析结果
            news_metadata: 场景元数据

        Returns:
            dict: 增强后的沙僧结果
        """
        if not sangsha_result:
            return sangsha_result

        metadata = news_metadata or {}
        applied_experiences = []

        buy_prob = sangsha_result.get('avg_buy_prob', 50)
        panic_prob = sangsha_result.get('avg_panic_prob', 30)
        sentiment = sangsha_result.get('overall_sentiment', '平稳')

        # === SS-001：狂热提前预警（FOMO加速度检测）===
        fomo_result = self._detect_fomo_acceleration(sangsha_result)
        if fomo_result['detected']:
            exp = self._find_experience('SS-001')
            if exp:
                sangsha_result = self._apply_fomo_warning(sangsha_result, fomo_result, exp)
                applied_experiences.append('SS-001')

        # === SS-002：恐慌逆向机会强化标记 ===
        if panic_prob >= 55:
            exp = self._find_experience('SS-002')
            if exp:
                sangsha_result = self._apply_panic_reverse(sangsha_result, metadata, exp)
                applied_experiences.append('SS-002')

        # === SS-003：情绪拐点预判 ===
        turning_point = self._detect_turning_point(sangsha_result, metadata)
        if turning_point['detected']:
            exp = self._find_experience('SS-003')
            if exp:
                sangsha_result = self._apply_turning_point(sangsha_result, turning_point, exp)
                applied_experiences.append('SS-003')

        sangsha_result['_experiences_applied'] = applied_experiences

        return sangsha_result

    # ============================================================
    #  SS-001：FOMO加速度检测
    # ============================================================

    def _detect_fomo_acceleration(self, result: Dict) -> Dict:
        """检测FOMO加速度"""
        analysis_results = result.get('analysis_results', [])

        # 提取近几天的买入概率序列
        buy_probs = []
        for ar in analysis_results:
            if isinstance(ar, dict):
                bp = ar.get('buy_prob', ar.get('买入概率', 0))
                try:
                    buy_probs.append(int(bp))
                except (ValueError, TypeError):
                    pass

        if len(buy_probs) < 2:
            # 无法计算加速度时，用绝对值判断
            current_buy = result.get('avg_buy_prob', 50)
            if current_buy >= 75:
                return {
                    'detected': True,
                    'level': '已狂热',
                    'acceleration': 0,
                    'current_buy_prob': current_buy
                }
            return {'detected': False, 'level': '', 'acceleration': 0, 'current_buy_prob': current_buy}

        # 计算加速度（买入概率变化速度）
        if len(buy_probs) >= 2:
            recent_change = buy_probs[-1] - buy_probs[-2] if len(buy_probs) >= 2 else 0
        else:
            recent_change = 0

        current_buy = buy_probs[-1] if buy_probs else 50

        # 三级预警
        if current_buy >= 80 and recent_change > 0:
            return {
                'detected': True,
                'level': '已狂热',
                'acceleration': recent_change,
                'current_buy_prob': current_buy
            }
        elif current_buy >= 70 or (current_buy >= 60 and recent_change >= 10):
            return {
                'detected': True,
                'level': '接近狂热',
                'acceleration': recent_change,
                'current_buy_prob': current_buy
            }
        elif current_buy >= 55 and recent_change >= 8:
            return {
                'detected': True,
                'level': '升温中',
                'acceleration': recent_change,
                'current_buy_prob': current_buy
            }

        return {'detected': False, 'level': '', 'acceleration': recent_change, 'current_buy_prob': current_buy}

    def _apply_fomo_warning(self, result: Dict, fomo: Dict, exp: Dict) -> Dict:
        """应用狂热提前预警"""
        level = fomo['level']
        acc = fomo['acceleration']
        buy = fomo['current_buy_prob']

        # 降级情绪（提前预警时把情绪评级降低一级）
        adj = exp.get('output_adjustment', {})
        if adj.get('downgrade_sentiment_on_warning'):
            current = result.get('overall_sentiment', '平稳')
            downgrade_map = {
                '狂热': '偏热',
                '积极': '偏热',
                '偏热': '升温中',
            }
            # 如果是提前预警（升温中/接近狂热），当前情绪还不到狂热
            if level == '升温中' and current not in ['狂热', '偏热']:
                result['original_sentiment'] = current
                result['overall_sentiment'] = '偏热'
            elif level == '接近狂热' and current != '狂热':
                result['original_sentiment'] = current
                result['overall_sentiment'] = '偏热'

        # 追加FOMO预警标注
        existing_advice = result.get('advice', '')
        fomo_note = f'\n[🔥 FOMO预警: {level}] 买入概率{buy}% 加速度+{acc}%/日'
        result['advice'] = f'{existing_advice}{fomo_note}'
        result['fomo_warning'] = {
            'level': level,
            'acceleration': acc,
            'current_buy_prob': buy
        }

        return result

    # ============================================================
    #  SS-002：恐慌逆向机会强化
    # ============================================================

    def _apply_panic_reverse(self, result: Dict, metadata: Dict, exp: Dict) -> Dict:
        """应用恐慌逆向机会标记"""
        panic_prob = result.get('avg_panic_prob', 0)

        # 评估逆向机会质量
        quality = self._assess_reverse_quality(result, metadata)
        stars = quality['stars']
        quality_desc = quality['description']

        # 追加逆向机会标注
        existing_advice = result.get('advice', '')
        reverse_note = f'\n[📌 逆向机会] 恐慌概率{panic_prob}% 质量{"★" * stars}{"☆" * (5 - stars)} {quality_desc}'
        result['advice'] = f'{existing_advice}{reverse_note}'

        result['reverse_opportunity'] = {
            'detected': True,
            'quality_stars': stars,
            'quality_description': quality_desc,
            'panic_prob': panic_prob,
            'reverse_layout_advice': quality.get('advice', '')
        }

        return result

    def _assess_reverse_quality(self, result: Dict, metadata: Dict) -> Dict:
        """评估逆向机会质量（1-5星）"""
        panic_prob = result.get('avg_panic_prob', 0)
        has_negative_news = metadata.get('has_negative_catalyst', False)
        has_landed_bad_news = metadata.get('bad_news_landed', False)
        market_dropped = metadata.get('market_dropped_pct', 0)

        if has_landed_bad_news and market_dropped > 5:
            return {
                'stars': 5,
                'description': '极佳逆向点（利空出尽+已深跌）',
                'advice': '利空落地+深跌，反弹概率极高，可大胆逆向布局优质标的'
            }
        elif market_dropped > 5:
            return {
                'stars': 4,
                'description': '高质量逆向点（已深跌）',
                'advice': '市场已充分反应恐慌，可分批逆向布局'
            }
        elif has_landed_bad_news:
            return {
                'stars': 4,
                'description': '高质量逆向点（利空出尽）',
                'advice': '利空已落地，恐慌情绪将逐步消退'
            }
        elif not has_negative_news:
            return {
                'stars': 3,
                'description': '中等逆向点（情绪性恐慌）',
                'advice': '恐慌无明显利空驱动，可能是情绪过度反应'
            }
        else:
            return {
                'stars': 2,
                'description': '风险仍大（利空未落地）',
                'advice': '还有未落地利空，建议观望等待利空出尽'
            }

    # ============================================================
    #  SS-003：情绪拐点预判
    # ============================================================

    def _detect_turning_point(self, result: Dict, metadata: Dict) -> Dict:
        """多因子检测情绪拐点"""
        factors = []
        buy_prob = result.get('avg_buy_prob', 50)
        panic_prob = result.get('avg_panic_prob', 30)

        # 因子1：情绪极值偏离
        if buy_prob > 80 or buy_prob < 20:
            factors.append('情绪极值偏离')
        if panic_prob > 70 or panic_prob < 15:
            factors.append('恐慌极值偏离')

        # 因子2：动量衰竭（通过加速度判断）
        fomo = self._detect_fomo_acceleration(result)
        if 0 < fomo.get('acceleration', 0) < 5 and buy_prob > 60:
            factors.append('动量衰竭')

        # 因子3：外部催化剂
        if metadata.get('has_catalyst_event'):
            factors.append('外部催化剂')

        # 因子4：时间节点
        if metadata.get('is_near_weekend') or metadata.get('is_near_holiday'):
            factors.append('时间节点')

        threshold = 2  # >=2个因子触发
        detected = len(factors) >= threshold

        return {
            'detected': detected,
            'factors': factors,
            'factor_count': len(factors)
        }

    def _apply_turning_point(self, result: Dict, tp: Dict, exp: Dict) -> Dict:
        """应用拐点预判"""
        factors = tp['factors']
        count = tp['factor_count']

        existing_advice = result.get('advice', '')
        tp_note = f'\n[🔄 拐点预警] {count}个因子触发，情绪拐点可能在1-2天内出现 | 因子: {", ".join(factors)}'
        result['advice'] = f'{existing_advice}{tp_note}'

        result['turning_point_warning'] = {
            'detected': True,
            'factors': factors,
            'factor_count': count,
            'prediction': '1-2天内可能出现情绪拐点'
        }

        return result

    # ============================================================
    #  辅助
    # ============================================================

    def _find_experience(self, exp_id: str) -> Optional[Dict]:
        for exp in self.experiences:
            if exp.get('id') == exp_id:
                return exp
        return None


def run_sangsha_enhanced(sangsha_result: Dict, news_metadata: Dict = None,
                         experience_path: str = None) -> Dict:
    """运行沙僧增强"""
    enhancer = SangshaEnhanced(experience_path)
    return enhancer.enhance(sangsha_result, news_metadata)


if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 测试1：狂热FOMO检测
    print('=== 测试1：FOMO狂热预警 ===')
    sg1 = {
        'overall_sentiment': '积极',
        'avg_buy_prob': 68,
        'avg_panic_prob': 15,
        'advice': '散户情绪偏积极',
        'analysis_results': [
            {'buy_prob': 55, 'date': '04-07'},
            {'buy_prob': 62, 'date': '04-08'},
            {'buy_prob': 68, 'date': '04-09'},
        ]
    }
    r1 = run_sangsha_enhanced(sg1)
    print(f"情绪: {r1.get('overall_sentiment')}")
    print(f"FOMO: {r1.get('fomo_warning', {})}")
    print(f"应用经验: {r1.get('_experiences_applied', [])}")

    # 测试2：恐慌逆向
    print('\n=== 测试2：恐慌逆向机会 ===')
    sg2 = {
        'overall_sentiment': '恐慌',
        'avg_buy_prob': 25,
        'avg_panic_prob': 60,
        'advice': '散户恐慌出逃',
        'analysis_results': []
    }
    r2 = run_sangsha_enhanced(sg2, {'bad_news_landed': True, 'market_dropped_pct': 6})
    print(f"逆向: {r2.get('reverse_opportunity', {})}")
    print(f"应用经验: {r2.get('_experiences_applied', [])}")

    # 测试3：拐点预判
    print('\n=== 测试3：拐点预判 ===')
    sg3 = {
        'overall_sentiment': '狂热',
        'avg_buy_prob': 85,
        'avg_panic_prob': 10,
        'advice': '散户疯狂追高',
        'analysis_results': [{'buy_prob': 84}, {'buy_prob': 85}]
    }
    r3 = run_sangsha_enhanced(sg3, {'is_near_weekend': True, 'has_catalyst_event': True})
    print(f"拐点: {r3.get('turning_point_warning', {})}")
    print(f"应用经验: {r3.get('_experiences_applied', [])}")

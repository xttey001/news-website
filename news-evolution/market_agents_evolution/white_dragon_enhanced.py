# -*- coding: utf-8 -*-
"""
白龙马经验注入增强 v1

职责：
- 从经验库加载白龙马领域的主力行为经验
- WD-001：Trump喊话-主力行为四象限关联模式
- WD-002：出货 vs 洗盘精分辨（四维度打分）
- WD-003：量价背离三级分类

不改变白龙马原有的K线量价计算逻辑，只做「经验标注追加+状态修正」
"""

import json
import os
import re
from typing import Dict, Any, List, Optional


class WhiteDragonEnhanced:
    """白龙马经验注入增强"""

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
            return [e for e in db.get('white_dragon_experiences', []) if e.get('active', True)]
        except Exception:
            return []

    def enhance(self, white_dragon_result: Dict, sangsha_result: Dict = None,
                news_metadata: Dict = None) -> Dict:
        """
        增强白龙马分析结果

        Args:
            white_dragon_result: 原始白龙马分析结果
            sangsha_result: 沙僧结果（用于出货vs洗盘四维验证）
            news_metadata: 场景元数据（含trump_intensity等）

        Returns:
            dict: 增强后的白龙马结果
        """
        if not white_dragon_result:
            return white_dragon_result

        metadata = news_metadata or {}
        applied_experiences = []

        state = white_dragon_result.get('主力状态', '观望')

        # === WD-001：Trump喊话-主力行为关联模式 ===
        trump_level = metadata.get('trump_intensity', 0)
        if trump_level >= 2:
            exp = self._find_experience('WD-001')
            if exp:
                white_dragon_result = self._apply_trump_pattern(white_dragon_result, metadata, exp)
                applied_experiences.append('WD-001')

        # === WD-002：出货 vs 洗盘精分辨 ===
        if state in ('出货', '洗盘'):
            exp = self._find_experience('WD-002')
            if exp:
                white_dragon_result = self._apply_wash_or_sell(
                    white_dragon_result, sangsha_result, exp
                )
                applied_experiences.append('WD-002')

        # === WD-003：量价背离三级分类 ===
        if self._has_divergence(white_dragon_result):
            exp = self._find_experience('WD-003')
            if exp:
                white_dragon_result = self._apply_divergence_grading(white_dragon_result, exp)
                applied_experiences.append('WD-003')

        white_dragon_result['_experiences_applied'] = applied_experiences

        return white_dragon_result

    # ============================================================
    #  WD-001：Trump喊话-主力行为四象限关联模式
    # ============================================================

    # Trump关联模式表
    TRUMP_PATTERNS = {
        # (Trump动作, 价格位置) → (主力真实意图, 可信度)
        ('喊多', '高位'): {'intent': '出货派发', 'credibility': 0.85,
                         'desc': 'Trump喊多+高位=主力借利好派发筹码给跟风散户'},
        ('喊多', '低位'): {'intent': '试探性拉升', 'credibility': 0.60,
                         'desc': 'Trump喊多+低位=主力试探拉升，需观察后续量能'},
        ('喊空', '高位'): {'intent': '打压出货', 'credibility': 0.70,
                         'desc': 'Trump喊空+高位=打压出货，高位震荡中派发'},
        ('喊空', '低位'): {'intent': '打压吸筹', 'credibility': 0.90,
                         'desc': 'Trump喊空+低位=主力借利空打压价格捡筹码'},
    }

    def _apply_trump_pattern(self, result: Dict, metadata: Dict, exp: Dict) -> Dict:
        """应用Trump-主力关联模式"""
        trump_action = metadata.get('trump_action', '喊多')  # 喊多/喊空
        price_position = metadata.get('price_position', '中性')  # 高位/低位/中性

        # 只有在高位或低位时才触发关联模式
        if price_position not in ('高位', '低位'):
            # 中性位置不触发四象限
            result['trump_correlation'] = {
                'detected': True,
                'action': trump_action,
                'position': price_position,
                'pattern': '中性位置不触发',
                'note': f'Trump强度={metadata.get("trump_intensity",0)}但价格位置中性'
            }
            return result

        key = (trump_action, price_position)
        pattern = self.TRUMP_PATTERNS.get(key)

        if pattern:
            original_state = result.get('主力状态', '观望')
            original_cred = result.get('可信度', 1.0)

            # 如果关联模式判断与原始判断不同，覆盖主力状态
            override = False
            if pattern['credibility'] > original_cred:
                result['主力状态'] = f"🚨 {pattern['intent']}（Trump关联模式）"
                result['可信度'] = pattern['credibility']
                result['original_state'] = original_state
                override = True

            result['trump_correlation'] = {
                'detected': True,
                'trump_action': trump_action,
                'price_position': price_position,
                'pattern': pattern['desc'],
                'intent': pattern['intent'],
                'credibility': pattern['credibility'],
                'overrode_original': override,
                'original_state': original_state
            }

            # 追加到综合建议
            existing_advice = result.get('综合建议', '')
            trump_note = f' [Trump关联: {trump_action}+{price_position}→{pattern["intent"]}({int(pattern["credibility"]*100)}%)]'
            result['综合建议'] = f'{existing_advice}{trump_note}'

        return result

    # ============================================================
    #  WD-002：出货 vs 洗盘精分辨（四维度打分）
    # ============================================================

    def _apply_wash_or_sell(self, result: Dict, sangsha: Dict, exp: Dict) -> Dict:
        """应用出货vs洗盘四维度验证"""
        scores = {
            '量能': self._score_volume(result),
            'K线': self._score_kline(result),
            '周期': self._score_period(result),
            '散户配合': self._score_retail(result, sangsha)
        }

        # 出货得分（每个维度0-2分，越高越像出货）
        total_sell_score = sum(scores.values())
        max_score = 8  # 4维度×2分

        # 根据总分判定
        if total_sell_score >= 6:
            final_judgment = '出货'
            confidence = 0.85
        elif total_sell_score <= 3:
            final_judgment = '洗盘'
            confidence = 0.80
        else:
            final_judgment = '待观察'
            confidence = 0.55

        original_state = result.get('主力状态', '观望')

        # 如果判定与原始不同
        if final_judgment != original_state and final_judgment != '待观察':
            # 只在可信度高时覆盖
            if confidence > result.get('可信度', 0.5):
                result['主力状态'] = f"{final_judgment}（四维验证修正）"
                result['original_state'] = original_state

        # 置信度低于70%时标记待观察
        if confidence < 0.70 and final_judgment != '待观察':
            result['主力状态'] = f"{final_judgment}⚠️（可信度偏低，待观察）"

        result['wash_sell_analysis'] = {
            'original_state': original_state,
            'scores': scores,
            'total_sell_score': total_sell_score,
            'max_score': max_score,
            'final_judgment': final_judgment,
            'confidence': confidence,
            'detail': self._explain_wash_sell(scores, final_judgment)
        }

        return result

    def _score_volume(self, result: Dict) -> int:
        """量能维度打分（0=洗盘, 1=中性, 2=出货）"""
        vol_info = result.get('量能分析', '')
        vol_str = str(vol_info) + str(result.get('综合建议', ''))

        if '放量' in vol_str and '缩量' not in vol_str:
            return 2  # 放量→出货特征
        elif '缩量' in vol_str:
            return 0  # 缩量→洗盘特征
        else:
            return 1  # 中性

    def _score_kline(self, result: Dict) -> int:
        """K线维度打分"""
        kline_info = str(result.get('K线分析', '')) + str(result.get('综合建议', ''))
        phase = str(result.get('阶段', ''))

        if '上影线' in kline_info or '走低' in kline_info:
            return 2  # 上影线+收盘走低→出货
        elif '下影线' in kline_info or '支撑' in kline_info:
            return 0  # 下影线+支撑稳→洗盘
        elif '洗盘' in phase:
            return 0
        elif '出货' in phase:
            return 2
        else:
            return 1

    def _score_period(self, result: Dict) -> int:
        """周期维度打分"""
        # 短促剧烈→洗盘，持续缓慢→出货
        # 目前没有直接的时间数据，用阶段信息推断
        phase = str(result.get('阶段', ''))
        if '洗盘' in phase:
            return 0
        elif '出货' in phase or '派发' in phase:
            return 2
        else:
            return 1

    def _score_retail(self, result: Dict, sangsha: Dict) -> int:
        """散户配合维度打分"""
        if not sangsha:
            return 1  # 无数据，中性

        sentiment = sangsha.get('overall_sentiment', '平稳')
        buy_prob = sangsha.get('avg_buy_prob', 50)

        # 出货需要有人接盘（散户乐观）
        if sentiment in ('积极', '狂热') or buy_prob > 65:
            return 2  # 散户在买→出货有人接
        elif sentiment in ('恐慌',) or buy_prob < 35:
            return 0  # 散户在卖→洗盘交筹码
        else:
            return 1

    def _explain_wash_sell(self, scores: Dict, judgment: str) -> str:
        """生成四维度验证说明"""
        parts = []
        label_map = {0: '✅符合洗盘', 1: '⚠️中性', 2: '🔴符合出货'}
        for dim, score in scores.items():
            parts.append(f'{dim}: {label_map.get(score, "?")}({score}/2)')
        return f'四维验证→{judgment} | ' + ' | '.join(parts)

    # ============================================================
    #  WD-003：量价背离三级分类
    # ============================================================

    def _has_divergence(self, result: Dict) -> bool:
        """检测是否存在量价背离信号"""
        text = str(result)
        return '背离' in text or '量缩' in text or '缩量' in text

    def _apply_divergence_grading(self, result: Dict, exp: Dict) -> Dict:
        """应用量价背离三级分类"""
        # 从结果中提取量价信息
        vol_info = str(result.get('量能分析', ''))
        price_info = str(result.get('价格分析', ''))
        combined = vol_info + price_info + str(result.get('综合建议', ''))

        # 判断背离等级
        if '极端' in combined or ('巨量' in combined and '上影线' in combined):
            grade = 3
            grade_name = '三级·极端背离'
            action = '减仓或清仓'
            desc = '趋势大概率反转'
        elif '缩量' in combined or ('量缩' in combined and '涨' in combined):
            # 进一步区分
            if '明显' in combined or '均量线' in combined:
                grade = 2
                grade_name = '二级·中度背离'
                action = '不减仓不加仓，设好止盈'
                desc = '上涨动能衰减，可能回调'
            else:
                grade = 1
                grade_name = '一级·温和背离'
                action = '继续持有，密切观察'
                desc = '多头力量减弱但仍占优'
        elif '连涨' in combined or '递减' in combined:
            grade = 2
            grade_name = '二级·中度背离'
            action = '不减仓不加仓，设好止盈'
            desc = '连涨但量递减，动能衰减'
        else:
            grade = 1
            grade_name = '一级·温和背离'
            action = '继续持有，密切观察'
            desc = '轻度量价不匹配'

        result['divergence_grade'] = {
            'grade': grade,
            'name': grade_name,
            'action': action,
            'description': desc
        }

        # 追加到综合建议
        existing = result.get('综合建议', '')
        div_note = f' [量价背离: {grade_name}→{action}]'
        result['综合建议'] = f'{existing}{div_note}'

        return result

    # ============================================================
    #  辅助
    # ============================================================

    def _find_experience(self, exp_id: str) -> Optional[Dict]:
        for exp in self.experiences:
            if exp.get('id') == exp_id:
                return exp
        return None


def run_white_dragon_enhanced(white_dragon_result: Dict, sangsha_result: Dict = None,
                               news_metadata: Dict = None, experience_path: str = None) -> Dict:
    """运行白龙马增强"""
    enhancer = WhiteDragonEnhanced(experience_path)
    return enhancer.enhance(white_dragon_result, sangsha_result, news_metadata)


if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 测试1：Trump关联模式 — 喊多+高位=出货派发
    print('=== 测试1：Trump关联模式 ===')
    wd1 = {
        '主力状态': '拉升',
        '可信度': 0.72,
        '综合建议': '主力在拉升阶段',
        '阶段': '拉升'
    }
    r1 = run_white_dragon_enhanced(wd1, news_metadata={
        'trump_intensity': 3, 'trump_action': '喊多', 'price_position': '高位'
    })
    print(f"状态: {r1.get('主力状态')}")
    print(f"Trump关联: {r1.get('trump_correlation', {}).get('intent', '无')}")
    print(f"经验: {r1.get('_experiences_applied', [])}")

    # 测试2：出货vs洗盘四维验证
    print('\n=== 测试2：出货vs洗盘验证 ===')
    wd2 = {
        '主力状态': '出货',
        '可信度': 0.65,
        '综合建议': '放量上影线，疑似出货',
        '量能分析': '放量1.8倍',
        'K线分析': '连续上影线',
        '阶段': '出货'
    }
    sangsha2 = {'overall_sentiment': '积极', 'avg_buy_prob': 68}
    r2 = run_white_dragon_enhanced(wd2, sangsha2)
    ws = r2.get('wash_sell_analysis', {})
    print(f"四维得分: {ws.get('total_sell_score')}/{ws.get('max_score')}")
    print(f"判定: {ws.get('final_judgment')} (置信{ws.get('confidence')})")
    print(f"明细: {ws.get('detail')}")
    print(f"经验: {r2.get('_experiences_applied', [])}")

    # 测试3：量价背离三级分类
    print('\n=== 测试3：量价背离 ===')
    wd3 = {
        '主力状态': '观望',
        '可信度': 0.80,
        '综合建议': '价格连涨但量明显缩量',
        '量能分析': '缩量至均量线下'
    }
    r3 = run_white_dragon_enhanced(wd3)
    dg = r3.get('divergence_grade', {})
    print(f"等级: {dg.get('name')}")
    print(f"操作: {dg.get('action')}")
    print(f"经验: {r3.get('_experiences_applied', [])}")

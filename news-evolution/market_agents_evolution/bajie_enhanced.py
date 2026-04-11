# -*- coding: utf-8 -*-
"""
八戒概率校准增强 v1

职责：
- BJ-001：历史同类场景先验概率库（替代默认50%拍脑袋）
- BJ-002：信号权重动态校准（根据近期准确率调整各信号源权重）
- BJ-003：地缘类先验12小时有效期规则

不改变八戒原有的贝叶斯融合逻辑，只做「先验校准+权重调整+有效期检查」
"""

import json
import os
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


class BajieEnhanced:
    """八戒概率校准增强"""

    # BJ-001：历史同类场景基准先验概率
    SCENE_PRIORS = {
        'geopolitical_sudden':    {'prior': 55, 'desc': '地缘突发事件做多', 'note': '方向对但时机难把握'},
        'earnings_beat':          {'prior': 72, 'desc': '业绩超预期做多', 'note': '财报季最高胜率场景'},
        'trump_reverse':          {'prior': 68, 'desc': 'Trump喊话反向操作', 'note': '逆向思维胜率较高'},
        'policy_benefit':         {'prior': 62, 'desc': '政策利好做多', 'note': '取决于政策力度'},
        'tech_breakthrough':      {'prior': 65, 'desc': '行业龙头技术突破', 'note': '需看产业化进度'},
        'panic_reverse':          {'prior': 61, 'desc': '散户恐慌逆向做多', 'note': '逆向但需选对标的'},
        'pre_holiday_hold':       {'prior': 45, 'desc': '节假日前夕持仓', 'note': '信息不对称风险大'},
        'default':                {'prior': 50, 'desc': '默认先验', 'note': '无特定场景匹配'},
    }

    # BJ-002：各信号源基础权重和动态校准规则
    SIGNAL_WEIGHTS = {
        'wukong':     {'base': 1.0, 'boost_conditions': [('accuracy_rate', '>', 0.80, 1.2)],
                       'label': '悟空深度分析'},
        'sangsha':    {'base': 0.8, 'boost_conditions': [('sentiment', 'in', ['狂热', '恐慌'], 1.1)],
                       'label': '沙僧情绪'},
        'white_dragon': {'base': 0.9, 'boost_conditions': [('credibility', '>', 0.85, 1.2)],
                         'label': '白龙马主力'},
        'overseas':   {'base': 1.1, 'boost_conditions': [('is_holiday_period', '==', True, 1.3)],
                       'label': '外盘先行指标'},
    }

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
            return [e for e in db.get('bajie_experiences', []) if e.get('active', True)]
        except Exception:
            return []

    def enhance(self, bajie_result: Dict, news_metadata: Dict = None,
                sangsha_result: Dict = None, white_dragon_result: Dict = None,
                wukong_result: Dict = None) -> Dict:
        """
        增强八戒融合结果

        Args:
            bajie_result: 原始八戒融合结果
            news_metadata: 场景元数据
            sangsha_result: 沙僧结果（用于权重校准）
            white_dragon_result: 白龙马结果（用于权重校准）
            wukong_result: 悟空结果（用于权重校准）

        Returns:
            dict: 增强后的八戒结果
        """
        if not bajie_result:
            return bajie_result

        metadata = news_metadata or {}
        applied_experiences = []

        # === BJ-001：历史先验概率库 ===
        exp = self._find_experience('BJ-001')
        if exp:
            bajie_result = self._apply_scene_prior(bajie_result, metadata, exp)
            applied_experiences.append('BJ-001')

        # === BJ-002：信号权重动态校准 ===
        exp = self._find_experience('BJ-002')
        if exp:
            bajie_result = self._apply_signal_weights(
                bajie_result, metadata, sangsha_result,
                white_dragon_result, wukong_result, exp
            )
            applied_experiences.append('BJ-002')

        # === BJ-003：地缘先验有效期检查 ===
        if metadata.get('prior_type') == 'geopolitical' or metadata.get('has_geopolitical'):
            exp = self._find_experience('BJ-003')
            if exp:
                bajie_result = self._apply_geo_prior_expiry(bajie_result, metadata, exp)
                applied_experiences.append('BJ-003')

        bajie_result['_experiences_applied'] = applied_experiences

        return bajie_result

    # ============================================================
    #  BJ-001：历史同类场景先验概率库
    # ============================================================

    def _detect_scene_type(self, metadata: Dict) -> str:
        """检测当前场景类型"""
        if metadata.get('has_geopolitical'):
            return 'geopolitical_sudden'
        if metadata.get('has_earnings_beat'):
            return 'earnings_beat'
        if metadata.get('trump_intensity', 0) >= 2:
            return 'trump_reverse'
        if metadata.get('has_policy_benefit'):
            return 'policy_benefit'
        if metadata.get('has_tech_breakthrough'):
            return 'tech_breakthrough'
        if metadata.get('is_panic_reverse'):
            return 'panic_reverse'
        if metadata.get('is_near_holiday'):
            return 'pre_holiday_hold'
        return 'default'

    def _apply_scene_prior(self, result: Dict, metadata: Dict, exp: Dict) -> Dict:
        """应用场景先验概率"""
        scene_type = self._detect_scene_type(metadata)
        scene = self.SCENE_PRIORS.get(scene_type, self.SCENE_PRIORS['default'])

        # 提取当前胜率
        current_wr = self._extract_win_rate(result.get('win_rate', '50%'))

        # 如果当前胜率接近默认50%，用场景先验替代
        if 45 <= current_wr <= 55 and scene['prior'] != 50:
            old_wr = current_wr
            new_wr = scene['prior']
            result['win_rate'] = f'~{new_wr}%（BJ校准：{scene["desc"]}，基准先验{scene["prior"]}%）'
            result['prior_calibration'] = {
                'scene_type': scene_type,
                'scene_desc': scene['desc'],
                'original_prior': old_wr,
                'calibrated_prior': new_wr,
                'note': scene['note']
            }
        else:
            # 不替代但记录
            result['prior_calibration'] = {
                'scene_type': scene_type,
                'scene_desc': scene['desc'],
                'original_prior': current_wr,
                'calibrated_prior': current_wr,
                'note': f'当前胜率{current_wr}%已偏离默认值，不替代（{scene["note"]}）'
            }

        return result

    # ============================================================
    #  BJ-002：信号权重动态校准
    # ============================================================

    def _apply_signal_weights(self, result: Dict, metadata: Dict,
                              sangsha: Dict, white_dragon: Dict,
                              wukong: Dict, exp: Dict) -> Dict:
        """应用信号权重动态校准"""
        weights = {}

        # 悟空权重
        wk_weight = self.SIGNAL_WEIGHTS['wukong']['base']
        wk_label = self.SIGNAL_WEIGHTS['wukong']['label']
        # 简化：如果悟空有S级分析，加权
        if wukong and wukong.get('has_s_level'):
            wk_weight *= 1.2
        weights[wk_label] = round(wk_weight, 2)

        # 沙僧权重
        sg_weight = self.SIGNAL_WEIGHTS['sangsha']['base']
        sg_label = self.SIGNAL_WEIGHTS['sangsha']['label']
        if sangsha:
            sentiment = sangsha.get('overall_sentiment', '平稳')
            if sentiment in ('狂热', '恐慌'):
                sg_weight *= 1.1
        weights[sg_label] = round(sg_weight, 2)

        # 白龙马权重
        wd_weight = self.SIGNAL_WEIGHTS['white_dragon']['base']
        wd_label = self.SIGNAL_WEIGHTS['white_dragon']['label']
        if white_dragon:
            cred = white_dragon.get('可信度', 1.0)
            if isinstance(cred, (int, float)) and cred > 0.85:
                wd_weight *= 1.2
        weights[wd_label] = round(wd_weight, 2)

        # 外盘权重
        os_weight = self.SIGNAL_WEIGHTS['overseas']['base']
        os_label = self.SIGNAL_WEIGHTS['overseas']['label']
        if metadata.get('is_holiday_period'):
            os_weight *= 1.3
        weights[os_label] = round(os_weight, 2)

        # 特殊调整规则
        special_notes = []

        # 规则1：沙僧狂热 + 白龙马非出货 → 听白龙马的
        if sangsha and white_dragon:
            sg_sent = sangsha.get('overall_sentiment', '平稳')
            wd_state = str(white_dragon.get('主力状态', '观望'))
            if sg_sent == '狂热' and '出货' not in wd_state:
                weights[sg_label] = round(weights[sg_label] * 0.7, 2)
                weights[wd_label] = round(weights[wd_label] * 1.3, 2)
                special_notes.append('沙僧狂热+白龙马非出货→听白龙马（沙僧降权0.7，白龙马加权1.3）')

        # 规则2：沙僧恐慌 + 白龙马吸筹 → 强烈逆向
        if sangsha and white_dragon:
            sg_sent = sangsha.get('overall_sentiment', '平稳')
            wd_state = str(white_dragon.get('主力状态', '观望'))
            if sg_sent == '恐慌' and '吸筹' in wd_state:
                weights[sg_label] = round(weights[sg_label] * 1.4, 2)
                weights[wd_label] = round(weights[wd_label] * 1.4, 2)
                special_notes.append('沙僧恐慌+白龙马吸筹→超级逆向信号（双加权1.4）')

        # 规则3：悟空与白龙马矛盾 → 降低整体置信度
        if wukong and white_dragon:
            wk_sent = str(wukong.get('market_sentiment', wukong.get('emotion', '')))
            wd_state = str(white_dragon.get('主力状态', ''))
            # 简化矛盾判断
            if ('偏多' in wk_sent or '看多' in wk_sent) and ('出货' in wd_state):
                for k in weights:
                    weights[k] = round(weights[k] * 0.8, 2)
                special_notes.append('悟空偏多+白龙马出货→信号矛盾，整体降权0.8')

        result['signal_weights'] = weights
        result['signal_weight_notes'] = special_notes

        return result

    # ============================================================
    #  BJ-003：地缘先验有效期规则
    # ============================================================

    def _apply_geo_prior_expiry(self, result: Dict, metadata: Dict, exp: Dict) -> Dict:
        """应用地缘先验有效期检查"""
        now = datetime.now()

        # 检查先验最后更新时间
        prior_updated_at = metadata.get('prior_updated_at')
        if prior_updated_at:
            try:
                last_update = datetime.fromisoformat(str(prior_updated_at))
                hours_since = (now - last_update).total_seconds() / 3600
            except (ValueError, TypeError):
                hours_since = 999  # 无法解析则视为过期
        else:
            hours_since = 999  # 无记录则视为过期

        # 地缘先验有效期12小时
        is_expired = hours_since > 12
        needs_review = hours_since > 6

        geo_check = {
            'prior_type': 'geopolitical',
            'hours_since_last_update': round(hours_since, 1),
            'is_expired': is_expired,
            'needs_review': needs_review,
            'validity_hours': 12,
            'review_interval_hours': 6
        }

        if is_expired:
            # 过期时降级胜率
            current_wr = self._extract_win_rate(result.get('win_rate', '50%'))
            if current_wr > 50:
                penalty = min(15, current_wr - 50)  # 降级幅度不超过偏离50的部分
                new_wr = max(50, current_wr - penalty)
                result['win_rate'] = f'~{new_wr}%（⚠️地缘先验已过期{round(hours_since)}h，自动降级）'
                geo_check['penalty_applied'] = penalty

            # 强制添加逻辑止损
            if not result.get('logic_stop_conditions'):
                result['logic_stop_conditions'] = [
                    '停火协议达成', '关键人物发表和平声明',
                    '海峡/通道宣布重新开放', '先验概率超过12小时未更新'
                ]
                geo_check['logic_stop_added'] = True

        if needs_review and not is_expired:
            # 需要重评但未过期
            existing_wr = result.get('win_rate', '')
            if 'BJ校准' in existing_wr and '需重评' not in existing_wr:
                result['win_rate'] = existing_wr.replace('）', '，⚠️需6h重评）')
            geo_check['review_note'] = '地缘先验已超过6小时，建议重评'

        result['geo_prior_check'] = geo_check

        return result

    # ============================================================
    #  辅助
    # ============================================================

    def _extract_win_rate(self, wr_str) -> int:
        """从胜率字符串提取数字"""
        if isinstance(wr_str, (int, float)):
            return int(wr_str)
        m = re.search(r'(\d+)', str(wr_str))
        return int(m.group(1)) if m else 50

    def _find_experience(self, exp_id: str) -> Optional[Dict]:
        for exp in self.experiences:
            if exp.get('id') == exp_id:
                return exp
        return None


def run_bajie_enhanced(bajie_result: Dict, news_metadata: Dict = None,
                       sangsha_result: Dict = None, white_dragon_result: Dict = None,
                       wukong_result: Dict = None, experience_path: str = None) -> Dict:
    """运行八戒校准增强"""
    enhancer = BajieEnhanced(experience_path)
    return enhancer.enhance(bajie_result, news_metadata,
                            sangsha_result, white_dragon_result, wukong_result)


if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 测试1：场景先验概率库 — 地缘事件
    print('=== 测试1：场景先验概率 ===')
    bj1 = {'win_rate': '~50%', 'optimal_action': '观望', 'optimal_etfs': ''}
    r1 = run_bajie_enhanced(bj1, news_metadata={'has_geopolitical': True})
    pc = r1.get('prior_calibration', {})
    print(f"场景: {pc.get('scene_desc')}")
    print(f"先验: {pc.get('original_prior')}→{pc.get('calibrated_prior')}")
    print(f"胜率: {r1.get('win_rate')}")
    print(f"经验: {r1.get('_experiences_applied', [])}")

    # 测试2：信号权重校准 — 沙僧恐慌+白龙马吸筹=超级逆向
    print('\n=== 测试2：信号权重（恐慌+吸筹=逆向）===')
    bj2 = {'win_rate': '~55%', 'optimal_action': '轻仓', 'optimal_etfs': ''}
    sg2 = {'overall_sentiment': '恐慌', 'avg_buy_prob': 25, 'avg_panic_prob': 65}
    wd2 = {'主力状态': '吸筹', '可信度': 0.88}
    r2 = run_bajie_enhanced(bj2, sangsha_result=sg2, white_dragon_result=wd2)
    print(f"权重: {r2.get('signal_weights')}")
    print(f"特殊规则: {r2.get('signal_weight_notes')}")
    print(f"经验: {r2.get('_experiences_applied', [])}")

    # 测试3：地缘先验有效期 — 已过期15小时
    print('\n=== 测试3：地缘先验有效期 ===')
    bj3 = {'win_rate': '~72%', 'optimal_action': '做多黄金', 'optimal_etfs': '518880'}
    meta3 = {
        'has_geopolitical': True,
        'prior_type': 'geopolitical',
        'prior_updated_at': (datetime.now() - timedelta(hours=15)).isoformat()
    }
    r3 = run_bajie_enhanced(bj3, news_metadata=meta3)
    gc = r3.get('geo_prior_check', {})
    print(f"过期: {gc.get('is_expired')} ({gc.get('hours_since_last_update')}h)")
    print(f"逻辑止损: {r3.get('logic_stop_conditions', [])}")
    print(f"胜率: {r3.get('win_rate')}")
    print(f"经验: {r3.get('_experiences_applied', [])}")

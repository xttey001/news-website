# -*- coding: utf-8 -*-
"""
八戒贝叶斯融合模型 v2 - 融合沙僧+白龙马信号

核心变化：
- 八戒最终结论不再只看悟空+新闻贝叶斯
- 而是融合：悟空分析 + 新闻贝叶斯 + 沙僧情绪 + 白龙马主力状态
- 四层信号互相印证/矛盾时动态调整胜率和ETF推荐
"""

import json
import re
from typing import Dict, Any, List, Optional


class BajieCrossModel:
    """八戒贝叶斯融合模型 v2"""

    def __init__(self):
        pass

    def _extract_win_rate(self, win_rate_str: str) -> int:
        """从胜率字符串提取数字"""
        if isinstance(win_rate_str, int):
            return win_rate_str
        m = re.search(r'(\d+)', str(win_rate_str))
        return int(m.group(1)) if m else 50

    def _extract_max_drawdown(self, md_str: str) -> float:
        """从止损字符串提取数字"""
        m = re.search(r'(-?\d+)%', str(md_str))
        return float(m.group(1)) if m else -8.0

    def _adjust_for_sangsha(self, base_win_rate: int,
                            sangsha_sentiment: str,
                            avg_buy_prob: int,
                            avg_panic_prob: int) -> Dict[str, Any]:
        """
        【核心新增】沙僧信号调整

        沙僧揭示了散户的真实情绪，这对八戒的决策至关重要：
        - 散户狂热追高 → 八戒做多胜率实际下降（容易被套）
        - 散户恐慌 → 八戒做空胜率上升（逆向机会）
        - 散户平稳 → 八戒信号更可靠
        """
        adjustment = {
            'adjusted_win_rate': base_win_rate,
            'adjusted_drawdown': -8.0,
            'signal': '',
            'confidence': 'neutral'
        }

        sentiment_lower = sangsha_sentiment.lower() if sangsha_sentiment else ''

        # 狂热信号：散户FOMO追高
        if sangsha_sentiment == '狂热':
            if base_win_rate > 60:
                # 散户都追高了，利好兑现，主力可能出货
                new_wr = max(35, base_win_rate - 25)
                adjustment['adjusted_win_rate'] = new_wr
                adjustment['signal'] = f'⚠️ 沙僧警告：散户狂热追高（买入概率{avg_buy_prob}%）→ 八戒胜率从{base_win_rate}%降至{new_wr}%，追高即被套风险'
                adjustment['confidence'] = 'low'
                adjustment['adjusted_drawdown'] = -12.0
            else:
                adjustment['signal'] = f'⚠️ 沙僧警告：散户狂热追高，市场可能过热'

        # 积极信号：散户情绪积极
        elif sangsha_sentiment == '积极':
            if base_win_rate > 55:
                new_wr = base_win_rate + 5
                adjustment['adjusted_win_rate'] = min(90, new_wr)
                adjustment['signal'] = f'✅ 沙僧支持：散户情绪积极（买入概率{avg_buy_prob}%）→ 八戒胜率提升至{min(90,new_wr)}%，信号一致'
                adjustment['confidence'] = 'high'
            else:
                adjustment['signal'] = f'✅ 沙僧支持：散户情绪积极，与八戒信号方向一致'

        # 恐慌信号：散户恐慌
        elif sangsha_sentiment == '恐慌':
            # 逆向机会：散户恐慌往往是主力吸筹的信号
            adjustment['signal'] = f'📌 逆向机会：散户恐慌（恐慌概率{avg_panic_prob}%）→ 逆向布局优质资产'
            adjustment['confidence'] = 'high'
            # 恐慌时优质资产胜率提升
            if base_win_rate < 60:
                adjustment['adjusted_win_rate'] = base_win_rate + 15
                adjustment['adjusted_drawdown'] = -5.0

        # 平稳：无需调整
        else:
            adjustment['signal'] = '✅ 沙僧中性：散户情绪平稳，八戒信号可信'
            adjustment['confidence'] = 'normal'

        return adjustment

    def _adjust_for_white_dragon(self, state: str, wd_confidence: float,
                                 using_retail: bool) -> Dict[str, Any]:
        """
        【核心新增】白龙马信号调整

        白龙马揭示了主力的真实意图，这对八戒的ETF推荐至关重要：
        - 主力出货 + 散户追高 → 坚决回避
        - 主力吸筹 + 散户恐慌 → 逆向布局
        - 信号矛盾 → 降低可信度
        """
        adjustment = {
            'etf_adjustment': 'normal',
            'action_override': None,
            'signal': '',
            'risk_level': 'normal'
        }

        if '矛盾' in state or '信号混乱' in state:
            adjustment['action_override'] = '观望'
            adjustment['signal'] = '⚠️ 白龙马：信号矛盾，市场方向不明，建议观望'
            adjustment['risk_level'] = 'high'

        elif state == '出货' and using_retail:
            adjustment['action_override'] = '减仓回避'
            adjustment['etf_adjustment'] = 'reduce'
            adjustment['signal'] = '🚨 白龙马：主力派发+散户追高，双杀信号！建议清仓/减仓'
            adjustment['risk_level'] = 'extreme'

        elif state == '出货':
            adjustment['action_override'] = '减仓'
            adjustment['etf_adjustment'] = 'reduce'
            adjustment['signal'] = '⚠️ 白龙马：主力在出货，建议减仓等待'
            adjustment['risk_level'] = 'high'

        elif state == '吸筹':
            adjustment['action_override'] = '分批布局'
            adjustment['etf_adjustment'] = 'accumulate'
            adjustment['signal'] = '📌 白龙马：主力吸筹阶段，分批布局优质标的'
            adjustment['risk_level'] = 'low'

        elif state == '拉升':
            if using_retail:
                adjustment['action_override'] = '高位减仓'
                adjustment['signal'] = '⚠️ 白龙马：主力拉升但散户追高，注意高位风险，可适度减仓'
                adjustment['risk_level'] = 'medium'
            else:
                adjustment['signal'] = '✅ 白龙马：主力拉升初期，无散户接盘，上涨空间仍在'
                adjustment['risk_level'] = 'low'

        elif state == '洗盘':
            adjustment['signal'] = '📌 白龙马：主力洗盘，耐心等待，不追涨不杀跌'
            adjustment['risk_level'] = 'low'

        else:  # 观望
            adjustment['signal'] = '📊 白龙马：方向不明，保持观望'
            adjustment['risk_level'] = 'normal'

        # 可信度调整
        if wd_confidence and wd_confidence < 0.8:
            adjustment['risk_level'] = 'high'
            adjustment['signal'] += '（白龙马可信度偏低）'

        return adjustment

    def fuse_conclusion(self,
                        wukong: Optional[Dict],
                        original_bajie: Optional[Dict],
                        sangsha: Optional[Dict],
                        white_dragon: Optional[Dict]) -> Dict[str, Any]:
        """
        【核心方法】三层信号融合

        Args:
            wukong: 悟空判断 {market_sentiment/emotion, operations, core_analysis}
            original_bajie: 原始八戒结论（未融合前）
            sangsha: 沙僧模块 {overall_sentiment, avg_buy_prob, avg_panic_prob}
            white_dragon: 白龙马决策 {主力状态, 是否利用散户, 可信度, 散户情绪}

        Returns:
            dict: 融合后的八戒结论
        """

        # 提取原始数据
        wukong_sentiment = ''
        if wukong:
            wukong_sentiment = wukong.get('market_sentiment') or wukong.get('emotion', '')

        base_wr = 50
        base_drawdown = -8.0
        base_action = ''
        base_etfs = ''

        if original_bajie:
            base_wr = self._extract_win_rate(original_bajie.get('win_rate', 50))
            base_drawdown = self._extract_max_drawdown(original_bajie.get('max_drawdown', -8.0))
            base_action = original_bajie.get('optimal_action', '')
            base_etfs = original_bajie.get('optimal_etfs', '')

        # === 第一步：沙僧调整 ===
        sg_sentiment = sangsha.get('overall_sentiment', '平稳') if sangsha else '平稳'
        sg_buy = sangsha.get('avg_buy_prob', 50) if sangsha else 50
        sg_panic = sangsha.get('avg_panic_prob', 30) if sangsha else 30

        sg_adj = self._adjust_for_sangsha(base_wr, sg_sentiment, sg_buy, sg_panic)
        final_wr = sg_adj['adjusted_win_rate']
        final_drawdown = sg_adj['adjusted_drawdown']

        # === 第二步：白龙马调整 ===
        wd_state = white_dragon.get('主力状态', '观望') if white_dragon else '观望'
        wd_retail = white_dragon.get('是否利用散户', False) if white_dragon else False
        wd_cred = white_dragon.get('可信度', 1.0) if white_dragon else 1.0

        wd_adj = self._adjust_for_white_dragon(wd_state, wd_cred, wd_retail)

        # === 第三步：综合行动建议 ===
        # 白龙马行动优先级最高
        if wd_adj['action_override']:
            final_action = wd_adj['action_override']
            if sg_adj['signal'] and '⚠️' in sg_adj['signal']:
                final_action = f'{final_action}（{sg_sentiment}）'
        elif sg_sentiment == '狂热' and base_wr > 60:
            final_action = '减仓观望'
        elif sg_sentiment == '恐慌':
            final_action = '逆向布局优质资产'
        else:
            final_action = base_action

        # === 第四步：ETF调整 ===
        if wd_adj['etf_adjustment'] == 'reduce':
            final_etfs = f'（已减仓）{base_etfs}'
        elif wd_adj['etf_adjustment'] == 'accumulate':
            final_etfs = f'（分批建仓）{base_etfs}'
        else:
            final_etfs = base_etfs

        # === 第五步：生成融合说明 ===
        fusion_notes = []
        fusion_notes.append(f'【沙僧融合】{sg_adj["signal"]}')
        fusion_notes.append(f'【白龙马融合】{wd_adj["signal"]}')

        # 信号一致性评分
        signal_score = 0
        if sangsha and white_dragon:
            # 一致性判断
            if sg_sentiment == '积极' and '拉升' in wd_state:
                signal_score = 3  # 高度一致
            elif sg_sentiment == '恐慌' and '吸筹' in wd_state:
                signal_score = 3  # 逆向机会
            elif sg_sentiment == '狂热' and '出货' in wd_state:
                signal_score = 3  # 双杀警告
            elif sg_sentiment == '平稳':
                signal_score = 2  # 中性
            else:
                signal_score = 1  # 信号混乱

        consistency = {
            3: '✅✅ 高度一致：四层信号共振，胜率可信',
            2: '✅ 信号正常：沙僧/白龙马无明显矛盾',
            1: '⚠️ 信号混乱：沙僧/白龙马判断不一致，需谨慎',
        }.get(signal_score, '⚠️ 信号待确认')

        # === 最终结论 ===
        return {
            # 核心结论
            'optimal_action': final_action,
            'optimal_etfs': final_etfs,
            'win_rate': f'~{final_wr}%（贝叶斯后验+沙僧白龙马融合）',
            'max_drawdown': f'{final_drawdown}%（止损线）',

            # 融合详情
            '沙僧信号': {
                '情绪': sg_sentiment,
                '平均买入概率': sg_buy,
                '平均恐慌概率': sg_panic,
                '调整结果': sg_adj['signal'],
                '可信度级别': sg_adj['confidence']
            },
            '白龙马信号': {
                '主力状态': wd_state,
                '是否利用散户': wd_retail,
                '可信度': round(wd_cred, 2) if wd_cred else 1.0,
                '风险等级': wd_adj['risk_level'],
                '调整结果': wd_adj['signal']
            },
            '悟空信号': {
                '市场情绪': wukong_sentiment
            },

            # 综合评估
            '信号一致性': consistency,
            '信号一致性得分': signal_score,
            '融合说明': fusion_notes,
            'original_bajie': original_bajie  # 保留原始八戒结论
        }


def run_bajie_cross(wukong: Optional[Dict],
                    original_bajie: Optional[Dict],
                    sangsha: Optional[Dict],
                    white_dragon: Optional[Dict]) -> Dict[str, Any]:
    """运行八戒融合模型"""
    model = BajieCrossModel()
    return model.fuse_conclusion(wukong, original_bajie, sangsha, white_dragon)


if __name__ == '__main__':
    # 测试案例1：信号矛盾
    wukong = {'market_sentiment': '谨慎偏多', 'operations': [{'type': '可做', 'content': '芯片'}]}
    bajie = {'optimal_action': '轻仓布局芯片ETF', 'optimal_etfs': '512760芯片ETF(50%)', 'win_rate': '~70%', 'max_drawdown': '-8%'}
    sangsha = {'overall_sentiment': '狂热', 'avg_buy_prob': 78, 'avg_panic_prob': 15}
    wd = {'主力状态': '出货', '是否利用散户': True, '可信度': 0.7, '散户情绪': {'平均买入概率': 78, '平均恐慌概率': 15}}

    result = run_bajie_cross(wukong, bajie, sangsha, wd)
    print('=== 信号矛盾测试 ===')
    print(f"最终行动: {result['optimal_action']}")
    print(f"最终胜率: {result['win_rate']}")
    print(f"风险等级: {result['白龙马信号']['风险等级']}")
    print(f"一致性: {result['信号一致性']}")
    print()
    for note in result['融合说明']:
        print(note)

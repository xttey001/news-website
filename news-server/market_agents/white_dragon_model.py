# -*- coding: utf-8 -*-
"""
白龙马主力行为模型 v2 - 融合悟空/八戒信号

变化：
- 接收悟空的市场情绪 + 八戒的胜率作为输入
- 当悟空情绪与白龙马判断矛盾时，自动降级主力可信度
- 当八戒胜率低但白龙马显示吸筹时，给出逆向布局建议
"""

import json
from typing import Dict, Any, List, Optional


class WhiteDragonModel:
    """白龙马主力行为模型 v2"""

    def __init__(self):
        self.main_etfs = ['512760', '512930', '518880', '588890', '159382']

    def _calculate_price_trend(self, klines: List[Dict]) -> Dict[str, Any]:
        if not klines or len(klines) < 3:
            return {'trend': 'side', 'strength': 0, 'change_pct': 0}
        recent = klines[-3:]
        earlier = klines[:-3] if len(klines) > 3 else recent[:1]
        avg_recent = sum(k['close'] for k in recent) / len(recent)
        avg_earlier = sum(k['close'] for k in earlier) / len(earlier)
        change_pct = (avg_recent - avg_earlier) / avg_earlier * 100 if avg_earlier > 0 else 0
        up_days = sum(1 for k in recent if k['change_pct'] > 0)
        if up_days >= 3:
            trend, strength = 'up', 90
        elif up_days >= 2 and change_pct > 3:
            trend, strength = 'up', 75
        elif change_pct > 5:
            trend, strength = 'up', 70
        elif up_days <= 1 and change_pct < -3:
            trend, strength = 'down', 70
        elif change_pct < -5:
            trend, strength = 'down', 80
        else:
            trend, strength = 'side', 40
        return {'trend': trend, 'strength': strength, 'change_pct': round(change_pct, 2)}

    def _calculate_volume_trend(self, klines: List[Dict]) -> Dict[str, Any]:
        if not klines or len(klines) < 5:
            return {'trend': 'side', 'change_pct': 0, 'level': 'normal'}
        recent_vol = sum(k['volume'] for k in klines[-3:]) / 3
        avg_vol = sum(k['volume'] for k in klines) / len(klines)
        change_pct = (recent_vol - avg_vol) / avg_vol * 100 if avg_vol > 0 else 0
        if change_pct > 50:
            return {'trend': 'up', 'change_pct': round(change_pct, 2), 'level': 'high'}
        elif change_pct < -30:
            return {'trend': 'down', 'change_pct': round(change_pct, 2), 'level': 'low'}
        else:
            return {'trend': 'side', 'change_pct': round(change_pct, 2), 'level': 'normal'}

    def _wukong_bajie_adjust(self, state: str, wukong: Optional[Dict], 
                             bajie: Optional[Dict]) -> Dict[str, Any]:
        """
        【新增】悟空/八戒信号交叉分析
        根据悟空情绪和八戒胜率调整主力状态可信度
        """
        wukong_sentiment = ''
        bajie_win_rate = 0
        bajie_action = ''

        if wukong and isinstance(wukong, dict):
            wukong_sentiment = wukong.get('market_sentiment', wukong.get('emotion', ''))

        if bajie and isinstance(bajie, dict):
            wr = bajie.get('win_rate', '')
            # 从 "~65%（贝叶斯后验）" 提取数字
            import re
            m = re.search(r'(\d+)', str(wr))
            if m:
                bajie_win_rate = int(m.group(1))
            bajie_action = bajie.get('optimal_action', '')

        adjustment = {
            'credibility': 1.0,  # 可信度调整
            'signal_conflict': False,
            'signal_note': '',
            'adjusted_state': state
        }

        # 矛盾检测1：悟空极度乐观 vs 白龙马显示出货
        if '出货' in state and wukong_sentiment:
            if any(kw in wukong_sentiment for kw in ['积极', '做多', '乐观', '突破']):
                adjustment['credibility'] *= 0.7
                adjustment['signal_conflict'] = True
                adjustment['signal_note'] = f'⚠️ 矛盾信号：悟空看多但主力在出货，可信度降30%'
                adjustment['adjusted_state'] = '矛盾-主力派发'
            elif any(kw in wukong_sentiment for kw in ['谨慎', '防御', '观望']):
                adjustment['credibility'] *= 1.1
                adjustment['signal_note'] = '✅ 信号一致：悟空谨慎，主力派发判断可信'

        # 矛盾检测2：悟空极度恐慌 vs 白龙马显示吸筹
        if '吸筹' in state and wukong_sentiment:
            if any(kw in wukong_sentiment for kw in ['恐慌', '谨慎', '防御']):
                adjustment['credibility'] *= 1.2
                adjustment['signal_note'] = '✅ 逆向布局机会：悟空恐慌 + 主力吸筹，逆向投资者可关注'
            elif any(kw in wukong_sentiment for kw in ['积极', '乐观']):
                adjustment['credibility'] *= 0.8
                adjustment['signal_conflict'] = True
                adjustment['signal_note'] = f'⚠️ 矛盾信号：悟空乐观但主力在吸筹，可能是诱多'

        # 矛盾检测3：八戒胜率高 vs 白龙马显示出货
        if '出货' in state and bajie_win_rate > 65:
            adjustment['credibility'] *= 0.75
            adjustment['signal_conflict'] = True
            adjustment['signal_note'] = f'⚠️ 矛盾：八戒胜率{bajie_win_rate}%但主力在出货，建议降仓'
            adjustment['adjusted_state'] = '矛盾-主力派发'

        # 矛盾检测4：八戒胜率低 vs 白龙马显示吸筹
        if '吸筹' in state and 0 < bajie_win_rate < 50:
            adjustment['credibility'] *= 1.15
            adjustment['signal_note'] = f'📌 逆向机会：八戒胜率低但主力吸筹，可分批布局'

        # 矛盾检测5：悟空中性 + 白龙马洗盘
        if '洗盘' in state and wukong_sentiment:
            if any(kw in wukong_sentiment for kw in ['震荡', '中性', '平稳']):
                adjustment['credibility'] *= 1.1
                adjustment['signal_note'] = '✅ 信号一致：悟空中性 + 主力洗盘，后市方向待定'

        return adjustment

    def analyze_single_etf(self, code: str, market_data: Dict,
                          sangsha_buy_prob: int = 0,
                          sangsha_panic_prob: int = 0,
                          wukong: Optional[Dict] = None,
                          bajie: Optional[Dict] = None) -> Dict[str, Any]:
        data = market_data.get(code, {})
        klines = data.get('klines', [])
        realtime = data.get('realtime', {})

        price_trend = self._calculate_price_trend(klines)
        volume_trend = self._calculate_volume_trend(klines)

        # 基础主力状态判断
        if price_trend['trend'] == 'up' and volume_trend['trend'] == 'up':
            if sangsha_buy_prob > 60:
                state, stage, explanation, using_retail = '出货', '末期', \
                    '价格大涨+放量，但散户追高情绪高涨，主力可能借机派发', True
            else:
                state, stage, explanation, using_retail = '拉升', '中期', \
                    '量价齐升，资金积极入场，短期有望继续上涨', False
        elif price_trend['trend'] == 'up':
            state, stage, explanation, using_retail = '出货', '末期', \
                '价格上涨但量能不足，主力高位派发可能性大', True
        elif price_trend['trend'] in ['side', 'down'] and sangsha_buy_prob < 40:
            state, stage, explanation, using_retail = '吸筹', '早期', \
                '价格横盘/小跌，资金流入，主力可能在低位吸筹', False
        elif price_trend['trend'] == 'down' and volume_trend['level'] == 'low':
            state, stage, explanation, using_retail = '洗盘', '早期', \
                '缩量下跌，主力清洗浮动筹码，后市有望拉升', False
        elif price_trend['trend'] == 'side':
            state, stage, explanation, using_retail = '观望', '整理', \
                '价格横盘震荡，等待方向选择', False
        else:
            state, stage, explanation, using_retail = '观望', '观察', \
                '处于下降趋势中，建议观望', False

        # 【核心新增】悟空/八戒交叉分析
        xg = self._wukong_bajie_adjust(state, wukong, bajie)
        if xg['signal_conflict']:
            state = xg['adjusted_state']

        return {
            'code': code,
            'price_trend': price_trend,
            'volume_trend': volume_trend,
            '主力状态': state,
            '阶段': stage,
            '行为解释': explanation,
            '是否利用散户': using_retail,
            '可信度': round(xg['credibility'], 2),
            '矛盾信号': xg['signal_note'],
            'sangsha_buy_prob': sangsha_buy_prob,
            'sangsha_panic_prob': sangsha_panic_prob
        }

    def analyze_multi_etfs(self, market_data: Dict,
                          sangsha_results: List[Dict] = None,
                          wukong: Optional[Dict] = None,
                          bajie: Optional[Dict] = None) -> Dict[str, Any]:
        avg_buy = 0
        avg_panic = 0
        if sangsha_results:
            n = min(5, len(sangsha_results))
            avg_buy = sum(r.get('买入概率', 0) for r in sangsha_results[:n]) / n
            avg_panic = sum(r.get('恐慌卖出概率', 0) for r in sangsha_results[:n]) / n

        etf_results = []
        for code in self.main_etfs:
            if code in market_data:
                result = self.analyze_single_etf(
                    code, market_data, int(avg_buy), int(avg_panic), wukong, bajie
                )
                etf_results.append(result)

        # 综合多个ETF的状态
        states = [r['主力状态'] for r in etf_results]
        creds = [r['可信度'] for r in etf_results]
        avg_cred = sum(creds) / len(creds) if creds else 1.0

        pumping = sum(1 for s in states if '拉升' in s)
        distributing = sum(1 for s in states if '出货' in s)
        accumulating = sum(1 for s in states if '吸筹' in s)
        washing = sum(1 for s in states if '洗盘' in s)
        conflicting = sum(1 for s in states if '矛盾' in s)

        # 矛盾ETF > 50%，判断为信号混乱
        if conflicting >= 2:
            overall_state, overall_stage = '信号混乱', '需观察'
            overall_explanation = f'多个ETF主力信号矛盾（{conflicting}个），市场分歧极大，建议观望等待信号明确'
        elif pumping >= 2:
            overall_state, overall_stage = '拉升', '中期'
            overall_explanation = '多个ETF处于拉升状态，市场整体偏多'
        elif distributing >= 2:
            overall_state, overall_stage = '出货', '末期'
            overall_explanation = '多个ETF出现主力派发信号，注意风险'
        elif accumulating >= 2:
            overall_state, overall_stage = '吸筹', '早期'
            overall_explanation = '多个ETF显示主力吸筹信号，可分批布局'
        elif washing >= 2:
            overall_state, overall_stage = '洗盘', '早期'
            overall_explanation = '多个ETF处于洗盘状态，后市有望反弹'
        else:
            overall_state, overall_stage = '分化', '观察'
            overall_explanation = '各ETF分化明显，需要精选标的'

        using_retail = any(r.get('是否利用散户', False) for r in etf_results)

        # 悟空/八戒交叉信号说明
        xg_note = ''
        if wukong and isinstance(wukong, dict):
            sentiment = wukong.get('market_sentiment', wukong.get('emotion', ''))
            xg_note += f'悟空情绪：{sentiment}；'

        # 最终建议（融合四层信号）
        final_advice = self._generate_advice_v2(
            overall_state, using_retail, avg_buy, avg_panic,
            avg_cred, wukong, bajie
        )

        return {
            "白龙马决策": {
                "主力状态": overall_state,
                "阶段": overall_stage,
                "行为解释": overall_explanation,
                "是否利用散户": using_retail,
                "可信度": round(avg_cred, 2),
                "矛盾ETF数": conflicting,
                "散户情绪": {
                    "平均买入概率": int(avg_buy),
                    "平均恐慌概率": int(avg_panic)
                },
                "悟空信号": wukong.get('market_sentiment', wukong.get('emotion', '')) if wukong else '暂无',
                "八戒胜率": bajie.get('win_rate', '暂无') if bajie else '暂无',
                "各ETF分析": etf_results,
                "综合建议": final_advice
            }
        }

    def _generate_advice_v2(self, state: str, using_retail: bool,
                            buy_prob: float, panic_prob: float,
                            credibility: float,
                            wukong: Optional[Dict],
                            bajie: Optional[Dict]) -> str:
        """v2版本：融合悟空/八戒/沙僧/白龙马四层信号"""

        # 从八戒提取胜率
        bajie_wr = 0
        if bajie and isinstance(bajie, dict):
            import re
            m = re.search(r'(\d+)', str(bajie.get('win_rate', '')))
            if m:
                bajie_wr = int(m.group(1))

        advice_parts = []

        # 白龙马基础建议
        if '矛盾' in state or '信号混乱' in state:
            advice_parts.append('⚠️ 信号矛盾：悟空/白龙马/散户三方信号不一致，建议观望或降仓')
        elif state == '出货' and using_retail:
            advice_parts.append('⚠️ 风险提示：主力派发+散户追高，双重风险，建议减仓')
        elif state == '拉升' and not using_retail and credibility > 1.0:
            advice_parts.append('✅ 积极信号：主力拉升初期，无散户接盘，可适度参与')
        elif state == '拉升' and credibility < 0.9:
            advice_parts.append('⚠️ 可疑拉升：主力可能在诱多，需警惕')
        elif state == '吸筹':
            advice_parts.append('📌 布局时机：主力吸筹阶段，可分批建仓')
        elif panic_prob > 55:
            advice_parts.append('📌 恐慌时刻：散户恐慌往往是逆向机会')
        elif buy_prob > 65:
            advice_parts.append('⚠️ 过热警告：散户情绪过于亢奋，追高风险大')

        # 八戒胜率融合
        if bajie_wr > 0:
            if bajie_wr >= 70 and '出货' not in state:
                advice_parts.append(f'✅ 八戒支持：胜率{bajie_wr}%，胜率信号积极')
            elif bajie_wr < 50 and '吸筹' in state:
                advice_parts.append(f'📌 逆向机会：八戒胜率低但主力吸筹，逆向布局窗口')
            elif bajie_wr < 50 and '出货' in state:
                advice_parts.append(f'⚠️ 双杀信号：八戒胜率低+主力派发，建议清仓观望')

        if not advice_parts:
            return '📊 观望为主：市场方向不明，建议轻仓观望'
        return '；'.join(advice_parts)


def run_white_dragon(market_data: Dict,
                     sangsha_results: List[Dict] = None,
                     wukong: Optional[Dict] = None,
                     bajie: Optional[Dict] = None) -> Dict:
    """运行白龙马模型（支持悟空/八戒信号输入）"""
    model = WhiteDragonModel()
    return model.analyze_multi_etfs(market_data, sangsha_results, wukong, bajie)


if __name__ == '__main__':
    test_klines = [
        {'date': '2026-04-03', 'close': 0.77, 'change_pct': 2.5, 'volume': 100},
        {'date': '2026-04-07', 'close': 0.78, 'change_pct': 1.3, 'volume': 150},
        {'date': '2026-04-08', 'close': 0.83, 'change_pct': 6.4, 'volume': 200},
        {'date': '2026-04-09', 'close': 0.83, 'change_pct': 0, 'volume': 120},
    ]
    test_data = {'512760': {'klines': test_klines, 'realtime': {}}}
    sangsha = [{'买入概率': 75, '恐慌卖出概率': 20}]
    wukong = {'market_sentiment': '谨慎偏多'}
    bajie = {'win_rate': '~65%（贝叶斯后验）'}

    result = run_white_dragon(test_data, sangsha, wukong, bajie)
    wd = result.get('白龙马决策', {})
    print(f"状态: {wd.get('主力状态')} | 阶段: {wd.get('阶段')} | 可信度: {wd.get('可信度')}")
    print(f"建议: {wd.get('综合建议')}")
    print(f"矛盾: {wd.get('矛盾ETF数', 0)}个")

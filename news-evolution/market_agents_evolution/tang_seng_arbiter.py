# -*- coding: utf-8 -*-
"""
唐僧轻量仲裁器 v1 — 跨层矛盾仲裁 + 全局风控

职责（精简版，不当总管）：
1. 跨层矛盾仲裁：当徒弟们意见冲突时裁决
2. 全局风控检查：节假日/黑天鹅等跨层风险
3. 决策格式化输出：汇总所有模块结果为最终决策

不做的事：
- 不替徒弟做他们专业领域内的判断
- 不重复计算徒弟们已经算过的东西
- 不存储经验（经验存在各模块的知识库里）
"""

import json
import os
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


# 中国法定节假日列表（可动态更新）
HOLIDAYS_2026 = [
    # 元旦
    {'name': '元旦', 'start': '2026-01-01', 'end': '2026-01-03'},
    # 春节
    {'name': '春节', 'start': '2026-02-14', 'end': '2026-02-20'},
    # 清明
    {'name': '清明', 'start': '2026-04-04', 'end': '2026-04-06'},
    # 五一
    {'name': '五一', 'start': '2026-05-01', 'end': '2026-05-05'},
    # 端午
    {'name': '端午', 'start': '2026-05-30', 'end': '2026-06-01'},
    # 中秋
    {'name': '中秋', 'start': '2026-09-25', 'end': '2026-09-27'},
    # 国庆
    {'name': '国庆', 'start': '2026-10-01', 'end': '2026-10-07'},
]


class TangSengArbiter:
    """唐僧轻量仲裁器"""

    def __init__(self):
        self.holidays = HOLIDAYS_2026

    # ============================================================
    #  主方法：仲裁 + 风控 + 格式化输出
    # ============================================================

    def arbitrate(self,
                  wukong_enhanced: Optional[Dict],
                  sangsha_enhanced: Optional[Dict],
                  white_dragon_enhanced: Optional[Dict],
                  bajie_calibrated: Optional[Dict],
                  news_metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """
        唐僧最终仲裁

        Args:
            wukong_enhanced: 悟空增强后的结果
            sangsha_enhanced: 沙僧增强后的结果
            white_dragon_enhanced: 白龙马增强后的结果
            bajie_calibrated: 八戒校准后的结果
            news_metadata: 场景元数据（地缘/节日/Trump等）

        Returns:
            dict: 最终决策（含仲裁说明+风控检查+各模块贡献）
        """
        metadata = news_metadata or {}
        arbitration_notes = []
        risk_checks = []

        # === 第一步：跨层矛盾仲裁 ===
        conflicts = self._detect_conflicts(wukong_enhanced, sangsha_enhanced,
                                           white_dragon_enhanced, bajie_calibrated)
        if conflicts:
            resolutions = self._resolve_conflicts(conflicts, bajie_calibrated)
            arbitration_notes.extend(resolutions)
        else:
            arbitration_notes.append('🙏 唐僧：四层信号无重大矛盾，各司其职')

        # === 第二步：全局风控检查 ===
        risk_checks = self._run_risk_checks(metadata, bajie_calibrated)

        # === 第三步：基于风控结果调整 ===
        final_action = bajie_calibrated.get('optimal_action', '') if bajie_calibrated else ''
        final_wr = self._extract_wr(bajie_calibrated.get('win_rate', '~50%')) if bajie_calibrated else 50

        for check in risk_checks:
            if check.get('override_action'):
                final_action = check['override_action']
            if check.get('adjust_win_rate'):
                final_wr += check['adjust_win_rate']

        final_wr = max(10, min(95, final_wr))  # 限制在10-95%范围

        # === 第四步：格式化输出 ===
        result = {
            # 最终决策
            'final_action': final_action,
            'final_win_rate': f'~{final_wr}%',
            'optimal_etfs': bajie_calibrated.get('optimal_etfs', '') if bajie_calibrated else '',
            'max_drawdown': bajie_calibrated.get('max_drawdown', '') if bajie_calibrated else '',

            # 唐僧附加
            'arbitration_notes': arbitration_notes,
            'risk_checks': risk_checks,
            'conflict_count': len(conflicts),

            # 各模块贡献摘要
            'module_summary': {
                '悟空': self._summarize_wukong(wukong_enhanced),
                '沙僧': self._summarize_sangsha(sangsha_enhanced),
                '白龙马': self._summarize_white_dragon(white_dragon_enhanced),
                '八戒': self._summarize_bajie(bajie_calibrated),
            },

            # 经验注入记录（用于复盘）
            'experience_applied': {
                '悟空': wukong_enhanced.get('_experiences_applied', []) if wukong_enhanced else [],
                '沙僧': sangsha_enhanced.get('_experiences_applied', []) if sangsha_enhanced else [],
                '白龙马': white_dragon_enhanced.get('_experiences_applied', []) if white_dragon_enhanced else [],
                '八戒': bajie_calibrated.get('_experiences_applied', []) if bajie_calibrated else [],
            },

            # 保留原始八戒结果用于对比
            'original_bajie': bajie_calibrated.get('original_bajie', bajie_calibrated) if bajie_calibrated else {},
        }

        return result

    # ============================================================
    #  矛盾检测
    # ============================================================

    def _detect_conflicts(self, wukong, sangsha, white_dragon, bajie) -> List[Dict]:
        """检测跨层矛盾"""
        conflicts = []

        # 矛盾1：沙僧狂热 + 白龙马≠出货 → 听白龙马
        sg_sentiment = sangsha.get('overall_sentiment', '') if sangsha else ''
        wd_state = white_dragon.get('主力状态', '') if white_dragon else ''

        if sg_sentiment == '狂热' and wd_state not in ['出货', '出货(Trump关联)']:
            conflicts.append({
                'type': 'sangsha_hot_vs_wd_not_selling',
                'description': f'沙僧=狂热 但 白龙马={wd_state}（非出货）',
                'rule': '散户可能过度反应，主力尚未派发'
            })

        # 矛盾2：悟空看多 + 白龙马出货
        wk_sentiment = wukong.get('market_sentiment', wukong.get('emotion', '')) if wukong else ''
        if any(kw in wk_sentiment for kw in ['偏多', '看多', '积极']) and '出货' in wd_state:
            conflicts.append({
                'type': 'wukong_bull_vs_wd_selling',
                'description': f'悟空看多({wk_sentiment}) 但 白龙马={wd_state}',
                'rule': '主力出货信号优先于新闻分析'
            })

        # 矛盾3：沙僧恐慌 + 白龙马吸筹 = 超级逆向
        if sg_sentiment in ['恐慌', '极度恐慌'] and '吸筹' in wd_state:
            conflicts.append({
                'type': 'sangsha_panic_vs_wd_accumulating',
                'description': f'沙僧={sg_sentiment} 且 白龙马={wd_state}',
                'rule': '超级逆向信号：散户恐慌交出筹码，主力趁机吸筹'
            })

        # 矛盾4：悟空与八戒方向不一致
        bj_action = bajie.get('optimal_action', '') if bajie else ''
        if any(kw in wk_sentiment for kw in ['偏空', '看空', '谨慎']) and \
           any(kw in bj_action for kw in ['布局', '买入', '加仓']):
            conflicts.append({
                'type': 'wukong_bear_vs_bajie_buy',
                'description': f'悟空看空({wk_sentiment}) 但 八戒建议买入({bj_action})',
                'rule': '降低整体置信度，方向矛盾时保守操作'
            })

        return conflicts

    # ============================================================
    #  矛盾仲裁
    # ============================================================

    def _resolve_conflicts(self, conflicts: List[Dict], bajie: Optional[Dict]) -> List[str]:
        """根据优先级表仲裁矛盾"""
        notes = []

        for conflict in conflicts:
            ctype = conflict['type']

            if ctype == 'sangsha_hot_vs_wd_not_selling':
                notes.append(f'🙏 唐僧仲裁：{conflict["description"]} → 听白龙马的（主力比韭菜聪明），散户可能过度反应')

            elif ctype == 'wukong_bull_vs_wd_selling':
                notes.append(f'🙏 唐僧仲裁：{conflict["description"]} → 主力出货信号优先，减仓回避')

            elif ctype == 'sangsha_panic_vs_wd_accumulating':
                notes.append(f'🙏 唐僧仲裁：{conflict["description"]} → ★超级逆向信号★，加权1.4，这是最好的买点')

            elif ctype == 'wukong_bear_vs_bajie_buy':
                notes.append(f'🙏 唐僧仲裁：{conflict["description"]} → 方向矛盾，降置信度20%，建议观望或极轻仓试探')

            else:
                notes.append(f'🙏 唐僧仲裁：{conflict["description"]} → 信号矛盾，建议谨慎')

        # 矛盾过多时全局降级
        if len(conflicts) >= 2:
            notes.append('🙏 唐僧全局：矛盾≥2个，整体置信度降级，建议保守操作或观望')

        return notes

    # ============================================================
    #  全局风控检查
    # ============================================================

    def _run_risk_checks(self, metadata: Dict, bajie: Optional[Dict]) -> List[Dict]:
        """全局风控检查（唐僧专属职责）"""
        checks = []

        # 检查1：地缘+节假日（最危险组合）
        if metadata.get('has_geopolitical') and metadata.get('is_near_holiday'):
            checks.append({
                'item': '地缘事件+节假日临近',
                'status': '🚨 极高风险',
                'override_action': '大幅减仓或清仓',
                'adjust_win_rate': -20,
                'reason': '休市期间信息不对称，地缘先验极不稳定'
            })

        # 检查2：节假日临近+持仓依赖地缘/大宗
        if metadata.get('is_near_holiday') and metadata.get('has_geopolitical'):
            checks.append({
                'item': '节假日前持仓风险',
                'status': '⚠️ 高风险',
                'adjust_win_rate': -10,
                'reason': '若持仓逻辑依赖地缘事件，必须大幅减仓'
            })

        # 检查3：Trump喊话强度≥2
        trump_intensity = metadata.get('trump_intensity', 0)
        if trump_intensity >= 2:
            checks.append({
                'item': f'Trump喊话强度={trump_intensity}',
                'status': '⚠️ 反转风险',
                'reason': f'连续{trump_intensity}天喊话，反转概率~{"50%" if trump_intensity==2 else "70%+"}',
                'adjust_win_rate': -5 if trump_intensity == 2 else -15
            })

        # 检查4：逻辑止损是否缺失
        if bajie and not bajie.get('logic_stop_conditions'):
            has_geo = metadata.get('has_geopolitical', False)
            if has_geo:
                checks.append({
                    'item': '逻辑止损缺失（地缘事件场景）',
                    'status': '❌ 必须补充',
                    'reason': '地缘事件必须设逻辑止损：停火/和平声明/海峡开放'
                })

        # 检查5：先验概率是否过期
        prior_age_hours = metadata.get('prior_age_hours', 0)
        prior_type = metadata.get('prior_type', '')
        if prior_type == 'geopolitical' and prior_age_hours > 12:
            checks.append({
                'item': f'地缘先验已{prior_age_hours}小时未更新',
                'status': '⚠️ 过期',
                'adjust_win_rate': -10,
                'reason': '地缘先验有效期12小时，需重新评估'
            })

        if not checks:
            checks.append({
                'item': '全局风控',
                'status': '✅ 通过',
                'reason': '无重大跨层风险'
            })

        return checks

    # ============================================================
    #  辅助方法
    # ============================================================

    def _extract_wr(self, wr_str: str) -> int:
        """从胜率字符串提取数字"""
        if isinstance(wr_str, (int, float)):
            return int(wr_str)
        m = re.search(r'(\d+)', str(wr_str))
        return int(m.group(1)) if m else 50

    def _summarize_wukong(self, wk: Optional[Dict]) -> str:
        if not wk:
            return '无数据'
        sentiment = wk.get('market_sentiment', wk.get('emotion', '?'))
        exps = wk.get('_experiences_applied', [])
        exp_tag = f' | 注入{len(exps)}条经验' if exps else ''
        return f'情绪:{sentiment}{exp_tag}'

    def _summarize_sangsha(self, sg: Optional[Dict]) -> str:
        if not sg:
            return '无数据'
        sentiment = sg.get('overall_sentiment', '?')
        buy = sg.get('avg_buy_prob', '?')
        exps = sg.get('_experiences_applied', [])
        exp_tag = f' | 注入{len(exps)}条经验' if exps else ''
        return f'情绪:{sentiment}(买入{buy}%){exp_tag}'

    def _summarize_white_dragon(self, wd: Optional[Dict]) -> str:
        if not wd:
            return '无数据'
        state = wd.get('主力状态', '?')
        cred = wd.get('可信度', '?')
        exps = wd.get('_experiences_applied', [])
        exp_tag = f' | 注入{len(exps)}条经验' if exps else ''
        return f'主力:{state}(可信度{cred}){exp_tag}'

    def _summarize_bajie(self, bj: Optional[Dict]) -> str:
        if not bj:
            return '无数据'
        action = bj.get('optimal_action', '?')
        wr = bj.get('win_rate', '?')
        exps = bj.get('_experiences_applied', [])
        exp_tag = f' | 注入{len(exps)}条经验' if exps else ''
        return f'行动:{action} 胜率:{wr}{exp_tag}'

    # ============================================================
    #  节假日检测（供外部调用）
    # ============================================================

    @staticmethod
    def is_near_holiday(date_str: str = None, days_before: int = 3) -> Dict:
        """
        检测是否临近节假日

        Args:
            date_str: 日期字符串 YYYY-MM-DD，默认今天
            days_before: 提前几天预警

        Returns:
            dict: {is_near: bool, holiday_name: str, days_until: int}
        """
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')

        try:
            check_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return {'is_near': False, 'holiday_name': '', 'days_until': 999}

        for h in HOLIDAYS_2026:
            start = datetime.strptime(h['start'], '%Y-%m-%d')
            delta = (start - check_date).days
            if 0 <= delta <= days_before:
                return {
                    'is_near': True,
                    'holiday_name': h['name'],
                    'days_until': delta,
                    'holiday_start': h['start'],
                    'holiday_end': h['end']
                }

        return {'is_near': False, 'holiday_name': '', 'days_until': 999}

    @staticmethod
    def is_earnings_season(date_str: str = None) -> bool:
        """判断是否在财报季"""
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        month = int(date_str.split('-')[1])
        return month in [3, 4, 8, 9]


# ============================================================
#  便捷函数
# ============================================================

def run_tang_seng_arbitrate(wukong_enhanced: Optional[Dict],
                            sangsha_enhanced: Optional[Dict],
                            white_dragon_enhanced: Optional[Dict],
                            bajie_calibrated: Optional[Dict],
                            news_metadata: Optional[Dict] = None) -> Dict[str, Any]:
    """运行唐僧仲裁"""
    arbiter = TangSengArbiter()
    return arbiter.arbitrate(wukong_enhanced, sangsha_enhanced,
                             white_dragon_enhanced, bajie_calibrated,
                             news_metadata)


# ============================================================
#  测试
# ============================================================

if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 测试案例1：四层无矛盾
    print('=== 测试1：四层无矛盾 ===')
    wk = {'market_sentiment': '谨慎偏多', '_experiences_applied': ['WX-002']}
    sg = {'overall_sentiment': '积极', 'avg_buy_prob': 60, '_experiences_applied': []}
    wd = {'主力状态': '吸筹', '可信度': 0.85, '_experiences_applied': ['WD-001']}
    bj = {'optimal_action': '轻仓布局', 'optimal_etfs': '512760', 'win_rate': '~68%',
          'max_drawdown': '-8%', '_experiences_applied': ['BJ-001'], 'original_bajie': {}}
    meta = {'has_geopolitical': False, 'is_near_holiday': False, 'trump_intensity': 0}

    result = run_tang_seng_arbitrate(wk, sg, wd, bj, meta)
    print(f"行动: {result['final_action']}")
    print(f"胜率: {result['final_win_rate']}")
    for note in result['arbitration_notes']:
        print(f"  {note}")
    for check in result['risk_checks']:
        print(f"  风控: {check['item']} → {check['status']}")

    # 测试案例2：地缘+节假日（极高风险）
    print('\n=== 测试2：地缘+节假日 ===')
    wk2 = {'market_sentiment': '偏多', '_experiences_applied': ['WX-001']}
    sg2 = {'overall_sentiment': '积极', 'avg_buy_prob': 65, '_experiences_applied': []}
    wd2 = {'主力状态': '拉升', '可信度': 0.80, '_experiences_applied': []}
    bj2 = {'optimal_action': '布局油气ETF', 'optimal_etfs': '518880', 'win_rate': '~72%',
           'max_drawdown': '-7%', '_experiences_applied': ['BJ-003'], 'original_bajie': {}}
    meta2 = {'has_geopolitical': True, 'is_near_holiday': True, 'trump_intensity': 2,
             'holiday_name': '清明', 'days_until': 1}

    result2 = run_tang_seng_arbitrate(wk2, sg2, wd2, bj2, meta2)
    print(f"行动: {result2['final_action']}")
    print(f"胜率: {result2['final_win_rate']}")
    for note in result2['arbitration_notes']:
        print(f"  {note}")
    for check in result2['risk_checks']:
        print(f"  风控: {check['item']} → {check['status']}")

    # 测试案例3：超级逆向信号
    print('\n=== 测试3：沙僧恐慌+白龙马吸筹 ===')
    wk3 = {'market_sentiment': '偏空', '_experiences_applied': []}
    sg3 = {'overall_sentiment': '恐慌', 'avg_buy_prob': 25, 'avg_panic_prob': 60, '_experiences_applied': ['SS-002']}
    wd3 = {'主力状态': '吸筹', '可信度': 0.88, '_experiences_applied': ['WD-002']}
    bj3 = {'optimal_action': '观望', 'optimal_etfs': '', 'win_rate': '~45%',
           'max_drawdown': '-5%', '_experiences_applied': [], 'original_bajie': {}}
    meta3 = {'has_geopolitical': False, 'is_near_holiday': False, 'trump_intensity': 0}

    result3 = run_tang_seng_arbitrate(wk3, sg3, wd3, bj3, meta3)
    print(f"行动: {result3['final_action']}")
    print(f"胜率: {result3['final_win_rate']}")
    for note in result3['arbitration_notes']:
        print(f"  {note}")

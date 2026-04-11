# -*- coding: utf-8 -*-
"""
validate_outcomes.py - 验证脚本

功能：
1. 读取 pending_validations.json 中所有待验证的决策
2. 获取验证日期的实际市场走势数据
3. 对比预判 vs 实际，计算准确率
4. 归因分析：判断是哪个模块导致了正确/错误
5. 生成验证报告并更新经验库命中率
6. 将已验证决策移入 validation_results.json
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
from datetime import datetime, timedelta

# ============================================================
#  路径配置
# ============================================================
EVOLUTION_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EVOLUTION_DIR, 'data')
EXPERIENCE_FILE = os.path.join(DATA_DIR, 'review-experience.json')
PENDING_FILE = os.path.join(DATA_DIR, 'pending_validations.json')
RESULTS_FILE = os.path.join(DATA_DIR, 'validation_results.json')

NEWS_SERVER_DIR = os.path.join(os.path.dirname(EVOLUTION_DIR), 'news-server')
sys.path.insert(0, NEWS_SERVER_DIR)

from market_agents.data_fetcher import get_market_data


# ============================================================
#  核心函数
# ============================================================

def load_json(filepath, default=None):
    """安全加载JSON"""
    if default is None:
        default = {}
    if not os.path.exists(filepath):
        return default
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f'  ⚠️ 读取 {filepath} 失败: {e}')
        return default


def save_json(filepath, data):
    """安全保存JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_actual_market_outcome(date_str, etf_codes=None):
    """
    获取指定日期之后5个交易日的实际走势
    
    返回:
    {
        'direction': 'up'/'down'/'flat',
        'return_pct': 2.5,  # 5日累计涨跌幅%
        'max_drawdown': -1.2,  # 最大回撤%
        'peak_day': 2,  # 第几天达到最高
        'etf_performances': {'512760': 3.1, ...}
    }
    """
    if etf_codes is None:
        etf_codes = ['512760', '512930', '518880', '588890', '159382']
    
    try:
        # 获取15天数据（5个验证日后留余量）
        market_data = get_market_data(etf_codes, 15)
        
        if not market_data:
            return {'direction': 'unknown', 'return_pct': 0, 'max_drawdown': 0,
                    'peak_day': 0, 'etf_performances': {}, 'note': '无法获取市场数据'}
        
        # 找到决策日期后的第5天
        # market_data 格式: {code: [{'date': '2026-04-10', 'close': 1.0, ...}, ...]}
        avg_returns = []
        etf_returns = {}
        max_drawdowns = []
        peak_days = []
        
        for code, klines in market_data.items():
            if len(klines) < 6:
                continue
            
            # 找到决策日期在klines中的位置
            start_idx = -1
            for i, k in enumerate(klines):
                if k.get('date', '') >= date_str:
                    start_idx = i
                    break
            
            if start_idx < 0:
                start_idx = len(klines) - 6  # 用最后6根K线
            
            # 取5根K线（如果有的话）
            end_idx = min(start_idx + 5, len(klines))
            chunk = klines[start_idx:end_idx]
            
            if len(chunk) < 2:
                continue
            
            open_price = chunk[0].get('open', chunk[0].get('close', 0))
            close_price = chunk[-1].get('close', 0)
            
            if open_price <= 0:
                continue
            
            ret = (close_price - open_price) / open_price * 100
            avg_returns.append(ret)
            etf_returns[code] = round(ret, 2)
            
            # 最大回撤
            peak = max(k.get('close', 0) or k.get('high', 0) for k in chunk)
            trough = min(k.get('close', 0) or k.get('low', 0) for k in chunk)
            if peak > 0:
                dd = (trough - peak) / peak * 100
                max_drawdowns.append(dd)
            
            # 最高点出现在第几天
            closes = [k.get('close', 0) for k in chunk]
            max_close = max(closes)
            peak_day = closes.index(max_close) + 1
            peak_days.append(peak_day)
        
        if not avg_returns:
            return {'direction': 'unknown', 'return_pct': 0, 'max_drawdown': 0,
                    'peak_day': 0, 'etf_performances': {}, 'note': '数据不足'}
        
        avg_ret = sum(avg_returns) / len(avg_returns)
        avg_dd = sum(max_drawdowns) / len(max_drawdowns) if max_drawdowns else 0
        avg_peak = int(sum(peak_days) / len(peak_days)) if peak_days else 0
        
        if avg_ret > 1.5:
            direction = 'up'
        elif avg_ret < -1.5:
            direction = 'down'
        else:
            direction = 'flat'
        
        return {
            'direction': direction,
            'return_pct': round(avg_ret, 2),
            'max_drawdown': round(avg_dd, 2),
            'peak_day': avg_peak,
            'etf_performances': etf_returns,
            'sample_count': len(avg_returns)
        }
    except Exception as e:
        return {'direction': 'unknown', 'return_pct': 0, 'max_drawdown': 0,
                'peak_day': 0, 'etf_performances': {}, 'note': f'获取数据异常: {e}'}


def check_prediction_accuracy(predictions, actual):
    """
    对比预判 vs 实际
    
    返回:
    {
        'is_correct': True/False,
        'score': 1.0,  # 0~1 的准确度评分
        'details': '...说明...',
        'module_scores': {
            'wukong': {'correct': True, 'score': 0.8, 'reason': '...'},
            'sangsha': {...},
            'white_dragon': {...},
            'bajie': {...},
            'tang_seng': {...}
        }
    }
    """
    pred_direction = predictions.get('market_direction', '').lower()
    pred_wr = float(predictions.get('win_rate', '50').replace('%', '').replace('％', ''))
    actual_direction = actual.get('direction', 'unknown')
    actual_return = actual.get('return_pct', 0)
    actual_dd = actual.get('max_drawdown', 0)
    
    # 方向判断
    direction_map = {
        '买入': 'up', '加仓': 'up', '做多': 'up',
        '卖出': 'down', '减仓': 'down', '做空': 'down', '空仓': 'down',
        '持有': 'flat', '观望': 'flat', '维持': 'flat',
    }
    pred_dir_code = direction_map.get(pred_direction, 'flat')
    
    # 方向正确性
    dir_correct = (pred_dir_code == actual_direction) or (pred_dir_code == 'flat' and actual_return > -1)
    
    # 胜率偏差
    wr_deviation = 0
    if actual_direction == 'up' and pred_dir_code == 'up':
        wr_deviation = 0  # 预测涨实际涨，胜率合理
    elif actual_direction == 'down' and pred_dir_code == 'down':
        wr_deviation = -10  # 预测跌实际跌，经验可能过于保守
    elif actual_direction == 'down' and pred_dir_code == 'up':
        wr_deviation = 30  # 大错
    elif actual_direction == 'up' and pred_dir_code == 'down':
        wr_deviation = 25  # 大错
    
    # 综合评分
    base_score = 1.0 if dir_correct else 0.0
    # 加上幅度评分（即使方向对，幅度也得看看）
    if dir_correct and actual_direction == 'up':
        amplitude_score = min(abs(actual_return) / 5, 1.0) * 0.3  # 最多加0.3
    elif dir_correct and actual_direction == 'down':
        amplitude_score = 0.2 if abs(actual_return) < 3 else 0.0  # 跌幅不大加0.2
    else:
        amplitude_score = 0
    
    total_score = min(base_score + amplitude_score, 1.0)
    
    is_correct = total_score >= 0.5
    
    detail_parts = []
    if dir_correct:
        detail_parts.append(f'方向正确(预判{pred_direction}→实际{actual_direction}, {actual_return}%)')
    else:
        detail_parts.append(f'方向错误(预判{pred_direction}→实际{actual_direction}, {actual_return}%)')
    
    return {
        'is_correct': is_correct,
        'score': round(total_score, 2),
        'direction_match': dir_correct,
        'pred_direction': pred_direction,
        'actual_direction': actual_direction,
        'actual_return': actual_return,
        'actual_drawdown': actual_dd,
        'details': ' | '.join(detail_parts)
    }


def attribute_to_module(accuracy, evolution_applied):
    """
    归因分析：判断正确/错误主要归功/归咎于哪个模块
    
    策略：
    - 每个模块按经验类型分类
    - 如果方向判断错→优先归因悟空（分析框架）
    - 如果情绪方向错→归因沙僧
    - 如果主力状态误判→归因白龙马
    - 如果胜率偏差大→归因八戒
    - 如果跨层矛盾处理错→归因唐僧
    """
    is_correct = accuracy.get('is_correct', False)
    dir_match = accuracy.get('direction_match', False)
    
    module_scores = {}
    
    # 悟空：负责方向判断
    wk_exps = evolution_applied.get('wukong_experiences', [])
    if dir_match:
        module_scores['wukong'] = {
            'correct': True,
            'score': 0.9,
            'reason': f'方向判断正确，{len(wk_exps)}条分析经验有贡献',
            'experiences_used': wk_exps
        }
    else:
        # 方向错了，检查是否有地缘/Trump经验被错误应用
        geo_exps = [e for e in wk_exps if '地缘' in e or 'WX' in e]
        reason = '方向判断错误'
        if geo_exps:
            reason += f'，地缘经验({geo_exps})可能误判场景'
        module_scores['wukong'] = {
            'correct': False,
            'score': 0.2,
            'reason': reason,
            'experiences_used': wk_exps,
            'needs_review': True
        }
    
    # 沙僧：负责情绪预判
    ss_exps = evolution_applied.get('sangsha_experiences', [])
    actual_return = accuracy.get('actual_return', 0)
    ss_correct = (actual_return > 0 and is_correct) or (actual_return < -3 and not is_correct)
    module_scores['sangsha'] = {
        'correct': ss_correct,
        'score': 0.7 if ss_correct else 0.3,
        'reason': f'情绪方向{"正确" if ss_correct else "偏离"}，{len(ss_exps)}条情绪经验',
        'experiences_used': ss_exps
    }
    
    # 白龙马：负责主力状态
    wd_exps = evolution_applied.get('white_dragon_experiences', [])
    # 简单判断：如果实际跌幅>3%且预判买入，白龙马没发出警告
    wd_missed = (actual_return < -3 and accuracy.get('pred_direction') in ['买入', '加仓'])
    module_scores['white_dragon'] = {
        'correct': not wd_missed,
        'score': 0.1 if wd_missed else 0.8,
        'reason': '未提前预警主力出货风险' if wd_missed else f'{len(wd_exps)}条主力经验有贡献',
        'experiences_used': wd_exps,
        'needs_review': wd_missed
    }
    
    # 八戒：负责概率校准
    bj_exps = evolution_applied.get('bajie_experiences', [])
    pred_wr = float(accuracy.get('pred_wr', '50').replace('%', '').replace('％', '')) if accuracy.get('pred_wr') else 50
    wr_reasonable = is_correct or (not is_correct and pred_wr < 60)
    module_scores['bajie'] = {
        'correct': wr_reasonable,
        'score': 0.6 if wr_reasonable else 0.4,
        'reason': f'胜率校准{"合理" if wr_reasonable else "偏高"}(预估{pred_wr}%)',
        'experiences_used': bj_exps,
        'needs_review': not wr_reasonable
    }
    
    # 唐僧：负责最终仲裁
    tang_rules = evolution_applied.get('tang_rules', [])
    tang_notes = evolution_applied.get('arbitration_notes', [])
    module_scores['tang_seng'] = {
        'correct': is_correct,
        'score': accuracy.get('score', 0.5),
        'reason': f'最终决策{"正确" if is_correct else "失误"}，应用{len(tang_rules)}条仲裁规则',
        'rules_applied': tang_rules,
        'notes': tang_notes
    }
    
    # 找出最需要复盘的模块
    # 优先归因逻辑：方向错→悟空优先；主力预警缺失→白龙马优先；概率偏高→八戒优先
    worst_module = min(module_scores.items(), key=lambda x: x[1]['score'])
    
    # 如果白龙马或悟空都有问题，优先归因到具体模块而非唐僧
    if worst_module[0] == 'tang_seng' and not dir_match:
        tang_score = module_scores['tang_seng']['score']
        for m in ['white_dragon', 'wukong', 'sangsha']:
            if module_scores[m].get('needs_review'):
                worst_module = (m, module_scores[m])
                break
    
    best_module = max(module_scores.items(), key=lambda x: x[1]['score'])
    
    return {
        'module_scores': module_scores,
        'primary_credit': best_module[0] if is_correct else None,
        'primary_blame': worst_module[0] if not is_correct else None,
        'needs_review': [m for m, s in module_scores.items() if s.get('needs_review')]
    }


def update_experience_stats(experience_file, exp_ids_applied, is_correct):
    """
    更新经验知识库的命中率统计
    
    exp_ids_applied: 本次决策中使用的经验ID列表
    is_correct: 本次决策是否正确
    """
    experiences = load_json(experience_file, {'experiences': [], 'lessons': []})
    
    for exp_id in exp_ids_applied:
        for exp in experiences.get('experiences', []):
            if exp.get('id') == exp_id:
                stats = exp.setdefault('stats', {'applied': 0, 'correct': 0, 'wrong': 0, 'hit_rate': 0})
                stats['applied'] = stats.get('applied', 0) + 1
                if is_correct:
                    stats['correct'] = stats.get('correct', 0) + 1
                else:
                    stats['wrong'] = stats.get('wrong', 0) + 1
                total = stats['applied']
                stats['hit_rate'] = round(stats['correct'] / total * 100, 1) if total > 0 else 0
                break
    
    save_json(experience_file, experiences)
    return True


def validate_single(decision, actual_outcome):
    """
    验证单个决策
    
    返回验证结果字典
    """
    predictions = decision.get('predictions', {})
    evolution = decision.get('evolution_applied', {})
    
    # 1. 对比预判 vs 实际
    accuracy = check_prediction_accuracy(predictions, actual_outcome)
    
    # 2. 归因分析
    attribution = attribute_to_module(accuracy, evolution)
    
    # 3. 收集所有用到的经验ID
    all_exp_ids = []
    for key in ['wukong_experiences', 'sangsha_experiences', 'white_dragon_experiences',
                'bajie_experiences']:
        for exp in evolution.get(key, []):
            if isinstance(exp, str) and exp.startswith(('WX-', 'SS-', 'WD-', 'BJ-')):
                all_exp_ids.append(exp)
            elif isinstance(exp, dict) and exp.get('id'):
                all_exp_ids.append(exp['id'])
    
    # 4. 更新经验库统计
    if all_exp_ids:
        update_experience_stats(EXPERIENCE_FILE, all_exp_ids, accuracy['is_correct'])
    
    return {
        'decision_id': decision.get('decision_id'),
        'date': decision.get('date'),
        'predictions': predictions,
        'actual_outcome': actual_outcome,
        'accuracy': accuracy,
        'attribution': attribution,
        'validated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'experiences_applied': all_exp_ids
    }


# ============================================================
#  主流程
# ============================================================

def run_validation():
    """主验证流程"""
    print('=' * 60)
    print('🔍 验证系统 - 对比预判 vs 实际走势')
    print('=' * 60)
    
    # 加载待验证队列
    pending = load_json(PENDING_FILE, {'pending': []})
    pending_list = pending.get('pending', [])
    
    if not pending_list:
        print('\n📭 没有待验证的决策')
        return
    
    print(f'\n📋 待验证: {len(pending_list)} 条决策')
    
    # 加载已有验证结果
    results = load_json(RESULTS_FILE, {'validated': []})
    validated_list = results.get('validated', [])
    
    today = datetime.now().strftime('%Y-%m-%d')
    new_validations = []
    remaining = []
    
    for decision in pending_list:
        dec_date = decision.get('date', '')
        validate_by = decision.get('validate_by_date', '')
        dec_id = decision.get('decision_id', '?')
        
        # 检查是否到期
        if validate_by > today:
            remaining.append(decision)
            print(f'  ⏳ {dec_id} ({dec_date}) → 验证截止日 {validate_by}，未到期')
            continue
        
        print(f'\n  🔍 {dec_id} ({dec_date}):')
        
        # 获取实际走势
        actual = get_actual_market_outcome(dec_date)
        print(f'     实际走势: {actual.get("direction")} ({actual.get("return_pct")}%) '
              f'回撤{actual.get("max_drawdown")}%')
        
        # 验证
        result = validate_single(decision, actual)
        is_ok = result['accuracy']['is_correct']
        score = result['accuracy']['score']
        blame = result['attribution'].get('primary_blame', '无')
        credit = result['attribution'].get('primary_credit', '无')
        
        print(f'     结果: {"✅正确" if is_ok else "❌错误"} (评分{score})')
        print(f'     归因: {"归功" if is_ok else "归咎"} {blame if not is_ok else credit}')
        if result['attribution'].get('needs_review'):
            print(f'     ⚠️ 需复盘模块: {result["attribution"]["needs_review"]}')
        
        new_validations.append(result)
    
    # 保存验证结果
    validated_list.extend(new_validations)
    results['validated'] = validated_list
    results['last_updated'] = today
    save_json(RESULTS_FILE, results)
    
    # 更新待验证队列（移除已验证的）
    pending['pending'] = remaining
    pending['last_updated'] = today
    save_json(PENDING_FILE, pending)
    
    # 统计报告
    print('\n' + '=' * 60)
    print('📊 验证报告')
    print('=' * 60)
    
    if new_validations:
        correct = sum(1 for v in new_validations if v['accuracy']['is_correct'])
        total = len(new_validations)
        avg_score = sum(v['accuracy']['score'] for v in new_validations) / total
        
        print(f'  本次验证: {total} 条')
        print(f'  正确: {correct} | 错误: {total - correct}')
        print(f'  平均评分: {avg_score:.2f}')
        print(f'  剩余待验证: {len(remaining)} 条')
        
        # 模块归因汇总
        module_errors = {}
        module_credits = {}
        for v in new_validations:
            blame = v['attribution'].get('primary_blame')
            credit = v['attribution'].get('primary_credit')
            if blame:
                module_errors[blame] = module_errors.get(blame, 0) + 1
            if credit:
                module_credits[credit] = module_credits.get(credit, 0) + 1
        
        if module_errors:
            print(f'\n  📉 错误归因:')
            for m, c in sorted(module_errors.items(), key=lambda x: -x[1]):
                emoji = {'wukong': '🐒', 'sangsha': '🧔', 'white_dragon': '🐉',
                         'bajie': '🐷', 'tang_seng': '🙏'}.get(m, '❓')
                print(f'     {emoji} {m}: {c}次')
        
        if module_credits:
            print(f'\n  📈 正确归功:')
            for m, c in sorted(module_credits.items(), key=lambda x: -x[1]):
                emoji = {'wukong': '🐒', 'sangsha': '🧔', 'white_dragon': '🐉',
                         'bajie': '🐷', 'tang_seng': '🙏'}.get(m, '❓')
                print(f'     {emoji} {m}: {c}次')
        
        # 累计统计
        all_validated = results.get('validated', [])
        if all_validated:
            total_all = len(all_validated)
            correct_all = sum(1 for v in all_validated if v['accuracy']['is_correct'])
            print(f'\n  📊 累计: {total_all}条 | 正确率 {correct_all}/{total_all} = {correct_all/total_all*100:.1f}%')
    else:
        print('  本次无新验证')
    
    # 返回结果供 weekly_review 使用
    return new_validations


# ============================================================
#  自测
# ============================================================

if __name__ == '__main__':
    # 带模拟数据的自测
    print('--- 自测模式 ---\n')
    
    # 模拟一个待验证决策
    test_pending = {
        'pending': [{
            'decision_id': 'DEC-TEST-001',
            'date': '2026-04-06',
            'predictions': {
                'market_direction': '买入',
                'win_rate': '65',
                'key_etf': '512760,512930'
            },
            'evolution_applied': {
                'wukong_experiences': ['WX-001'],
                'sangsha_experiences': ['SS-001'],
                'white_dragon_experiences': [],
                'bajie_experiences': ['BJ-001'],
                'tang_rules': []
            },
            'status': 'pending_validation',
            'validate_by_date': '2026-04-11'
        }]
    }
    
    # 临时写入
    import shutil
    if os.path.exists(PENDING_FILE):
        shutil.copy2(PENDING_FILE, PENDING_FILE + '.bak_test')
    
    save_json(PENDING_FILE, test_pending)
    
    try:
        print('测试1: 验证流程（模拟买入预判）\n')
        result = validate_single(test_pending['pending'][0], {
            'direction': 'up',
            'return_pct': 3.2,
            'max_drawdown': -0.8,
            'peak_day': 3,
            'etf_performances': {'512760': 3.5, '512930': 2.9}
        })
        
        print(f'  方向: {"✅" if result["accuracy"]["direction_match"] else "❌"}')
        print(f'  评分: {result["accuracy"]["score"]}')
        print(f'  归功: {result["attribution"].get("primary_credit")}')
        print(f'  归咎: {result["attribution"].get("primary_blame")}')
        assert result['accuracy']['is_correct'] == True, '买入预测涨应该正确'
        print('  ✅ 测试1通过\n')
        
        print('测试2: 方向错误的归因\n')
        result2 = validate_single(test_pending['pending'][0], {
            'direction': 'down',
            'return_pct': -4.1,
            'max_drawdown': -5.2,
            'peak_day': 1,
            'etf_performances': {'512760': -4.3, '512930': -3.9}
        })
        
        print(f'  方向: {"✅" if result2["accuracy"]["direction_match"] else "❌"}')
        print(f'  归咎: {result2["attribution"].get("primary_blame")}')
        blame = result2["attribution"].get("primary_blame")
        assert blame in ['wukong', 'white_dragon', 'tang_seng'], f'买入但跌应归咎悟空/白龙马/唐僧，实际{blame}'
        print('  ✅ 测试2通过\n')
        
        print('测试3: 方向预测验证函数\n')
        acc1 = check_prediction_accuracy({'market_direction': '买入', 'win_rate': '60'},
                                          {'direction': 'up', 'return_pct': 2.0, 'max_drawdown': -1})
        acc2 = check_prediction_accuracy({'market_direction': '卖出', 'win_rate': '55'},
                                          {'direction': 'down', 'return_pct': -3.0, 'max_drawdown': -3.5})
        acc3 = check_prediction_accuracy({'market_direction': '观望', 'win_rate': '50'},
                                          {'direction': 'flat', 'return_pct': 0.5, 'max_drawdown': -0.3})
        print(f'  买入+涨: {acc1["is_correct"]} | 卖出+跌: {acc2["is_correct"]} | 观望+平: {acc3["is_correct"]}')
        assert acc1['is_correct'] and acc2['is_correct'] and acc3['is_correct']
        print('  ✅ 测试3通过\n')
        
        print('=' * 40)
        print('🎉 所有自测通过!')
        
    finally:
        # 恢复
        if os.path.exists(PENDING_FILE + '.bak_test'):
            shutil.copy2(PENDING_FILE + '.bak_test', PENDING_FILE)
            os.remove(PENDING_FILE + '.bak_test')

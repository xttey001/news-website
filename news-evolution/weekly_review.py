# -*- coding: utf-8 -*-
"""
weekly_review.py - 周五复盘定时任务

功能：
1. 运行验证脚本（validate_outcomes.py）对比预判vs实际
2. 汇总本周归因统计（哪个模块正确率最高/最低）
3. 更新经验知识库命中率
4. 生成复盘数据JSON（供 review.html 读取展示）
5. 将验证结果写回新闻数据文件（evolution_v4.validation_result）
6. 推送到 wnews 仓库

使用：
  python weekly_review.py              # 手动运行
  cron: 每周五 17:00 自动运行
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
import subprocess
from datetime import datetime, timedelta

# ============================================================
#  路径配置
# ============================================================
EVOLUTION_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EVOLUTION_DIR, 'data')
EXPERIENCE_FILE = os.path.join(DATA_DIR, 'review-experience.json')
RESULTS_FILE = os.path.join(DATA_DIR, 'validation_results.json')
NEWS_SERVER_DIR = os.path.join(os.path.dirname(EVOLUTION_DIR), 'news-server')
WNEWS_DIR = r'c:\Users\asus\wnews'

sys.path.insert(0, EVOLUTION_DIR)
sys.path.insert(0, NEWS_SERVER_DIR)


def load_json(filepath, default=None):
    if default is None:
        default = {}
    if not os.path.exists(filepath):
        return default
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return default


def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_current_week_dates():
    """获取本周一到今天的日期列表"""
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    dates = []
    for i in range((today - monday).days + 1):
        d = monday + timedelta(days=i)
        dates.append(d.strftime('%Y-%m-%d'))
    return dates


def run_validation():
    """运行验证脚本"""
    print('\n=== Step 1: 运行验证脚本 ===')
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(EVOLUTION_DIR, 'validate_outcomes.py')],
            capture_output=True, text=True, encoding='utf-8', cwd=EVOLUTION_DIR
        )
        if result.stdout:
            print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
        if result.returncode != 0 and result.stderr:
            print(f'  验证脚本 stderr: {result.stderr[-300:]}')
        return result.returncode == 0
    except Exception as e:
        print(f'  ⚠️ 验证脚本执行失败: {e}')
        return False


def generate_weekly_attribution_report():
    """生成本周归因统计报告"""
    print('\n=== Step 2: 生成本周归因报告 ===')

    results = load_json(RESULTS_FILE, {'validated': []})
    all_validated = results.get('validated', [])
    today = datetime.now().strftime('%Y-%m-%d')

    # 本周的验证结果
    week_dates = get_current_week_dates()
    week_validated = [v for v in all_validated if v.get('date') in week_dates]

    if not week_validated:
        print('  本周无验证结果')
        return None

    # 模块归因统计
    module_stats = {
        'wukong': {'correct': 0, 'wrong': 0, 'name': '悟空', 'icon': '🐒', 'role': '深度分析'},
        'sangsha': {'correct': 0, 'wrong': 0, 'name': '沙僧', 'icon': '🧔', 'role': '散户情绪'},
        'white_dragon': {'correct': 0, 'wrong': 0, 'name': '白龙马', 'icon': '🐉', 'role': '主力预判'},
        'bajie': {'correct': 0, 'wrong': 0, 'name': '八戒', 'icon': '🐷', 'role': '概率融合'},
        'tang_seng': {'correct': 0, 'wrong': 0, 'name': '唐僧', 'icon': '🙏', 'role': '最终仲裁'}
    }

    for v in week_validated:
        attr = v.get('attribution', {})
        ms = attr.get('module_scores', {})

        for mod in module_stats:
            if mod in ms:
                if ms[mod].get('correct', False):
                    module_stats[mod]['correct'] += 1
                else:
                    module_stats[mod]['wrong'] += 1

    # 经验命中率统计
    experience_stats = load_experience_stats()

    # 生成报告
    total = len(week_validated)
    correct = sum(1 for v in week_validated if v['accuracy']['is_correct'])
    report = {
        'week_start': week_dates[0],
        'week_end': today,
        'total_decisions': total,
        'correct': correct,
        'wrong': total - correct,
        'accuracy': round(correct / total * 100, 1) if total > 0 else 0,
        'module_stats': module_stats,
        'experience_stats': experience_stats,
        'details': week_validated,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # 打印报告
    print(f'\n  📊 本周复盘报告 ({week_dates[0]} ~ {today})')
    print(f'  决策数: {total} | 正确: {correct} | 错误: {total-correct} | 准确率: {report["accuracy"]}%')
    print(f'\n  模块归因:')
    for mod, stats in module_stats.items():
        total_m = stats['correct'] + stats['wrong']
        rate = round(stats['correct'] / total_m * 100, 1) if total_m > 0 else 0
        emoji = stats['icon']
        print(f'    {emoji} {stats["name"]}({stats["role"]}): {stats["correct"]}✅ {stats["wrong"]}❌ = {rate}%')

    if experience_stats:
        print(f'\n  经验命中率 Top 5:')
        sorted_exps = sorted(experience_stats, key=lambda x: x.get('hit_rate', 0), reverse=True)[:5]
        for exp in sorted_exps:
            print(f'    {exp["id"]}: {exp.get("hit_rate", 0)}% ({exp.get("applied", 0)}次使用)')

    # 保存报告
    report_file = os.path.join(DATA_DIR, f'weekly_report_{week_dates[0]}.json')
    save_json(report_file, report)
    print(f'\n  ✅ 报告已保存: {report_file}')

    return report


def load_experience_stats():
    """从经验知识库加载统计"""
    exp_data = load_json(EXPERIENCE_FILE, {'experiences': []})
    stats = []
    for exp in exp_data.get('experiences', []):
        s = exp.get('stats', {})
        if s.get('applied', 0) > 0:
            stats.append({
                'id': exp.get('id', '?'),
                'title': exp.get('title', ''),
                'module': exp.get('module', ''),
                'applied': s.get('applied', 0),
                'correct': s.get('correct', 0),
                'wrong': s.get('wrong', 0),
                'hit_rate': s.get('hit_rate', 0)
            })
    return sorted(stats, key=lambda x: x.get('applied', 0), reverse=True)


def is_last_week_of_month():
    """判断本周是否是本月最后一周
    
    判断逻辑：如果当前周五 + 7天 > 本月最后一天 → 最后一周
    """
    today = datetime.now()
    
    # 计算本月最后一天
    if today.month == 12:
        last_day = datetime(today.year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
    
    # 计算本周五
    days_to_friday = (4 - today.weekday()) % 7  # 4 = Friday
    this_friday = today + timedelta(days=days_to_friday)
    
    # 如果本周五 + 7天超过月末 → 最后一周
    next_week = this_friday + timedelta(days=7)
    
    return next_week > last_day, last_day.day


def generate_monthly_report(weekly_reports):
    """生成月度汇总报告
    
    参数：
        weekly_reports: 本月所有周报的列表
    
    返回：
        月度报告字典
    """
    today = datetime.now()
    
    # 合并所有周报数据
    total_decisions = 0
    total_correct = 0
    total_wrong = 0
    module_totals = {}
    
    for report in weekly_reports:
        total_decisions += report.get('total_decisions', 0)
        total_correct += report.get('correct', 0)
        total_wrong += report.get('wrong', 0)
        
        for mod, stats in report.get('module_stats', {}).items():
            if mod not in module_totals:
                module_totals[mod] = {'correct': 0, 'wrong': 0, 'name': stats.get('name', ''), 
                                      'icon': stats.get('icon', ''), 'role': stats.get('role', '')}
            module_totals[mod]['correct'] += stats.get('correct', 0)
            module_totals[mod]['wrong'] += stats.get('wrong', 0)
    
    # 计算月度准确率
    accuracy = round(total_correct / total_decisions * 100, 1) if total_decisions > 0 else 0
    
    # 找出最佳和最差模块
    best_module = None
    worst_module = None
    best_rate = 0
    worst_rate = 100
    
    for mod, stats in module_totals.items():
        total = stats['correct'] + stats['wrong']
        if total > 0:
            rate = stats['correct'] / total * 100
            if rate > best_rate:
                best_rate = rate
                best_module = {'module': mod, 'rate': rate, **stats}
            if rate < worst_rate:
                worst_rate = rate
                worst_module = {'module': mod, 'rate': rate, **stats}
    
    # 生成报告
    report = {
        'month': today.strftime('%Y-%m'),
        'total_decisions': total_decisions,
        'correct': total_correct,
        'wrong': total_wrong,
        'accuracy': accuracy,
        'module_stats': module_totals,
        'best_module': best_module,
        'worst_module': worst_module,
        'weeks_count': len(weekly_reports),
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # 打印报告
    print(f'\n  📊 月度汇总报告 ({today.strftime("%Y年%m月")})')
    print(f'  决策数: {total_decisions} | 正确: {total_correct} | 错误: {total_wrong} | 准确率: {accuracy}%')
    print(f'  周报数: {len(weekly_reports)}')
    
    if best_module:
        print(f'\n  🏆 最佳模块: {best_module["icon"]} {best_module["name"]}({best_module["rate"]:.0f}%)')
    if worst_module:
        print(f'  ⚠️ 需改进模块: {worst_module["icon"]} {worst_module["name"]}({worst_module["rate"]:.0f}%)')
    
    # 保存月报
    report_file = os.path.join(DATA_DIR, f'monthly_report_{today.strftime("%Y-%m")}.json')
    save_json(report_file, report)
    print(f'\n  ✅ 月报已保存: {report_file}')
    
    return report


def load_monthly_weekly_reports():
    """加载本月所有周报"""
    today = datetime.now()
    month_prefix = today.strftime('%Y-%m')
    
    reports = []
    for filename in os.listdir(DATA_DIR):
        if filename.startswith(f'weekly_report_{month_prefix}') and filename.endswith('.json'):
            filepath = os.path.join(DATA_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    reports.append(json.load(f))
            except:
                pass
    
    return reports


def backfill_validation_to_news():
    """将验证结果回填到新闻数据文件中"""
    print('\n=== Step 3: 回填验证结果到新闻数据 ===')

    results = load_json(RESULTS_FILE, {'validated': []})
    news_data_dir = os.path.join(NEWS_SERVER_DIR, 'news_data')

    if not os.path.exists(news_data_dir):
        print(f'  ⚠️ 新闻目录不存在: {news_data_dir}')
        return

    count = 0
    for v in results.get('validated', []):
        date = v.get('date', '')
        if not date:
            continue

        news_file = os.path.join(news_data_dir, f'news_{date}.json')
        if not os.path.exists(news_file):
            continue

        try:
            with open(news_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 检查是否已经回填过
            if data.get('evolution_v4', {}).get('validation_result'):
                continue

            # 回填验证结果
            if 'evolution_v4' not in data:
                data['evolution_v4'] = {}

            data['evolution_v4']['validation_result'] = {
                'is_correct': v['accuracy']['is_correct'],
                'score': v['accuracy']['score'],
                'details': v['accuracy']['details'],
                'actual_return': v['accuracy'].get('actual_return', 0),
                'actual_direction': v['accuracy'].get('actual_direction', ''),
                'primary_blame': v['attribution'].get('primary_blame'),
                'primary_credit': v['attribution'].get('primary_credit'),
                'validated_at': v.get('validated_at', '')
            }

            with open(news_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            count += 1
        except Exception as e:
            print(f'  ⚠️ 回填 {date} 失败: {e}')

    print(f'  ✅ 回填了 {count} 个文件的验证结果')


def push_to_wnews():
    """重新生成 news-data.js 并推送到 wnews"""
    print('\n=== Step 4: 推送到 wnews ===')

    try:
        # 重新生成 news-data.js
        gen_script = os.path.join(NEWS_SERVER_DIR, 'generate_full_newsdata.py')
        if os.path.exists(gen_script):
            result = subprocess.run(
                [sys.executable, gen_script],
                capture_output=True, text=True, encoding='utf-8', cwd=NEWS_SERVER_DIR
            )
            if result.returncode == 0:
                print('  ✅ news-data.js 重新生成')
            else:
                print(f'  ⚠️ 生成失败: {result.stderr[-200:] if result.stderr else "未知错误"}')

        # 推送到 wnews
        src_js = os.path.join(NEWS_SERVER_DIR, 'github-pages-deploy', 'news-data.js')
        if not os.path.exists(src_js):
            src_js = os.path.join(NEWS_SERVER_DIR, 'news-data.js')

        if os.path.exists(src_js) and os.path.exists(WNEWS_DIR):
            import shutil
            shutil.copy2(src_js, os.path.join(WNEWS_DIR, 'news-data.js'))
            os.chdir(WNEWS_DIR)
            os.system('git add -A')
            today = datetime.now().strftime('%Y-%m-%d')
            os.system(f'git commit -m "weekly review: {today} validation results"')
            os.system('git push origin main')
            os.chdir(EVOLUTION_DIR)
            print('  ✅ wnews 推送成功')
        else:
            print('  ⚠️ 跳过推送')
    except Exception as e:
        print(f'  ⚠️ 推送失败: {e}')


def suggest_experience_updates(report):
    """基于验证结果建议经验库更新"""
    print('\n=== Step 5: 经验进化建议 ===')

    if not report:
        return

    module_stats = report.get('module_stats', {})
    suggestions = []

    for mod, stats in module_stats.items():
        total = stats['correct'] + stats['wrong']
        if total == 0:
            continue
        rate = stats['correct'] / total * 100

        if rate < 50 and total >= 2:
            suggestions.append({
                'module': mod,
                'type': 'warning',
                'message': f"{stats['icon']} {stats['name']}本周准确率仅{rate:.0f}%（{total}次），建议检查经验库是否有误导性规则"
            })
        elif rate >= 80 and total >= 2:
            suggestions.append({
                'module': mod,
                'type': 'success',
                'message': f"{stats['icon']} {stats['name']}本周表现出色（{rate:.0f}%），经验规则有效"
            })

    if suggestions:
        print('  基于本周验证结果的建议:')
        for s in suggestions:
            icon = '⚠️' if s['type'] == 'warning' else '✅'
            print(f'    {icon} {s["message"]}')
    else:
        print('  数据不足，暂无建议（需至少2次验证后才会生成）')

    # 保存建议
    if suggestions:
        suggest_file = os.path.join(DATA_DIR, 'evolution_suggestions.json')
        existing = load_json(suggest_file, {'suggestions': []})
        existing['suggestions'].extend(suggestions)
        existing['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        save_json(suggest_file, existing)


# ============================================================
#  主流程
# ============================================================

def main():
    print('=' * 60)
    print(f'📅 周五复盘 - {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    print('=' * 60)
    
    # 检查是否是本月最后一周
    is_last_week, last_day = is_last_week_of_month()
    if is_last_week:
        print(f'\n🌟 本周是本月最后一周（月末{last_day}号），将执行月度总复盘！')

    # Step 1: 运行验证
    run_validation()

    # Step 2: 生成本周归因报告
    report = generate_weekly_attribution_report()

    # Step 3: 回填验证结果到新闻数据
    backfill_validation_to_news()

    # Step 4: 推送到 wnews
    push_to_wnews()

    # Step 5: 经验进化建议
    suggest_experience_updates(report)
    
    # Step 6: 如果是本月最后一周，执行月度汇总
    if is_last_week:
        print('\n' + '=' * 60)
        print('📊 月度总复盘')
        print('=' * 60)
        
        # 加载本月所有周报
        weekly_reports = load_monthly_weekly_reports()
        
        if weekly_reports:
            # 生成月度汇总
            monthly_report = generate_monthly_report(weekly_reports)
            
            # 月度经验进化建议
            print('\n=== 月度经验进化建议 ===')
            
            if monthly_report.get('worst_module'):
                wm = monthly_report['worst_module']
                print(f'  ⚠️ {wm["icon"]} {wm["name"]}本月准确率仅{wm["rate"]:.0f}%')
                print(f'     建议：检查该模块的经验库是否有误导性规则')
            
            if monthly_report.get('best_module'):
                bm = monthly_report['best_module']
                print(f'  ✅ {bm["icon"]} {bm["name"]}本月表现出色（{bm["rate"]:.0f}%）')
                print(f'     建议：将该模块的成功经验推广到其他模块')
        else:
            print('  ⚠️ 未找到本月的周报数据，跳过月度汇总')

    print('\n' + '=' * 60)
    print('📅 周五复盘完成!')
    if is_last_week:
        print('📊 月度总复盘完成!')
    print('=' * 60)


if __name__ == '__main__':
    main()

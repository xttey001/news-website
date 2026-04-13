# -*- coding: utf-8 -*-
"""
每日自动更新脚本 v4 - 五维进化版

与 v3 的区别：
- v3（原有）：新闻→沙僧→白龙马→八戒融合→输出
- v4（进化）：新闻→悟空增强→沙僧增强→白龙马增强→八戒校准→唐僧仲裁→输出+存待验证队列

关键设计：
- 本文件位于 news-evolution/ 独立目录，不修改原有 news-server/ 的任何文件
- 通过 sys.path 引用原有模型和进化模块
- 输出结果写入 news-server/news_data/ （共享数据目录）
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
from datetime import datetime, timedelta
import subprocess
import shutil

# ============================================================
#  路径配置
# ============================================================
# 进化系统根目录
EVOLUTION_DIR = os.path.dirname(os.path.abspath(__file__))
# 原有新闻系统目录
NEWS_SERVER_DIR = os.path.join(os.path.dirname(EVOLUTION_DIR), 'news-server')
# wnews 仓库
WNEWS_DIR = r'c:\Users\asus\wnews'

# 加入路径
sys.path.insert(0, EVOLUTION_DIR)
sys.path.insert(0, NEWS_SERVER_DIR)

# ============================================================
#  ETF 名称校准映射表（防止AI幻觉导致名称错误）
#  数据来源: 东方财富/天天基金 实时验证 (2026-04-12)
#  完整映射表见: .workbuddy/skills/wnews-analysis/SKILL.md
# ============================================================
ETF_CANONICAL_MAP = {
    # === 已验证正确（可直接使用） ===
    '512930': 'AI算力ETF',           # 平安中证人工智能主题ETF ✅
    '515070': '人工智能ETF华夏',      # 华夏中证人工智能主题ETF ✅
    '518880': '黄金ETF',              # 华安黄金ETF ✅
    '588790': '科创AIETF',            # 博时科创板人工智能ETF ✅
    '588890': '科创芯片ETF',          # 南方上证科创板芯片ETF ✅
    '588260': '科创信息ETF',          # ⚠️ 华安上证科创板新一代信息技术ETF（AI常误写为"科创芯片设计ETF"）
    '159322': '黄金股ETF平安',        # 平安中证沪深港黄金产业ETF ✅
    '159382': '创业板人工智能ETF南方', # 南方创业板人工智能ETF ✅
    '159915': '创业板ETF',            # 易方达创业板ETF ✅
    '512880': '证券ETF',              # 国泰中证全指证券公司ETF（也称券商ETF）✅
    '159320': '电网ETF',              # ⚠️ 广发恒生A股电网设备ETF（这才是真正的电网ETF！）

    # === 易混淆代码（⚠️ AI 高频错误区） ===
    '159542': '工程机械ETF',          # ⚠️ 大成中证工程机械ETF（AI常误写为"电网ETF"，真电网是159320）
    '159871': '有色ETF',              # ⚠️ 银华中证有色金属ETF（AI常误写为"电池ETF"）
    '589260': '科创芯设ETF',          # ⚠️ 国泰上证科创板芯片设计主题ETF（AI常误写为"科创信息ETF"，注意：588260才是科创信息！）
}

def correct_etf_names(text):
    """
    校正文本中的ETF名称错误。
    
    扫描所有 ETF(XXXXXX) 格式，将错误名称替换为标准名称。
    
    Args:
        text: str 或 dict/list，待校正的内容
    
    Returns:
        校正后的内容（同类型）
    """
    import re
    
    if isinstance(text, str):
        def replace_etf(match):
            full_match = match.group(0)  # 如 "电网ETF(159542)"
            code = match.group(1)         # 如 "159542"
            
            if code in ETF_CANONICAL_MAP:
                correct_name = ETF_CANONICAL_MAP[code]
                return f'{correct_name}({code})'
            return full_match
        
        # 匹配格式: XXXETF(数字) 或 XXX(数字)
        return re.sub(r'([^\s,(（）]{2,10})[ETF]*[(（](\d{6})[)）]', replace_etf, text)
    
    elif isinstance(text, dict):
        return {k: correct_etf_names(v) for k, v in text.items()}
    
    elif isinstance(text, list):
        return [correct_etf_names(item) for item in text]
    
    return text


print('=== Daily Update v4 - 五维进化版 ===')
print(f'  进化系统: {EVOLUTION_DIR}')
print(f'  原有系统: {NEWS_SERVER_DIR}')

# ============================================================
#  Step 1: 搜索最新新闻（调用原有脚本）
# ============================================================
print('\nStep 1: Searching latest news...')
try:
    os.chdir(NEWS_SERVER_DIR)
    subprocess.run([sys.executable, 'search_today.py'], check=True)
    os.chdir(EVOLUTION_DIR)
    print('  ✅ News search done')
except Exception as e:
    os.chdir(EVOLUTION_DIR)
    print(f'  ⚠️ News search failed: {e}')

# ============================================================
#  Step 2: 导入模块
# ============================================================
print('\nStep 2: Importing models...')

# 原有模型
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon
from market_agents.bajie_model import run_bajie_cross

# 进化模块
from market_agents_evolution import (
    run_wukong_enhanced,
    run_sangsha_enhanced,
    run_white_dragon_enhanced,
    run_bajie_enhanced,
    run_tang_seng_arbitrate
)

print('  ✅ All models imported')

# ============================================================
#  Step 3: 加载今天的新闻
# ============================================================
today = datetime.now().strftime('%Y-%m-%d')
news_file = os.path.join(NEWS_SERVER_DIR, 'news_data', f'news_{today}.json')

if not os.path.exists(news_file):
    print(f'\n❌ No news file for today: {news_file}')
    print('Please run search_today.py first')
    sys.exit(1)

with open(news_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
today_news = {today: data}

wukong = data.get('wukong_judgment', {})
orig_bajie = data.get('bajie_conclusion', {})

# 【新增】ETF名称校准：纠正AI生成的错误ETF名称映射
wukong = correct_etf_names(wukong)
orig_bajie = correct_etf_names(orig_bajie)
print(f'\nStep 3: News loaded | 悟空: {bool(wukong)} | 原始八戒: {bool(orig_bajie)} | [ETF校准已启用]')

# ============================================================
#  Step 4: 构建场景元数据（供经验匹配用）
# ============================================================
print('\nStep 4: Building scene metadata...')

news_texts = json.dumps(data, ensure_ascii=False).lower()

news_metadata = {
    'date': today,
    'has_geopolitical': any(kw in news_texts for kw in ['战争', '制裁', '冲突', '海峡', '军事', '地缘', '霍尔木兹']),
    'has_earnings_beat': any(kw in news_texts for kw in ['业绩超预期', '净利润', '营收增长', '财报']),
    'trump_intensity': sum(1 for kw in ['trump', '特朗普', '关税', '威胁'] if kw in news_texts),
    'has_policy_benefit': any(kw in news_texts for kw in ['政策利好', '扶持', '补贴', '降准', '降息']),
    'has_tech_breakthrough': any(kw in news_texts for kw in ['突破', '创新', '首发', '量产']),
    'is_near_holiday': False,  # TODO: 接入节假日日历
    'is_earnings_season': today[5:7] in ['03', '04', '08', '09'],
    'is_near_weekend': datetime.now().weekday() >= 4,
    'prior_type': 'geopolitical' if any(kw in news_texts for kw in ['战争', '制裁', '冲突', '海峡']) else 'default',
    'prior_updated_at': datetime.now().isoformat(),
}

meta_summary = {k: v for k, v in news_metadata.items() if v}
print(f'  📋 场景标签: {meta_summary}')

# ============================================================
#  Step 5: 原有四层分析
# ============================================================
print('\nStep 5: Running base 4-layer analysis...')

# 获取市场数据
codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
    print(f'  Market data: {len(market_data)} codes')
except Exception as e:
    print(f'  ⚠️ Market data error: {e}')
    market_data = {}

# 5a. 沙僧（原始）
try:
    sangsha_result = run_sangsha(today_news, today, market_data)
    sangsha = sangsha_result.get('沙僧模块', sangsha_result.get('sengseng', {}))
except Exception as e:
    print(f'  ⚠️ Sangsha error: {e}')
    sangsha = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 50,
               'avg_panic_prob': 30, 'analysis_results': [], 'total_news_count': 0}
print(f'  🧔 沙僧(原始): {sangsha.get("overall_sentiment")} (买入{sangsha.get("avg_buy_prob",0)}%)')

# 5b. 白龙马（原始）
try:
    wd_result = run_white_dragon(market_data, sangsha.get('analysis_results', []),
                                  wukong, orig_bajie)
    white_dragon = wd_result.get('白龙马决策', {})
except Exception as e:
    print(f'  ⚠️ WhiteDragon error: {e}')
    white_dragon = {'主力状态': '观望', '阶段': '观察', '综合建议': '暂无数据', '可信度': 1.0}
print(f'  🐉 白龙马(原始): {white_dragon.get("主力状态")} (可信度{white_dragon.get("可信度")})')

# 5c. 八戒融合（原始）
try:
    fused_bajie = run_bajie_cross(wukong, orig_bajie, sangsha, white_dragon)
    base_bajie = {
        'optimal_action': fused_bajie.get('optimal_action', ''),
        'optimal_etfs': fused_bajie.get('optimal_etfs', ''),
        'win_rate': fused_bajie.get('win_rate', ''),
        'max_drawdown': fused_bajie.get('max_drawdown', ''),
        'holding_period': orig_bajie.get('holding_period', ''),
        '沙僧信号': fused_bajie.get('沙僧信号', {}),
        '白龙马信号': fused_bajie.get('白龙马信号', {}),
        '悟空信号': fused_bajie.get('悟空信号', {}),
        '信号一致性': fused_bajie.get('信号一致性', ''),
        '融合说明': fused_bajie.get('融合说明', []),
        'original_bajie': fused_bajie.get('original_bajie', {})
    }
except Exception as e:
    print(f'  ⚠️ Bajie fusion error: {e}')
    base_bajie = orig_bajie
print(f'  🐷 八戒(原始): 胜率={base_bajie.get("win_rate")}')

# ============================================================
#  Step 6: 五维进化增强（核心！）
# ============================================================
print('\nStep 6: 🧬 Running evolution enhancement...')

# 6a. 悟空增强
try:
    wukong_enh = run_wukong_enhanced(wukong, news_metadata)
    wk_exp = wukong_enh.get('_experiences_applied', [])
    print(f'  🐵 悟空进化: +{len(wk_exp)}条经验 {wk_exp}')
except Exception as e:
    print(f'  ⚠️ Wukong enhanced error: {e}')
    wukong_enh = wukong

# 6b. 沙僧增强
try:
    sangsha_enh = run_sangsha_enhanced(sangsha, news_metadata)
    sg_exp = sangsha_enh.get('_experiences_applied', [])
    fomo = sangsha_enh.get('fomo_warning', {})
    reverse = sangsha_enh.get('reverse_opportunity', {})
    tp = sangsha_enh.get('turning_point_warning', {})
    notes = []
    if fomo: notes.append(f'FOMO:{fomo.get("level")}')
    if reverse: notes.append(f'逆向:{"★"*reverse.get("quality_stars",0)}')
    if tp: notes.append(f'拐点:{tp.get("factor_count")}因子')
    print(f'  🧔 沙僧进化: +{len(sg_exp)}条经验 {sg_exp} | {" ".join(notes)}')
except Exception as e:
    print(f'  ⚠️ Sangsha enhanced error: {e}')
    sangsha_enh = sangsha

# 6c. 白龙马增强
try:
    wd_enh = run_white_dragon_enhanced(white_dragon, news_metadata, sangsha)
    wd_exp = wd_enh.get('_experiences_applied', [])
    trump_mode = wd_enh.get('trump_mainforce_mode', {})
    if trump_mode:
        print(f'  🐉 白龙马进化: +{len(wd_exp)}条经验 {wd_exp} | Trump模式:{trump_mode.get("mode","无")}')
    else:
        print(f'  🐉 白龙马进化: +{len(wd_exp)}条经验 {wd_exp}')
except Exception as e:
    print(f'  ⚠️ WhiteDragon enhanced error: {e}')
    wd_enh = white_dragon

# 6d. 八戒校准
try:
    bajie_enh = run_bajie_enhanced(base_bajie, news_metadata,
                                    sangsha_enh, wd_enh, wukong_enh)
    bj_exp = bajie_enh.get('_experiences_applied', [])
    prior_cal = bajie_enh.get('prior_calibration', {})
    sig_w = bajie_enh.get('signal_weights', {})
    geo_check = bajie_enh.get('geo_prior_check', {})
    print(f'  🐷 八戒校准: +{len(bj_exp)}条经验 {bj_exp}')
    if prior_cal:
        print(f'     先验: {prior_cal.get("scene_desc")} {prior_cal.get("original_prior")}→{prior_cal.get("calibrated_prior")}')
    if geo_check and geo_check.get('is_expired'):
        print(f'     ⚠️ 地缘先验已过期{geo_check.get("hours_since_last_update")}h')
except Exception as e:
    print(f'  ⚠️ Bajie enhanced error: {e}')
    bajie_enh = base_bajie

# 6e. 唐僧仲裁
try:
    tang_result = run_tang_seng_arbitrate(
        wukong_enhanced=wukong_enh,
        sangsha_enhanced=sangsha_enh,
        white_dragon_enhanced=wd_enh,
        bajie_calibrated=bajie_enh,
        news_metadata=news_metadata
    )
    tang_exp = tang_result.get('applied_rules', [])
    tang_action = tang_result.get('final_decision', {}).get('optimal_action', '?')
    tang_wr = tang_result.get('final_decision', {}).get('win_rate', '?')
    print(f'  🙏 唐僧仲裁: +{len(tang_exp)}条规则 | 行动={tang_action} | 胜率={tang_wr}')
except Exception as e:
    print(f'  ⚠️ TangSeng arbitrate error: {e}')
    tang_result = {'final_decision': bajie_enh, 'applied_rules': [], 'arbitration_notes': [f'仲裁失败: {e}']}

# ============================================================
#  Step 7: 组装最终输出
# ============================================================
print('\nStep 7: Assembling final output...')

final_output = {
    # 唐僧最终决策
    'final_decision': tang_result.get('final_decision', bajie_enh),
    
    # 进化标注
    'evolution': {
        'version': 'v4',
        'date': today,
        'scene_metadata': meta_summary,
        'wukong_experiences': wukong_enh.get('_experiences_applied', []) if isinstance(wukong_enh, dict) else [],
        'sangsha_experiences': sangsha_enh.get('_experiences_applied', []) if isinstance(sangsha_enh, dict) else [],
        'white_dragon_experiences': wd_enh.get('_experiences_applied', []) if isinstance(wd_enh, dict) else [],
        'bajie_experiences': bajie_enh.get('_experiences_applied', []) if isinstance(bajie_enh, dict) else [],
        'tang_rules': tang_result.get('applied_rules', []),
        'arbitration_notes': tang_result.get('arbitration_notes', []),
    },
    
    # 各模块增强后的完整结果
    'wukong_enhanced': wukong_enh if isinstance(wukong_enh, dict) else {},
    'sangsha_enhanced': sangsha_enh if isinstance(sangsha_enh, dict) else {},
    'white_dragon_enhanced': wd_enh if isinstance(wd_enh, dict) else {},
    'bajie_enhanced': bajie_enh if isinstance(bajie_enh, dict) else {},
}

# ============================================================
#  Step 8: 写入新闻文件（追加进化结果，不覆盖原有字段）
# ============================================================
with open(news_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 保留原有字段，追加进化结果（五维全量输出）
data['sangsha_module'] = sangsha_enh if isinstance(sangsha_enh, dict) else sangsha
data['white_dragon'] = wd_enh if isinstance(wd_enh, dict) else white_dragon
data['bajie_conclusion'] = correct_etf_names(bajie_enh if isinstance(bajie_enh, dict) else base_bajie)  # 保留八戒校准结果+ETF校准
data['wukong_enhanced'] = wukong_enh if isinstance(wukong_enh, dict) else wukong  # 新增：悟空增强

# 【重要】唐僧结果需要转换为前端期望的中文key格式（含ETF名称校准）
tang_final_decision = tang_result.get('final_decision', bajie_enh)
tang_action_text = correct_etf_names(tang_result.get('final_action', tang_final_decision.get('optimal_action', '观望') if isinstance(tang_final_decision, dict) else '?'))
tang_wr_text = tang_result.get('final_win_rate', '~60%')

# 从 action 文本提取仓位建议
if '轻仓' in str(tang_action_text):
    tang_position = '30-50% 轻仓'
elif '重仓' in str(tang_action_text) or '加仓' in str(tang_action_text):
    tang_position = '70%+ 重仓'
elif '减仓' in str(tang_action_text) or '清仓' in str(tang_action_text):
    tang_position = '0-20% 空仓/极轻'
else:
    tang_position = '40-60% 中性'

# 构建前端兼容的唐僧字段
data['tang_sanzang'] = {
    # 前端 index.html 期望的中文 key 格式
    '仓位': tang_position,
    '最终行动': tang_action_text,
    '仲裁矛盾': tang_result.get('arbitration_notes', []),
    '仓位公式': f'base({tang_position}) × 风控调整',
    '风控触发': [c.get('item') + ': ' + c.get('status') + ' - ' + c.get('reason','') 
                 for c in tang_result.get('risk_checks', []) if c.get('status','') != '✅ 通过'],
    # 同时保留原始结构供其他用途
    '_raw': tang_result,
}

data['evolution_v4'] = final_output['evolution']

with open(news_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'  ✅ Updated {news_file} (五维全量: 悟空+沙僧+白龙马+八戒+唐僧)')

# ============================================================
#  Step 9: 存入待验证队列
# ============================================================
pending_file = os.path.join(EVOLUTION_DIR, 'data', 'pending_validations.json')
try:
    if os.path.exists(pending_file):
        with open(pending_file, 'r', encoding='utf-8') as f:
            pending = json.load(f)
    else:
        pending = {'pending': []}
    
    decision_id = f'DEC-{today.replace("-", "")}-{len(pending["pending"])+1:03d}'
    pending['pending'].append({
        'decision_id': decision_id,
        'date': today,
        'predictions': {
            'market_direction': tang_result.get('final_decision', {}).get('optimal_action', ''),
            'win_rate': str(tang_result.get('final_decision', {}).get('win_rate', '')),
            'key_etf': tang_result.get('final_decision', {}).get('optimal_etfs', ''),
        },
        'evolution_applied': final_output['evolution'],
        'status': 'pending_validation',
        'validate_by_date': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
    })
    
    with open(pending_file, 'w', encoding='utf-8') as f:
        json.dump(pending, f, ensure_ascii=False, indent=2)
    print(f'  ✅ Pending validation saved: {decision_id}')
except Exception as e:
    print(f'  ⚠️ Pending save error: {e}')

# ============================================================
#  Step 10: 重新生成 news-data.js（调用原有脚本）
# ============================================================
print('\nStep 10: Regenerating news-data.js...')
try:
    os.chdir(NEWS_SERVER_DIR)
    subprocess.run([sys.executable, 'generate_full_newsdata.py'], check=True)
    os.chdir(EVOLUTION_DIR)
    print('  ✅ news-data.js regenerated')
except Exception as e:
    os.chdir(EVOLUTION_DIR)
    print(f'  ⚠️ Generate error: {e}')

# ============================================================
#  Step 11: 推送到 wnews 仓库
# ============================================================
print('\nStep 11: Pushing to wnews repository...')
try:
    src_js = os.path.join(NEWS_SERVER_DIR, 'github-pages-deploy', 'news-data.js')
    if not os.path.exists(src_js):
        src_js = os.path.join(NEWS_SERVER_DIR, 'news-data.js')
    
    if os.path.exists(src_js) and os.path.exists(WNEWS_DIR):
        shutil.copy2(src_js, os.path.join(WNEWS_DIR, 'news-data.js'))
        os.chdir(WNEWS_DIR)
        os.system('git add -A')
        os.system(f'git commit -m "Auto update v4: {today} with evolution enhancement"')
        os.system('git push origin main')
        os.chdir(EVOLUTION_DIR)
        print('  ✅ wnews pushed')
    else:
        print(f'  ⚠️ Push skipped')
except Exception as e:
    os.chdir(EVOLUTION_DIR)
    print(f'  ⚠️ Push error: {e}')

# ============================================================
#  Done!
# ============================================================
print('\n' + '=' * 60)
print('🧬 Daily Update v4 - 五维进化版 完成!')
print('=' * 60)

# 输出对比
orig_wr = base_bajie.get('win_rate', '?')
final_wr = tang_result.get('final_decision', {}).get('win_rate', orig_wr)
total_exp = sum(len(final_output['evolution'].get(k, [])) for k in 
                ['wukong_experiences', 'sangsha_experiences', 'white_dragon_experiences',
                 'bajie_experiences', 'tang_rules'])

print(f'  原始胜率: {orig_wr} → 进化胜率: {final_wr}')
print(f'  注入经验: {total_exp}条')
print(f'  网站地址: https://xttey001.github.io/wnews/')
print(f'  进化系统: {EVOLUTION_DIR}')

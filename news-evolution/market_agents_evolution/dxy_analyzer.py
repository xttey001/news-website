# -*- coding: utf-8 -*-
"""
美元指数(DXY)分析模块
分析DXY与科创50等资产的相关性，提供交易信号
"""

import requests
import json
from datetime import datetime, timedelta

def get_dxy_data():
    """
    获取美元指数数据
    使用新浪财经API
    """
    try:
        # 新浪财经美元指数
        url = "https://hq.sinajs.cn/list=fx_susdxy"
        headers = {
            'Referer': 'https://finance.sina.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'gbk'
        
        # 解析返回数据: var hq_str_fx_susdxy="103.45,103.23,103.56,103.12,103.45,0.22,0.21,2025-05-06,10:30:00";
        text = response.text
        if 'hq_str_fx_susdxy' in text:
            # 提取引号内的数据
            start = text.find('"') + 1
            end = text.rfind('"')
            data_str = text[start:end]
            parts = data_str.split(',')
            
            if len(parts) >= 9:
                return {
                    'price': float(parts[0]),  # 当前价格
                    'open': float(parts[1]),
                    'high': float(parts[2]),
                    'low': float(parts[3]),
                    'prev_close': float(parts[4]),
                    'change': float(parts[5]),  # 涨跌额
                    'change_pct': float(parts[6]),  # 涨跌幅%
                    'name': '美元指数',
                    'code': 'DXY',
                    'timestamp': datetime.now().isoformat()
                }
    except Exception as e:
        print(f"获取DXY数据失败: {e}")
    
    return None

def analyze_dxy_impact(dxy_data):
    """
    分析DXY对市场的影响
    返回影响评估和交易信号
    """
    if not dxy_data:
        return {
            'impact_level': 'unknown',
            'signal': 'neutral',
            'description': '无法获取DXY数据',
            'recommendation': {}
        }
    
    price = dxy_data['price']
    change = dxy_data.get('change_pct', dxy_data.get('change', 0))
    
    # 水平位判断
    if price < 100:
        level = 'weak_dollar'
        level_desc = '美元弱势区（<100）'
        kc50_bias = 'strong_bullish'
    elif price < 103:
        level = 'neutral'
        level_desc = '中性区间（100-103）'
        kc50_bias = 'neutral'
    elif price < 105:
        level = 'strong_dollar_warning'
        level_desc = '美元偏强（103-105）'
        kc50_bias = 'bearish'
    else:
        level = 'strong_dollar_danger'
        level_desc = '美元强势区（>105）'
        kc50_bias = 'strong_bearish'
    
    # 变动幅度判断
    if change <= -2:
        change_signal = 'extreme_weak'
        change_desc = '美元暴跌（<-2%）'
        urgency = 'immediate'
    elif change <= -1:
        change_signal = 'strong_weak'
        change_desc = '美元大跌（<-1%）'
        urgency = 'high'
    elif change < -0.5:
        change_signal = 'moderate_weak'
        change_desc = '美元走弱（-0.5%~-1%）'
        urgency = 'medium'
    elif change <= 0.5:
        change_signal = 'neutral'
        change_desc = '美元震荡（-0.5%~+0.5%）'
        urgency = 'low'
    elif change < 1:
        change_signal = 'moderate_strong'
        change_desc = '美元走强（+0.5%~+1%）'
        urgency = 'medium'
    elif change < 2:
        change_signal = 'strong_strong'
        change_desc = '美元大涨（+1%~+2%）'
        urgency = 'high'
    else:
        change_signal = 'extreme_strong'
        change_desc = '美元暴涨（>+2%）'
        urgency = 'immediate'
    
    # 综合信号
    if kc50_bias == 'strong_bullish' and change_signal in ['extreme_weak', 'strong_weak']:
        overall_signal = 'strong_buy'
        impact_level = 'very_positive'
    elif kc50_bias in ['strong_bullish', 'neutral'] and change_signal in ['moderate_weak', 'strong_weak']:
        overall_signal = 'buy'
        impact_level = 'positive'
    elif kc50_bias == 'strong_bearish' and change_signal in ['extreme_strong', 'strong_strong']:
        overall_signal = 'strong_sell'
        impact_level = 'very_negative'
    elif kc50_bias in ['bearish', 'strong_bearish'] and change_signal in ['moderate_strong', 'strong_strong']:
        overall_signal = 'sell'
        impact_level = 'negative'
    else:
        overall_signal = 'neutral'
        impact_level = 'neutral'
    
    # 生成建议
    recommendation = {
        '科创50ETF': {
            'action': overall_signal,
            'confidence': 'high' if urgency == 'immediate' else 'medium',
            'rationale': f'DXY处于{level_desc}，日内{change_desc}'
        },
        '纳指ETF': {
            'action': overall_signal,
            'confidence': 'high' if urgency == 'immediate' else 'medium',
            'rationale': '与科创50同逻辑'
        },
        '黄金': {
            'action': 'buy' if change_signal in ['extreme_weak', 'strong_weak', 'moderate_weak'] else 
                     'sell' if change_signal in ['extreme_strong', 'strong_strong', 'moderate_strong'] else 'neutral',
            'confidence': 'high',
            'rationale': f'美元{change_desc}，黄金负相关'
        }
    }
    
    return {
        'dxy_price': price,
        'dxy_change': change,
        'level': level,
        'level_desc': level_desc,
        'change_signal': change_signal,
        'change_desc': change_desc,
        'impact_level': impact_level,
        'signal': overall_signal,
        'urgency': urgency,
        'description': f'DXY {price:.2f} ({change:+.2f}%) - {level_desc}，{change_desc}',
        'recommendation': recommendation,
        'correlation_note': 'DXY与科创50负相关约-0.8，美元弱则科技股强'
    }

def get_dxy_analysis_for_daily_update():
    """
    为每日更新提供DXY分析结果
    """
    dxy_data = get_dxy_data()
    analysis = analyze_dxy_impact(dxy_data)
    
    return {
        'dxy_data': dxy_data,
        'analysis': analysis,
        'has_data': dxy_data is not None,
        'summary': analysis.get('description', 'DXY数据 unavailable'),
        'key_signal': analysis.get('signal', 'neutral'),
        'kc50_recommendation': analysis.get('recommendation', {}).get('科创50ETF', {})
    }

if __name__ == '__main__':
    # 测试
    result = get_dxy_analysis_for_daily_update()
    print(json.dumps(result, ensure_ascii=False, indent=2))

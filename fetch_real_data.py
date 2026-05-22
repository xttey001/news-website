#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取2026年5月21-22日真实市场数据
使用新浪API
"""
import requests
import json
import time
from datetime import datetime

def get_stock_data(symbol, name):
    """从新浪API获取股票数据"""
    url = f'https://hq.sinajs.cn/list={symbol}'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.text
            if '="' in data:
                content = data.split('="')[1].split('";')[0]
                fields = content.split(',')
                if len(fields) > 30:
                    return {
                        'name': name,
                        'symbol': symbol,
                        'current': float(fields[3]),
                        'prev_close': float(fields[2]),
                        'open': float(fields[1]),
                        'high': float(fields[4]),
                        'low': float(fields[5]),
                        'change': float(fields[3]) - float(fields[2]),
                        'change_percent': (float(fields[3]) - float(fields[2])) / float(fields[2]) * 100,
                        'volume': int(fields[8]),
                        'amount': float(fields[9])
                    }
    except Exception as e:
        print(f'获取{name}失败: {e}')
    return None

def main():
    print("=== 获取2026年5月真实市场数据 ===")
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 主要指数
    indices = {
        'sh000001': '上证指数',
        'sz399006': '创业板指',
        'sz399001': '深证成指',
        'sh000688': '科创50',
        'sh000016': '上证50',
        'sh000300': '沪深300'
    }
    
    # 主要ETF
    etfs = {
        'sh512760': '芯片ETF',
        'sh518880': '黄金ETF',
        'sh588000': '科创50ETF',
        'sz159915': '创业板ETF',
        'sh512010': '医药ETF',
        'sh512800': '银行ETF'
    }
    
    print("【主要指数】")
    index_data = {}
    for symbol, name in indices.items():
        data = get_stock_data(symbol, name)
        if data:
            index_data[name] = data
            print(f"{name}: {data['current']:.2f} ({data['change_percent']:+.2f}%)")
        time.sleep(0.3)
    
    print("\n【主要ETF】")
    etf_data = {}
    for symbol, name in etfs.items():
        data = get_stock_data(symbol, name)
        if data:
            etf_data[name] = data
            print(f"{name}: {data['current']:.3f} ({data['change_percent']:+.2f}%)")
        time.sleep(0.3)
    
    # 保存数据
    result = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'indices': index_data,
        'etfs': etf_data
    }
    
    with open('real_market_data_2026.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n数据已保存到 real_market_data_2026.json")

if __name__ == "__main__":
    main()

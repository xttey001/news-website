#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析美元指数(DXY)与科创50ETF的相关性
"""
import requests
import json
from datetime import datetime, timedelta

def get_dxy_data():
    """
    获取美元指数数据
    使用新浪财经API或东方财富API
    """
    # 新浪财经美元指数
    url = "https://hq.sinajs.cn/list=fx_susdcny"
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'gbk'
        # 解析数据
        data = response.text
        return data
    except Exception as e:
        print(f"获取美元指数失败: {e}")
        return None

def get_stock_kline(code, market='sh'):
    """
    获取股票K线数据
    """
    # 腾讯财经K线API
    url = f"http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={market}{code},day,,,100,qfq"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return data
    except Exception as e:
        print(f"获取{code}K线失败: {e}")
        return None

def analyze_correlation():
    """
    分析美元指数与科创50的相关性
    """
    print("=" * 60)
    print("美元指数(DXY)与科创50ETF相关性分析")
    print("=" * 60)
    print()
    
    # 获取科创50ETF数据
    kc50_data = get_stock_kline('588000', 'sh')
    
    if kc50_data:
        print("✓ 成功获取科创50ETF数据")
        # 解析数据
        try:
            kline = kc50_data.get('data', {}).get('sh588000', {}).get('day', [])
            if kline:
                print(f"  获取到 {len(kline)} 个交易日数据")
                print(f"  最新数据: {kline[-1]}")
        except:
            print("  数据解析失败")
    else:
        print("✗ 获取科创50ETF数据失败")
    
    print()
    print("分析框架:")
    print("1. 美元指数下跌 → 美元走弱 → 资金流出美国 → 新兴市场受益")
    print("2. 科创50以科技股为主，对流动性敏感")
    print("3. 美元走弱时，外资更倾向于配置中国科技股")
    print()
    
    print("关键观察点:")
    print("- DXY跌破100: 美元进入弱势周期，利好科创50")
    print("- DXY突破105: 美元强势，科创50承压")
    print("- DXY与科创50通常呈负相关")

if __name__ == "__main__":
    analyze_correlation()

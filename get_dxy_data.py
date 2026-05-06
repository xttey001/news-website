#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取美元指数数据
"""
import requests
import json

def get_dxy_from_sina():
    """从新浪财经获取美元指数"""
    try:
        url = "https://hq.sinajs.cn/list=fx_susdxy"
        headers = {
            'Referer': 'https://finance.sina.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'gbk'
        
        text = response.text
        if 'hq_str_fx_susdxy' in text:
            start = text.find('"') + 1
            end = text.rfind('"')
            data_str = text[start:end]
            parts = data_str.split(',')
            
            if len(parts) >= 9:
                return {
                    'price': float(parts[0]),
                    'change_pct': float(parts[6]),
                    'source': 'sina'
                }
    except Exception as e:
        print(f"新浪财经获取失败: {e}")
    return None

def get_dxy_from_eastmoney():
    """从东方财富获取美元指数"""
    try:
        url = "https://push2.eastmoney.com/api/qt/stock/get"
        params = {
            'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
            'fltt': 2,
            'invt': 2,
            'fields': 'f43,f44,f45,f46,f47,f48,f57,f58,f60,f107,f170',
            'secid': '100.DX0',
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if data.get('data'):
            d = data['data']
            return {
                'price': float(d.get('f43', 0)) / 100,
                'change_pct': float(d.get('f170', 0)) / 100,
                'source': 'eastmoney'
            }
    except Exception as e:
        print(f"东方财富获取失败: {e}")
    return None

def get_dxy_data():
    """获取美元指数，优先新浪财经"""
    result = get_dxy_from_sina()
    if result:
        return result
    return get_dxy_from_eastmoney()

if __name__ == "__main__":
    dxy = get_dxy_data()
    if dxy:
        print(f"美元指数: {dxy['price']:.2f} ({dxy['change_pct']:+.2f}%)")
        print(f"来源: {dxy['source']}")
        
        # 判断信号
        if dxy['change_pct'] <= -1:
            signal = "强烈利好科创50"
        elif dxy['change_pct'] <= -0.5:
            signal = "利好科创50"
        elif dxy['change_pct'] >= 1:
            signal = "强烈利空科创50"
        elif dxy['change_pct'] >= 0.5:
            signal = "利空科创50"
        else:
            signal = "中性"
        
        print(f"信号: {signal}")
    else:
        print("获取DXY数据失败")

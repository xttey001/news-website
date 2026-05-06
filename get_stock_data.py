#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取腾讯股票API数据
"""
import requests
import json

def get_stock_data(symbols):
    """
    从腾讯API获取股票数据
    symbols: 股票代码列表，如 ['sh688256', 'sh688521', 'sz300502']
    """
    url = f"http://qt.gtimg.cn/q={','.join(symbols)}"
    
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'gbk'
        
        data = {}
        lines = response.text.strip().split(';')
        
        for line in lines:
            if not line.strip():
                continue
            
            # 解析数据
            if 'v_' in line:
                parts = line.split('~')
                if len(parts) >= 45:
                    # 腾讯API字段说明:
                    # 1: 股票名称
                    # 2: 股票代码
                    # 3: 当前价格
                    # 4: 昨收
                    # 5: 今开
                    # ...
                    # 32: 涨跌幅%
                    # 33: 涨跌额
                    
                    code = parts[2]
                    name = parts[1]
                    price = parts[3]
                    prev_close = parts[4]
                    change_pct = parts[32] if len(parts) > 32 else "0"
                    change_amount = parts[33] if len(parts) > 33 else "0"
                    
                    data[code] = {
                        'name': name,
                        'price': price,
                        'prev_close': prev_close,
                        'change_pct': change_pct,
                        'change_amount': change_amount
                    }
        
        return data
    except Exception as e:
        print(f"获取数据失败: {e}")
        return {}

if __name__ == "__main__":
    # 获取5月6日关键股票数据
    stocks = [
        'sh688256',   # 寒武纪
        'sh688521',   # 芯原股份
        'sz300308',   # 中际旭创
        'sz000858',   # 五粮液
        'sh588000',   # 科创50ETF
        'sh512760',   # 芯片ETF
        'sh600673',   # 东阳光
    ]
    
    result = get_stock_data(stocks)
    
    print("=" * 60)
    print("5月6日收盘数据")
    print("=" * 60)
    
    for code, info in result.items():
        print(f"{info['name']} ({code}):")
        print(f"  现价: {info['price']}")
        print(f"  涨跌: {info['change_amount']} ({info['change_pct']}%)")
        print()
    
    # 保存为JSON
    with open('stock_data_20260506.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("数据已保存到 stock_data_20260506.json")

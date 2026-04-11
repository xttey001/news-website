# -*- coding: utf-8 -*-
"""行情数据获取模块 - 多源备用方案
支持: 腾讯API(主) + 东方财富(备) + 新浪(备用)
"""

import requests
import os
import json
import time

# 清除代理干扰
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
    os.environ.pop(k, None)


def _get_session():
    """创建无代理的请求会话"""
    s = requests.Session()
    s.trust_env = False
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://finance.qq.com'
    })
    return s


def get_kline(code, days=7):
    """
    获取K线数据
    方案1: 腾讯API (主)
    方案2: 新浪API (备)
    """
    # 方案1: 腾讯
    s = _get_session()
    market = 'sh' if code.startswith(('5', '6')) else 'sz'
    url = f'https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={market}{code},day,,,{days + 30},qfq'
    
    try:
        r = s.get(url, timeout=8)
        data = r.json()
        key = f'{market}{code}'
        klines = (data.get('data', {}).get(key, {}).get('day', []) or 
                  data.get('data', {}).get(key, {}).get('qfqday', []))
        
        if klines:
            result = []
            for k in klines[-days:]:
                if len(k) >= 6:
                    open_p, close_p = float(k[1]), float(k[2])
                    change_pct = round((close_p - open_p) / open_p * 100, 2) if open_p > 0 else 0
                    result.append({
                        'date': k[0], 'open': open_p, 'close': close_p,
                        'high': float(k[3]), 'low': float(k[4]),
                        'volume': float(k[5]), 'change_pct': change_pct
                    })
            return {'klines': result, 'source': 'tencent'}
    except Exception as e:
        pass
    
    # 方案2: 新浪
    try:
        url2 = f'https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={market}{code}&scale=240&ma=no&datalen={days}'
        r2 = s.get(url2, timeout=8)
        if r2.status_code == 200:
            data2 = r2.json()
            if data2:
                result = [{
                    'date': k['day'],
                    'open': float(k['open']),
                    'close': float(k['close']),
                    'high': float(k['high']),
                    'low': float(k['low']),
                    'volume': float(k['volume']),
                    'change_pct': round((float(k['close']) - float(k['open'])) / float(k['open']) * 100, 2)
                } for k in data2[-days:]]
                return {'klines': result, 'source': 'sina'}
    except Exception as e:
        pass
    
    return {'klines': [], 'source': 'none'}


def get_realtime(code):
    """
    获取实时行情 + 主力资金
    方案1: 东方财富 (主)
    方案2: 腾讯 (备)
    """
    s = _get_session()
    market = '1' if code.startswith(('5', '6')) else '0'
    
    # 方案1: 东方财富
    url = f'https://push2.eastmoney.com/api/qt/stock/get?secid={market}.{code}&fields=f43,f57,f58,f169,f170,f171,f177'
    try:
        r = s.get(url, timeout=6)
        data = r.json().get('data', {})
        if data:
            price = data.get('f43', 0)
            if price > 10000: price = price / 100
            change_pct = data.get('f170', 0)
            if abs(change_pct) > 100: change_pct = change_pct / 100
            return {
                'code': code, 'price': price, 'change_pct': change_pct,
                'name': data.get('f58', ''), 'source': 'eastmoney'
            }
    except:
        pass
    
    # 方案2: 腾讯
    try:
        url2 = f'https://qt.gtimg.cn/q={market}{code}'
        r2 = s.get(url2, timeout=6)
        if r2.status_code == 200:
            parts = r2.text.strip().split('~')
            if len(parts) > 32:
                return {
                    'code': code,
                    'price': float(parts[3]) if parts[3] else 0,
                    'change_pct': float(parts[32]) if parts[32] else 0,
                    'name': parts[1] if len(parts) > 1 else '',
                    'source': 'tencent'
                }
    except:
        pass
    
    return {'code': code, 'price': 0, 'change_pct': 0, 'name': '', 'source': 'none'}


def get_market_data(codes, days=7):
    """批量获取市场数据"""
    result = {}
    for code in codes:
        kline_data = get_kline(code, days)
        realtime = get_realtime(code)
        result[code] = {
            'klines': kline_data.get('klines', []),
            'realtime': realtime,
            'source': kline_data.get('source', 'unknown')
        }
        time.sleep(0.2)
    return result


# ETF代码映射表
ETF_MAP = {
    '512760': '芯片ETF', '512930': 'AI人工智能ETF', '518880': '黄金ETF',
    '588890': '科创芯片ETF', '159382': '创业板AI ETF', '515980': '云计算ETF',
    '512010': '医药ETF', '512880': '国债ETF', '501018': '南方原油',
    '513500': '标普500ETF', '513050': '中概互联网ETF', '515700': '新能源ETF',
    '510300': '沪深300ETF', '515070': '人工智能AIETF', '588790': '科创AIETF',
}


if __name__ == '__main__':
    data = get_market_data(['512760', '518880'], 7)
    for code, info in data.items():
        name = ETF_MAP.get(code, code)
        print(f"{name}: source={info['source']}")
        if info['klines']:
            k = info['klines'][-1]
            print(f"  {k['date']} close={k['close']} change={k['change_pct']}%")
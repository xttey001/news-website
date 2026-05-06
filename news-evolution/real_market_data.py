# -*- coding: utf-8 -*-
"""
真实财经数据获取模块
集成真实市场数据 + 五维智能体分析框架
"""

import requests
import json
import time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

class RealMarketDataFetcher:
    """真实财经数据获取器"""
    
    def __init__(self):
        self.base_urls = {
            'sina': 'https://hq.sinajs.cn/list=',
            'eastmoney': 'https://push2.eastmoney.com/api/qt/ulist.np/get',
            'tencent': 'http://qt.gtimg.cn/q='
        }
        
    def get_stock_real_time(self, symbol):
        """获取股票实时数据"""
        try:
            # 新浪财经API
            if symbol.startswith('sh') or symbol.startswith('sz'):
                url = f"{self.base_urls['sina']}{symbol}"
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.text
                    # 解析新浪财经数据格式
                    if '="' in data:
                        content = data.split('="')[1].split('";')[0]
                        fields = content.split(',')
                        if len(fields) > 30:
                            return {
                                'symbol': symbol,
                                'name': fields[0],
                                'open': float(fields[1]),
                                'close': float(fields[2]),
                                'current': float(fields[3]),
                                'high': float(fields[4]),
                                'low': float(fields[5]),
                                'volume': int(fields[8]),
                                'amount': float(fields[9]),
                                'change': float(fields[3]) - float(fields[2]),
                                'change_percent': (float(fields[3]) - float(fields[2])) / float(fields[2]) * 100
                            }
            
            # 腾讯财经API作为备选
            url = f"{self.base_urls['tencent']}{symbol}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.text
                if '~' in data:
                    fields = data.split('~')
                    return {
                        'symbol': symbol,
                        'name': fields[1],
                        'current': float(fields[3]),
                        'change': float(fields[31]),
                        'change_percent': float(fields[32]),
                        'volume': int(fields[36]),
                        'amount': float(fields[37])
                    }
                    
        except Exception as e:
            print(f"获取股票数据失败 {symbol}: {e}")
        
        return None
    
    def get_index_data(self):
        """获取主要指数数据"""
        indices = {
            'sh000001': '上证指数',
            'sz399006': '创业板指',
            'sz399001': '深证成指',
            'sh000016': '上证50',
            'sz399005': '中小板指',
            'sh000688': '科创50'
        }
        
        result = {}
        for symbol, name in indices.items():
            data = self.get_stock_real_time(symbol)
            if data:
                result[name] = data
            time.sleep(0.5)  # 避免请求过于频繁
        
        return result
    
    def get_etf_data(self):
        """获取主要ETF数据"""
        etfs = {
            'sh512760': '芯片ETF',
            'sh512930': '纳指ETF',
            'sh518880': '黄金ETF',
            'sh588000': '科创50ETF',
            'sz159915': '创业板ETF',
            'sh512010': '医药ETF',
            'sh512170': '医疗ETF',
            'sh512880': '证券ETF'
        }
        
        result = {}
        for symbol, name in etfs.items():
            data = self.get_stock_real_time(symbol)
            if data:
                result[name] = data
            time.sleep(0.5)
        
        return result
    
    def get_news_summary(self):
        """获取财经新闻摘要（基于真实市场表现）"""
        indices = self.get_index_data()
        etfs = self.get_etf_data()
        
        # 分析市场表现
        market_analysis = self.analyze_market_trend(indices, etfs)
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'indices': indices,
            'etfs': etfs,
            'analysis': market_analysis
        }
    
    def analyze_market_trend(self, indices, etfs):
        """分析市场趋势"""
        analysis = {
            'overall_trend': '中性',
            'strong_industries': [],
            'weak_industries': [],
            'key_events': [],
            'volume_analysis': '正常',
            'sentiment': '中性'
        }
        
        # 分析指数表现
        if '上证指数' in indices:
            sh_change = indices['上证指数']['change_percent']
            if sh_change > 1:
                analysis['overall_trend'] = '强势'
            elif sh_change < -1:
                analysis['overall_trend'] = '弱势'
            else:
                analysis['overall_trend'] = '震荡'
        
        # 分析行业表现
        for etf_name, data in etfs.items():
            change = data['change_percent']
            if change > 2:
                analysis['strong_industries'].append(f"{etf_name}(+{change:.1f}%)")
            elif change < -2:
                analysis['weak_industries'].append(f"{etf_name}({change:.1f}%)")
        
        # 分析成交量
        total_volume = sum(data.get('volume', 0) for data in indices.values() if data)
        if total_volume > 1000000000:  # 10亿
            analysis['volume_analysis'] = '放量'
        elif total_volume < 500000000:  # 5亿
            analysis['volume_analysis'] = '缩量'
        
        return analysis

# 测试函数
def test_real_data():
    """测试真实数据获取"""
    fetcher = RealMarketDataFetcher()
    
    print("=== 测试真实财经数据获取 ===")
    
    # 获取指数数据
    indices = fetcher.get_index_data()
    print("\n主要指数表现：")
    for name, data in indices.items():
        if data:
            print(f"{name}: {data['current']:.2f} ({data['change_percent']:+.2f}%)")
    
    # 获取ETF数据
    etfs = fetcher.get_etf_data()
    print("\n主要ETF表现：")
    for name, data in etfs.items():
        if data:
            print(f"{name}: {data['current']:.3f} ({data['change_percent']:+.2f}%)")
    
    # 获取新闻摘要
    summary = fetcher.get_news_summary()
    print(f"\n市场分析: {summary['analysis']}")

if __name__ == "__main__":
    test_real_data()
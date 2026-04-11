# -*- coding: utf-8 -*-
import requests
import json
import sys

# 设置stdout编码
sys.stdout.reconfigure(encoding='utf-8')

def search_news(keyword):
    """搜索新闻"""
    url = 'http://localhost:19000/proxy/prosearch/search'
    payload = {
        'keyword': keyword,
        'industry': 'news'
    }
    
    try:
        r = requests.post(url, json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {'success': False, 'error': str(e)}

if __name__ == '__main__':
    keywords = [
        'A股最新行情 上证指数 深证成指 2026年3月',
        '新能源股票 锂电池 光伏 储能 最新消息',
        '科技股 芯片 人工智能 机器人 2026年',
        '金融板块 银行 保险 券商 最新新闻',
        '腾讯 阿里巴巴 美团 字节跳动 最新动态'
    ]
    
    all_results = []
    
    for kw in keywords:
        print(f"\n{'='*60}")
        print(f"搜索: {kw}")
        print('='*60)
        
        result = search_news(kw)
        
        if result.get('success'):
            data = result.get('data', {})
            docs = data.get('docs', [])
            print(f"找到 {len(docs)} 条结果")
            
            for i, doc in enumerate(docs[:5], 1):
                title = doc.get('title', '')
                url = doc.get('url', '')
                passage = doc.get('passage', '')
                date = doc.get('date', '')
                site = doc.get('site', '')
                
                print(f"\n{i}. {title}")
                print(f"   来源: {site} ({date})")
                print(f"   链接: {url}")
                print(f"   摘要: {passage[:200]}...")
                
                all_results.append({
                    'title': title,
                    'url': url,
                    'passage': passage,
                    'date': date,
                    'site': site
                })
        else:
            print(f"搜索失败: {result.get('error', result.get('message', '未知错误'))}")
    
    # 保存结果
    with open('latest_news_raw.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\n\n总共收集 {len(all_results)} 条新闻，已保存到 latest_news_raw.json")

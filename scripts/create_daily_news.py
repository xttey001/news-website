#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日新闻生成脚本
生成独立的日期 JSON 文件并更新索引

使用方法:
    python scripts/create_daily_news.py 2026-05-21
    
    或不带参数（默认今天）:
    python scripts/create_daily_news.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def load_template():
    """加载新闻数据模板"""
    return {
        "date": "",
        "market_tone": {
            "早报": "",
            "晚报": ""
        },
        "all_news": [],
        "s_level": [],
        "a_level": [],
        "wukong_judgment": {
            "emotion": "",
            "analysis": [],
            "strategy": []
        },
        "sangsha_module": {
            "overall_sentiment": "",
            "analysis_results": [],
            "韭菜行为总结": "",
            "市场含义": ""
        },
        "white_dragon": {
            "主力状态": "",
            "阶段": "",
            "etf_signals": [],
            "综合建议": ""
        },
        "bajie_conclusion": {
            "optimal_action": "",
            "optimal_etfs": "",
            "win_rate": "",
            "decision_matrix": [],
            "沙僧信号": {},
            "白龙马信号": {},
            "悟空信号": {}
        },
        "tang_sanzang": {
            "仓位建议": "",
            "最终行动": "",
            "跨层矛盾仲裁": [],
            "仓位公式": "",
            "风控触发": [],
            "唐僧结论": ""
        },
        "market_data": {
            "shanghai": {"index": 0, "change": ""},
            "chi_next": {"index": 0, "change": ""},
            "hk": {"index": 0, "change": ""},
            "turnover": "",
            "advancing_stocks": 0
        },
        "hot_topics": [],
        "douyin": []
    }


def update_index(index_path, new_date):
    """更新索引文件，添加新日期到最前面"""
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            index = json.load(f)
    else:
        index = {
            "availableDates": [],
            "version": "1.0"
        }
    
    # 如果日期已存在，先移除
    if new_date in index["availableDates"]:
        index["availableDates"].remove(new_date)
    
    # 添加到最前面
    index["availableDates"].insert(0, new_date)
    index["lastUpdated"] = datetime.now().isoformat()
    index["totalCount"] = len(index["availableDates"])
    
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    return index


def create_daily_news(date_str=None):
    """创建每日新闻文件"""
    # 确定日期
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    # 路径配置
    workspace_dir = Path(__file__).parent.parent
    news_data_dir = workspace_dir / 'news-data'
    index_file = workspace_dir / 'news-data-index.json'
    
    # 确保目录存在
    news_data_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建模板数据
    template = load_template()
    template['date'] = date_str
    
    # 保存文件
    file_path = news_data_dir / f"{date_str}.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 创建新闻文件: {file_path}")
    
    # 更新索引
    index = update_index(index_file, date_str)
    print(f"✓ 更新索引: {index_file}")
    
    print(f"\n📊 当前共有 {index['totalCount']} 个日期")
    print(f"   最新日期: {index['availableDates'][0]}")
    
    return file_path


def main():
    """主函数"""
    print("=" * 50)
    print("每日新闻生成工具")
    print("=" * 50)
    
    # 获取日期参数
    date_str = sys.argv[1] if len(sys.argv) > 1 else None
    
    if date_str:
        print(f"\n📅 指定日期: {date_str}\n")
    else:
        print(f"\n📅 使用今天日期\n")
    
    # 创建文件
    file_path = create_daily_news(date_str)
    
    print("\n" + "=" * 50)
    print("✅ 完成!")
    print(f"   文件路径: {file_path}")
    print("\n💡 提示: 编辑此文件添加新闻内容")
    print("=" * 50)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
使用完整五维智能体分析系统更新数据
"""

import sys
import os
import json
from datetime import datetime

# 添加路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from real_market_data import RealMarketDataFetcher
from full_five_layer_analysis import FiveLayerAnalyzer

def update_with_full_analysis():
    """使用完整五维分析更新数据"""
    
    print("🐵 悟空财经 - 完整五维智能体分析更新")
    print("=" * 60)
    
    # Step 1: 获取真实市场数据
    print("\nStep 1: 获取真实市场数据...")
    fetcher = RealMarketDataFetcher()
    real_data = fetcher.get_news_summary()
    
    if not real_data or 'indices' not in real_data:
        print("❌ 获取真实数据失败")
        return False
    
    print(f"✅ 真实数据获取成功")
    print(f"   上证指数: {real_data['indices']['上证指数']['current']:.2f} ({real_data['indices']['上证指数']['change_percent']:+.2f}%)")
    print(f"   科创50: {real_data['indices']['科创50']['current']:.2f} ({real_data['indices']['科创50']['change_percent']:+.2f}%)")
    print(f"   芯片ETF: {real_data['etfs']['芯片ETF']['current']:.3f} ({real_data['etfs']['芯片ETF']['change_percent']:+.2f}%)")
    
    # Step 2: 五维智能体分析
    print("\nStep 2: 运行五维智能体分析...")
    analyzer = FiveLayerAnalyzer(real_data)
    five_layer_data = analyzer.generate_full_analysis()
    
    print(f"✅ 五维分析完成")
    print(f"   悟空判断: {five_layer_data['wukong_judgment']['emotion']}")
    print(f"   沙僧情绪: {five_layer_data['sangsha_module']['overall_sentiment']}")
    print(f"   白龙马状态: {five_layer_data['white_dragon']['主力状态']}")
    print(f"   八戒胜率: {five_layer_data['bajie_conclusion']['win_rate']}")
    print(f"   唐僧仓位: {five_layer_data['tang_sanzang']['仓位建议']}")
    
    # Step 3: 更新news-data.js
    print("\nStep 3: 更新news-data.js...")
    news_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'news-data.js')
    
    try:
        # 读取现有文件
        with open(news_data_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 找到2026-04-30的数据位置
        date_str = '"2026-04-30"'
        if date_str in content:
            # 找到该日期的开始位置
            start_idx = content.find(date_str)
            # 找到该日期的结束位置（下一个日期或文件结尾）
            end_idx = content.find('",\n  "2026-04-29"', start_idx)
            if end_idx == -1:
                end_idx = content.find('\n};', start_idx)
            
            # 构建新的数据内容
            new_data_str = json.dumps(five_layer_data, ensure_ascii=False, indent=2)
            # 替换旧数据
            new_content = content[:start_idx] + '"2026-04-30": ' + new_data_str + content[end_idx:]
            
            # 更新文件头
            new_content = new_content.replace(
                '// 财经新闻数据 - 混合模式（真实数据+智能体分析）',
                '// 财经新闻数据 - 完整五维智能体分析版'
            )
            new_content = new_content.replace(
                '// 生成时间: 2026-04-30 16:46:27',
                f'// 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            )
            new_content = new_content.replace(
                '// 数据源: 实时财经数据 + 五维智能体分析',
                '// 数据源: 实时财经数据 + 完整五维智能体深度分析（悟空/沙僧/白龙马/八戒/唐僧）'
            )
            
            # 写回文件
            with open(news_data_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ news-data.js 更新成功")
        else:
            print("❌ 未找到2026-04-30数据")
            return False
        
    except Exception as e:
        print(f"❌ 更新失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Step 4: 生成本地HTML
    print("\nStep 4: 生成本地HTML版本...")
    try:
        create_local_html(news_data_path)
        print("✅ local_news.html 生成成功")
    except Exception as e:
        print(f"⚠️ 生成本地HTML失败: {e}")
    
    # Step 5: 验证语法
    print("\nStep 5: 验证JavaScript语法...")
    import subprocess
    result = subprocess.run(['node', '-c', news_data_path], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ JavaScript语法验证通过")
    else:
        print(f"❌ JavaScript语法错误: {result.stderr}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 完整五维智能体分析更新完成！")
    print("\n📊 分析特点:")
    print("  • 真实财经数据驱动")
    print("  • 完整五维智能体分析框架")
    print("  • 悟空：市场深度判断")
    print("  • 沙僧：散户情绪监测")
    print("  • 白龙马：主力行为识别")
    print("  • 八戒：贝叶斯概率校准")
    print("  • 唐僧：跨层矛盾仲裁")
    print("\n📁 更新文件:")
    print("  • news-data.js (主数据文件)")
    print("  • local_news.html (本地离线版)")
    
    return True

def create_local_html(news_data_path):
    """生成本地HTML版本"""
    # 读取news-data.js内容
    with open(news_data_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # 读取index.html模板
    index_path = os.path.join(os.path.dirname(news_data_path), 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 替换脚本引用为内嵌脚本
    old_script = '<script src="news-data.js"></script>'
    new_script = f'<script>\n{js_content}\n</script>'
    html_content = html_content.replace(old_script, new_script)
    
    # 更新标题和说明
    html_content = html_content.replace(
        '数据来源：天集 ProSearch · 权威财经媒体',
        '数据来源：实时财经数据 + 完整五维智能体深度分析'
    )
    
    # 保存为local_news.html
    local_html_path = os.path.join(os.path.dirname(news_data_path), 'local_news.html')
    with open(local_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    success = update_with_full_analysis()
    sys.exit(0 if success else 1)
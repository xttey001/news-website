# -*- coding: utf-8 -*-
"""
混合模式每日更新脚本
真实财经数据 + 五维智能体分析框架
"""

import sys
import os
import json
from datetime import datetime
from hybrid_data_generator import HybridDataGenerator

def update_news_data_with_real_data():
    """使用真实数据更新新闻数据"""
    
    # 初始化混合数据生成器
    generator = HybridDataGenerator()
    
    # 生成今日混合数据
    print("=== 混合模式数据生成 ===")
    print("正在获取真实财经数据...")
    
    try:
        hybrid_data = generator.generate_daily_data()
        print("✅ 真实数据获取成功")
        
        # 读取现有news-data.js
        news_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'news-data.js')
        
        with open(news_data_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析现有数据
        if 'const newsData = {' in content:
            # 提取newsData对象内容
            start_idx = content.find('const newsData = {') + len('const newsData = {')
            end_idx = content.find('};', start_idx) + 1
            
            # 解析现有数据
            existing_data_str = '{' + content[start_idx:end_idx]
            existing_data = json.loads(existing_data_str)
            
            # 更新availableDates
            today = datetime.now().strftime('%Y-%m-%d')
            if 'availableDates' in existing_data:
                if today not in existing_data['availableDates']:
                    existing_data['availableDates'].insert(0, today)
            
            # 添加今日数据
            existing_data[today] = hybrid_data
            
            # 重新生成news-data.js内容
            new_content = "// 财经新闻数据 - 混合模式（真实数据+智能体分析）\n"
            new_content += "// 生成时间: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"
            new_content += "// 数据源: 实时财经数据 + 五维智能体分析\n\n"
            new_content += "const newsData = " + json.dumps(existing_data, ensure_ascii=False, indent=2) + ";\n\n"
            
            # 保留原有函数
            functions_start = content.find('const availableDates =')
            if functions_start != -1:
                new_content += content[functions_start:]
            
            # 写回文件
            with open(news_data_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ news-data.js 更新成功")
            
            # 生成本地HTML版本
            create_local_html(news_data_path)
            
            return True
            
    except Exception as e:
        print(f"❌ 混合模式更新失败: {e}")
        return False

def create_local_html(news_data_path):
    """生成本地HTML版本"""
    try:
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
            '数据来源：实时财经数据 + 五维智能体分析（混合模式）'
        )
        
        # 保存为local_news.html
        local_html_path = os.path.join(os.path.dirname(news_data_path), 'local_news.html')
        with open(local_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✅ local_news.html 生成成功")
        
    except Exception as e:
        print(f"❌ 生成本地HTML失败: {e}")

def main():
    """主函数"""
    print("🐵 悟空财经 - 混合模式数据更新")
    print("=" * 50)
    
    success = update_news_data_with_real_data()
    
    if success:
        print("\n🎉 混合模式更新完成！")
        print("📊 数据特点:")
        print("  • 真实财经数据驱动")
        print("  • 五维智能体分析框架")
        print("  • 实时市场表现整合")
        print("  • 风险控制机制完善")
        print("\n📁 更新文件:")
        print("  • news-data.js (主数据文件)")
        print("  • local_news.html (本地离线版)")
        print("\n🌐 访问地址:")
        print("  • 在线版: https://xttey001.github.io/news-website/")
        print("  • 本地版: 双击 local_news.html")
    else:
        print("\n❌ 更新失败，请检查网络连接或数据源")

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
创建本地版本脚本
将 index.html 和 news-data.js 合并为 local_news.html
"""

# 路径配置
INDEX_PATH = r'C:\Users\asus\.qclaw\workspace\index.html'
DATA_PATH = r'C:\Users\asus\.qclaw\workspace\news-data.js'
OUTPUT_PATH = r'C:\Users\asus\.qclaw\workspace\local_news.html'

def create_local_version():
    """创建本地版本"""
    print("="*60)
    print("🔄 创建本地版本")
    print("="*60)
    
    # 读取 index.html
    try:
        with open(INDEX_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"✅ 已读取: {INDEX_PATH}")
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return False
    
    # 读取 news-data.js
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            js_content = f.read()
        print(f"✅ 已读取: {DATA_PATH}")
        print(f"   数据大小: {len(js_content)} 字符")
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return False
    
    # 替换外部脚本引用为内嵌脚本
    # 查找 <script src="news-data.js"></script> 并替换为内嵌数据
    import re
    
    # 添加本地版标记到标题
    html_content = html_content.replace(
        '<title>悟空财经分析</title>',
        '<title>悟空财经分析 - 本地版</title>'
    )
    
    # 替换数据脚本引用
    old_script = '<script src="news-data.js"></script>'
    new_script = f'<script>\n{js_content}\n</script>'
    
    if old_script not in html_content:
        print("⚠️ 未找到数据脚本引用，尝试其他模式...")
        # 尝试其他可能的格式
        old_script = 'src="news-data.js"'
        if old_script not in html_content:
            print("❌ 无法找到数据脚本引用")
            return False
        else:
            # 替换整个script标签（可能有多行）
            pattern = r'<script[^>]*src=["\']news-data\.js["\'][^>]*>[^<]*</script>'
            html_content = re.sub(pattern, new_script, html_content)
    else:
        html_content = html_content.replace(old_script, new_script)
    
    # 添加本地版标记到页面
    local_badge = '''<div style="display:inline-block;margin-top:8px;padding:4px 10px;background:rgba(63,185,80,0.15);border:1px solid rgba(63,185,80,0.3);border-radius:6px;color:#3fb950;font-size:11px;">📱 本地版 - 无需网络</div>'''
    
    # 在header中添加本地版标记
    if '<div class="local-badge">' not in html_content:
        html_content = html_content.replace(
            '<div class="subtitle">不盲从主流解读，用逻辑和数据说话</div>',
            '<div class="subtitle">不盲从主流解读，用逻辑和数据说话</div>\n            ' + local_badge
        )
    
    # 写入输出文件
    try:
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ 已保存: {OUTPUT_PATH}")
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False
    
    print("="*60)
    print("🎉 本地版本创建成功!")
    print(f"📁 文件位置: {OUTPUT_PATH}")
    print("💡 提示: 双击文件即可在浏览器中打开，无需网络")
    print("="*60)
    return True

if __name__ == '__main__':
    create_local_version()

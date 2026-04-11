#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动财经新闻网站服务器
"""

import subprocess
import sys
import os

def main():
    # 检查 Flask 是否已安装
    try:
        import flask
    except ImportError:
        print("📦 正在安装依赖...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # 启动服务器
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║         财经新闻网站服务器已启动                            ║
    ╠════════════════════════════════════════════════════════════╣
    ║  🌐 本地访问: http://localhost:5000                        ║
    ║  📱 局域网访问: http://[你的IP]:5000                       ║
    ║  🔗 公网访问: 需要配置反向代理或内网穿透                   ║
    ║                                                            ║
    ║  功能:                                                     ║
    ║  ✅ 查看今天的新闻                                         ║
    ║  ✅ 切换日期查看历史新闻                                   ║
    ║  ✅ 自动保存每天的新闻数据                                 ║
    ║  ✅ 支持其他人访问                                         ║
    ║                                                            ║
    ║  按 Ctrl+C 停止服务器                                      ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()

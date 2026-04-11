#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动财经新闻网站服务器（后台运行版本）
"""

import subprocess
import sys
import os
import time
from pathlib import Path

# 设置输出编码
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

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
    
    # 启动服务器
    try:
        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
        sys.exit(0)

if __name__ == '__main__':
    main()

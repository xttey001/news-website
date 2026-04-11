#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 Ngrok 快速部署到公网
"""

import subprocess
import sys
import os
import io
import time
import webbrowser

# 修复编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def check_ngrok():
    """检查 ngrok 是否已安装"""
    try:
        result = subprocess.run(['ngrok', 'version'], 
                              capture_output=True, text=True, timeout=5)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False

def main():
    print("\n" + "="*60)
    print("财经新闻网站 - 公网部署工具")
    print("="*60)
    
    # 检查 ngrok
    if not check_ngrok():
        print("\n未检测到 ngrok，请按以下步骤安装：")
        print("\n1. 访问: https://ngrok.com/download")
        print("2. 下载 Windows 版本")
        print("3. 解压到任意目录（如 C:\\ngrok\\）")
        print("4. 将 ngrok.exe 所在目录添加到系统 PATH")
        print("\n或者使用 Cloudflare Tunnel（无需下载）：")
        print("   python share_cloudflare.py")
        input("\n按 Enter 键退出...")
        sys.exit(1)
    
    print("\n✅ ngrok 已安装")
    print("\n正在启动公网隧道...")
    print("\n步骤：")
    print("1. ngrok 会显示一个公网 URL（如 https://abc123.ngrok.io）")
    print("2. 复制这个 URL 分享给其他人")
    print("3. 其他人可以通过这个 URL 访问你的新闻网站")
    print("\n提示：")
    print("- 免费版本的 URL 每次启动都会变化")
    print("- 如需固定 URL，可升级到付费版本")
    print("- 或使用 Cloudflare Tunnel（免费固定 URL）")
    print("\n" + "="*60)
    
    # 启动 ngrok
    try:
        subprocess.run(['ngrok', 'http', '5000'], check=False)
    except KeyboardInterrupt:
        print("\n\n隧道已关闭")
        sys.exit(0)
    except Exception as e:
        print(f"\n错误: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

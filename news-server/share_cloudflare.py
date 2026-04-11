#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动配置公网访问 - 使用 Cloudflare Tunnel（无需下载额外工具）
"""

import subprocess
import sys
import os
import io

# 修复编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def check_cloudflared():
    """检查 cloudflared 是否已安装"""
    try:
        subprocess.run(['cloudflared', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_cloudflared():
    """安装 cloudflared"""
    print("\nInstalling cloudflared...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'cloudflare-cli'],
                      check=True)
        return True
    except subprocess.CalledProcessError:
        print("\nFailed to install cloudflared via pip")
        print("Please download from: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/")
        return False

def main():
    print("\n" + "="*60)
    print("Public Access Configuration - Cloudflare Tunnel")
    print("="*60)
    
    # 检查 cloudflared
    if not check_cloudflared():
        print("\ncloudflared not found")
        print("Attempting to install...")
        if not install_cloudflared():
            print("\nPlease install cloudflared manually:")
            print("https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/")
            input("\nPress Enter to exit...")
            sys.exit(1)
    
    print("\ncloudflared is installed")
    print("\nStarting tunnel to http://localhost:5000...")
    print("\nYou will get a public URL like: https://xxx.trycloudflare.com")
    print("Share this URL with others\n")
    
    try:
        subprocess.run(['cloudflared', 'tunnel', '--url', 'http://localhost:5000'],
                      check=False)
    except KeyboardInterrupt:
        print("\n\nTunnel stopped")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

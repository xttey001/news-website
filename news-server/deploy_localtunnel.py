"""
Localtunnel 自动部署脚本（完全免费，无需注册）
"""
import subprocess
import sys
import os
import time
import urllib.request
import json

def main():
    print("\n" + "="*60)
    print("Localtunnel Auto-Deploy (Free, No Registration)")
    print("="*60 + "\n")
    
    # 1. 检查服务器
    print("[1/4] Checking Flask server...")
    try:
        urllib.request.urlopen("http://127.0.0.1:5000", timeout=2)
        print("[OK] Server running on port 5000\n")
    except:
        print("[INFO] Starting server...")
        server_dir = os.path.dirname(os.path.abspath(__file__))
        server_script = os.path.join(server_dir, "start_simple.py")
        subprocess.Popen(
            [sys.executable, server_script],
            cwd=server_dir,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        time.sleep(3)
        print("[OK] Server started\n")
    
    # 2. 安装 localtunnel
    print("[2/4] Installing localtunnel...")
    
    # 检查 npm
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        print(f"[OK] npm version: {result.stdout.strip()}\n")
    except:
        print("[ERROR] npm not found. Please install Node.js first")
        print("Download: https://nodejs.org/")
        return
    
    # 安装 localtunnel
    print("[INFO] Installing localtunnel globally...")
    subprocess.run(["npm", "install", "-g", "localtunnel"], shell=True)
    print("[OK] localtunnel installed\n")
    
    # 3. 启动 tunnel
    print("[3/4] Starting tunnel...")
    print("[INFO] This creates a public URL for your website\n")
    
    # 启动 localtunnel
    proc = subprocess.Popen(
        ["npx", "lt", "--port", "5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    print("[OK] Tunnel started\n")
    
    # 4. 获取 URL
    print("[4/4] Waiting for public URL...\n")
    
    public_url = None
    start_time = time.time()
    
    while time.time() - start_time < 30:
        try:
            line = proc.stdout.readline()
            if not line:
                if proc.poll() is not None:
                    break
                time.sleep(0.5)
                continue
            
            print(line.strip())
            
            # 查找 URL
            if "https://" in line:
                import re
                urls = re.findall(r'https://[^\s]+', line)
                if urls:
                    public_url = urls[0]
                    break
        except:
            time.sleep(1)
    
    if public_url:
        print("\n" + "="*60)
        print("SUCCESS! Your Public URL:")
        print("="*60)
        print(f"\n  {public_url}\n")
        print("="*60)
        print("\nShare this URL with others!")
        print(f"\nLocal:  http://localhost:5000")
        print(f"Public: {public_url}")
        
        # 保存
        with open("PUBLIC_URL.txt", 'w', encoding='utf-8') as f:
            f.write(f"{public_url}\n")
        print("\nURL saved to PUBLIC_URL.txt")
        print("="*60 + "\n")
    else:
        print("[ERROR] Could not get public URL")

if __name__ == "__main__":
    main()

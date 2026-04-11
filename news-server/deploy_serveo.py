"""
Serveo.net 自动部署脚本（完全免费，无需安装，无需注册）
使用 SSH 隧道，Windows 自带 SSH 客户端
"""
import subprocess
import sys
import os
import time
import re

def main():
    print("\n" + "="*60)
    print("Serveo.net Auto-Deploy (Free, No Registration)")
    print("="*60 + "\n")
    
    print("[INFO] Serveo.net uses SSH tunnel - no installation needed!")
    print("[INFO] Works on Windows 10/11 with built-in SSH\n")
    
    # 1. 检查服务器
    print("[1/3] Checking Flask server...")
    try:
        import urllib.request
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
    
    # 2. 启动 SSH 隧道
    print("[2/3] Starting SSH tunnel to serveo.net...")
    print("[INFO] This creates a public URL for your website\n")
    
    # 使用 Windows 自带的 ssh
    proc = subprocess.Popen(
        ["ssh", "-R", "80:localhost:5000", "serveo.net"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace',
        stdin=subprocess.PIPE
    )
    
    print("[OK] Tunnel started\n")
    
    # 3. 获取 URL
    print("[3/3] Waiting for public URL...")
    print("[INFO] This usually takes 3-10 seconds...\n")
    
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
            
            # Serveo 显示格式: "Forwarding HTTP traffic from https://xxx.serveo.net"
            if "https://" in line and "serveo.net" in line:
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
        print("They can access your news website from anywhere!")
        print(f"\nLocal:  http://localhost:5000")
        print(f"Public: {public_url}")
        
        # 保存
        with open("PUBLIC_URL.txt", 'w', encoding='utf-8') as f:
            f.write(f"News Website Public URL:\n")
            f.write(f"{public_url}\n")
            f.write(f"\nGenerated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("\nURL saved to PUBLIC_URL.txt")
        print("\nPress Ctrl+C to stop the tunnel")
        print("="*60 + "\n")
        
        # 保持运行
        try:
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
    else:
        print("[ERROR] Could not get public URL")
        print("\nPossible issues:")
        print("1. SSH not available (Windows 10/11 required)")
        print("2. Firewall blocking SSH")
        print("3. Serveo.net temporarily unavailable")

if __name__ == "__main__":
    main()

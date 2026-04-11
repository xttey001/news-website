"""
Cloudflare Tunnel 自动部署脚本（无需注册）
"""
import subprocess
import sys
import os
import time
import urllib.request
import json

def main():
    print("\n" + "="*60)
    print("Cloudflare Tunnel Auto-Deploy")
    print("="*60 + "\n")
    
    print("[INFO] Cloudflare Tunnel is free and requires NO registration!\n")
    
    # 1. 检查服务器是否运行
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
    
    # 2. 检查 cloudflared
    print("[2/4] Checking cloudflared...")
    cloudflared_path = None
    
    # 检查常见位置
    possible_paths = [
        r"C:\Program Files (x86)\Cloudflare\Cloudflare WARP\cloudflared.exe",
        r"C:\Program Files\Cloudflare\Cloudflare WARP\cloudflared.exe",
        os.path.expanduser(r"~\.cloudflared\cloudflared.exe"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            cloudflared_path = path
            break
    
    if not cloudflared_path:
        print("[INFO] cloudflared not found, downloading...")
        
        # 下载 cloudflared
        download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
        cloudflared_path = os.path.join(os.path.dirname(__file__), "cloudflared.exe")
        
        try:
            print(f"[INFO] Downloading from: {download_url}")
            urllib.request.urlretrieve(download_url, cloudflared_path)
            print(f"[OK] Downloaded to: {cloudflared_path}\n")
        except Exception as e:
            print(f"[ERROR] Download failed: {e}")
            print("\n[FALLBACK] Trying alternative method...")
            
            # 使用 PowerShell 下载
            ps_cmd = f'''
            Invoke-WebRequest -Uri "{download_url}" -OutFile "{cloudflared_path}"
            '''
            subprocess.run(["powershell", "-Command", ps_cmd], shell=True)
            
            if os.path.exists(cloudflared_path):
                print(f"[OK] Downloaded to: {cloudflared_path}\n")
            else:
                print("[ERROR] Failed to download cloudflared")
                print("\nAlternative: Try Ngrok with registration")
                print("1. Sign up: https://dashboard.ngrok.com/signup")
                print("2. Get token: https://dashboard.ngrok.com/get-started/your-authtoken")
                print("3. Run: ngrok config add-authtoken YOUR_TOKEN")
                return
    else:
        print(f"[OK] Found cloudflared at: {cloudflared_path}\n")
    
    # 3. 启动 Cloudflare Tunnel
    print("[3/4] Starting Cloudflare Tunnel...")
    print("[INFO] This creates a public URL for your website\n")
    
    # 启动 cloudflared
    proc = subprocess.Popen(
        [cloudflared_path, "tunnel", "--url", "http://localhost:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    print("[OK] Tunnel started\n")
    
    # 4. 等待并获取 URL
    print("[4/4] Waiting for public URL...")
    print("[INFO] This may take 10-30 seconds...\n")
    
    public_url = None
    start_time = time.time()
    
    while time.time() - start_time < 60:
        try:
            line = proc.stdout.readline()
            if not line:
                if proc.poll() is not None:
                    break
                time.sleep(0.5)
                continue
            
            print(line.strip())
            
            # 查找 URL
            if "https://" in line and "trycloudflare.com" in line:
                import re
                urls = re.findall(r'https://[^\s]+\.trycloudflare\.com', line)
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
        print("="*60 + "\n")
        
        print("Press Ctrl+C to stop the tunnel")
        
        # 保持运行
        try:
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
    else:
        print("[ERROR] Could not get public URL")
        print("\nCheck the output above for errors")

if __name__ == "__main__":
    main()

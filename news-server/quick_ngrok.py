"""
快速启动 Ngrok 并显示 URL
"""
import subprocess
import urllib.request
import json
import time
import os

print("\n" + "="*60)
print("Quick Ngrok Deploy")
print("="*60 + "\n")

# 1. 启动 ngrok（后台）
ngrok_path = r"C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe"

print("[1] Starting ngrok...")
proc = subprocess.Popen(
    [ngrok_path, "http", "5000", "--log=stdout"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NO_WINDOW
)

print("[2] Waiting for tunnel...")
time.sleep(8)

# 2. 获取 URL
print("[3] Fetching public URL...\n")
try:
    response = urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels", timeout=5)
    data = json.loads(response.read().decode())
    
    if data.get('tunnels'):
        public_url = data['tunnels'][0]['public_url']
        print("="*60)
        print("SUCCESS! Your Public URL:")
        print("="*60)
        print(f"\n  {public_url}\n")
        print("="*60)
        print("\nShare this URL with others!")
        print(f"\nLocal:  http://localhost:5000")
        print(f"Public: {public_url}")
        
        # 保存
        with open("PUBLIC_URL.txt", 'w') as f:
            f.write(f"{public_url}\n")
        print("\nURL saved to PUBLIC_URL.txt")
        print("="*60 + "\n")
    else:
        print("[ERROR] No tunnels found")
        print("\nChecking ngrok output...")
        stdout, stderr = proc.communicate(timeout=2)
        if stdout:
            print(stdout.decode('utf-8', errors='ignore'))
        if stderr:
            print(stderr.decode('utf-8', errors='ignore'))
        
except Exception as e:
    print(f"[ERROR] {e}")
    print("\nPossible issues:")
    print("1. Ngrok may need authentication")
    print("2. Port 5000 may not be running")
    print("3. Ngrok process may have failed")
    
    # 检查进程
    if proc.poll() is not None:
        stdout, stderr = proc.communicate()
        print("\nNgrok output:")
        if stdout:
            print(stdout.decode('utf-8', errors='ignore'))
        if stderr:
            print(stderr.decode('utf-8', errors='ignore'))

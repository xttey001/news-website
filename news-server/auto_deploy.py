"""
自动部署 Ngrok 公网访问脚本（非交互版）
"""
import subprocess
import sys
import os
import time
import urllib.request
import json

def main():
    print("\n" + "="*60)
    print("Ngrok Auto-Deploy for News Website")
    print("="*60 + "\n")
    
    # ngrok 路径
    ngrok_path = r"C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe"
    
    if not os.path.exists(ngrok_path):
        print(f"[ERROR] ngrok.exe not found at: {ngrok_path}")
        return
    
    print(f"[1/4] Found ngrok: {ngrok_path}\n")
    
    # Step 2: Start Flask server
    print("[2/4] Starting Flask server...")
    server_dir = os.path.dirname(os.path.abspath(__file__))
    server_script = os.path.join(server_dir, "start_simple.py")
    
    # 检查是否已经有服务器在运行
    try:
        urllib.request.urlopen("http://127.0.0.1:5000", timeout=2)
        print("[OK] Server already running on port 5000\n")
    except:
        # 启动服务器
        server_process = subprocess.Popen(
            [sys.executable, server_script],
            cwd=server_dir,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print("[OK] Server starting in new window...")
        time.sleep(3)
        print()
    
    # Step 3: Start ngrok
    print("[3/4] Starting ngrok tunnel...")
    
    ngrok_process = subprocess.Popen(
        [ngrok_path, "http", "5000"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    
    print("[OK] Ngrok started in new window")
    print("[INFO] Waiting for ngrok to establish tunnel...\n")
    
    # Step 4: Get public URL
    print("[4/4] Fetching public URL...")
    time.sleep(5)
    
    # 尝试多次获取 URL
    public_url = None
    for i in range(10):
        try:
            response = urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels", timeout=3)
            data = json.loads(response.read().decode())
            
            if data.get('tunnels'):
                public_url = data['tunnels'][0]['public_url']
                break
        except:
            pass
        time.sleep(1)
    
    if public_url:
        print("\n" + "="*60)
        print("SUCCESS! Your public URL is:")
        print("="*60)
        print(f"\n  {public_url}\n")
        print("="*60)
        print("\nShare this URL with others to access your news website!")
        print("\nLocal:  http://localhost:5000")
        print(f"Public: {public_url}")
        
        # 保存 URL
        url_file = os.path.join(server_dir, "PUBLIC_URL.txt")
        with open(url_file, 'w', encoding='utf-8') as f:
            f.write(f"News Website Public URL:\n")
            f.write(f"{public_url}\n")
            f.write(f"\nGenerated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"\nURL saved to: PUBLIC_URL.txt")
        print("="*60 + "\n")
    else:
        print("[WARNING] Cannot fetch URL automatically")
        print("[INFO] Please check the ngrok window for your public URL")
        print("[INFO] The URL looks like: https://xxxx.ngrok-free.app\n")

if __name__ == "__main__":
    main()

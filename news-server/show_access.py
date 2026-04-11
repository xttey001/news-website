"""
显示访问选项
"""
import os

print("\n" + "="*60)
print("Public Access Options")
print("="*60 + "\n")

ngrok_path = r"C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe"

print("Option 1: Ngrok (Recommended for public access)")
print("-" * 60)
print("1. Sign up (free): https://dashboard.ngrok.com/signup")
print("2. Get your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken")
print("3. Open PowerShell and run:")
print(f'   {ngrok_path} config add-authtoken YOUR_TOKEN')
print("4. Then run:")
print(f'   {ngrok_path} http 5000')
print("5. Copy the URL (looks like https://xxxx.ngrok-free.app)\n")

print("Option 2: Local Network Access (no setup needed)")
print("-" * 60)
print("Your computer IP: 192.168.1.12")
print("Others on same WiFi can access: http://192.168.1.12:5000\n")

print("Option 3: Current Status")
print("-" * 60)
print("Server is running at:")
print("  Local:   http://localhost:5000")
print("  Network: http://192.168.1.12:5000")
print("\nShare with people on same WiFi:")
print("  Just give them: http://192.168.1.12:5000\n")

print("="*60)
print("Summary")
print("="*60)
print("\nYour news website is ready!")
print("\n- Local:      http://localhost:5000")
print("- Network:    http://192.168.1.12:5000 (same WiFi)")
print("- Public:     Use Ngrok (Option 1)")
print("="*60 + "\n")

# 保存访问信息
with open("ACCESS_INFO.txt", 'w', encoding='utf-8') as f:
    f.write("News Website Access Information\n")
    f.write("="*60 + "\n\n")
    f.write("Local Access:\n")
    f.write("  http://localhost:5000\n\n")
    f.write("Network Access (same WiFi):\n")
    f.write("  http://192.168.1.12:5000\n\n")
    f.write("="*60 + "\n")
    f.write("For Public Internet Access:\n")
    f.write("="*60 + "\n\n")
    f.write("Using Ngrok:\n")
    f.write("1. Sign up: https://dashboard.ngrok.com/signup\n")
    f.write("2. Get token: https://dashboard.ngrok.com/get-started/your-authtoken\n")
    f.write(f"3. Run: {ngrok_path} config add-authtoken YOUR_TOKEN\n")
    f.write(f"4. Run: {ngrok_path} http 5000\n")
    f.write("5. Share the URL with others\n")

print("Access info saved to ACCESS_INFO.txt\n")

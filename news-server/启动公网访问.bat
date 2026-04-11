@echo off
chcp 65001 >nul
echo.
echo ================================================
echo 启动公网访问（Ngrok）
echo ================================================
echo.
echo 正在启动 Ngrok 隧道...
echo 请在新窗口中查看你的公网URL
echo.
echo 公网URL格式：https://xxxx.ngrok-free.app
echo.
echo ================================================
echo.
start "Ngrok Tunnel" "C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe" http 5000
echo Ngrok 已在新窗口启动！
echo.
echo 请在新窗口中找到 "Forwarding" 那一行
echo 复制 https:// 开头的URL分享给他人
echo.
echo ================================================
echo 本机访问：   http://localhost:5000
echo 局域网访问： http://192.168.1.12:5000
echo 公网访问：   见 Ngrok 窗口
echo ================================================
echo.
pause

@echo off
REM 使用 Ngrok 将本地服务器暴露到公网
REM 前提：已安装 ngrok (https://ngrok.com/download)

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         财经新闻网站 - 公网访问配置                        ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM 检查 ngrok 是否已安装
ngrok --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 ngrok，请先安装：
    echo    https://ngrok.com/download
    echo.
    echo 安装后，运行此脚本即可
    pause
    exit /b 1
)

echo ✅ ngrok 已安装
echo.
echo 📡 正在启动公网隧道...
echo.

REM 启动 ngrok
ngrok http 5000

pause

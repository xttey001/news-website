@echo off
chcp 65001 >nul
echo ==========================================
echo    板块轮动监控系统
echo ==========================================
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.x
    pause
    exit /b 1
)

echo [1/3] 正在检查依赖...
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo 安装requests库...
    pip install requests -q
)

echo [2/3] 正在启动监控...
echo 按 Ctrl+C 停止监控
echo.

:: 运行监控程序
python sector_rotation_monitor.py

echo.
echo 监控已停止
pause

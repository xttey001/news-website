@echo off
REM 财经新闻网站启动脚本

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         财经新闻网站 - 启动脚本                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Python，请先安装 Python 3.8+
    pause
    exit /b 1
)

REM 进入目录
cd /d "%~dp0"

REM 检查依赖
echo 📦 检查依赖...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo 📥 安装 Flask...
    pip install -r requirements.txt
)

REM 启动服务器
echo.
echo ✅ 启动服务器...
echo.
python run_server.py

pause

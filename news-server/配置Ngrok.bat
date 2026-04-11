@echo off
chcp 65001 >nul
echo.
echo ================================================
echo 一键配置 Ngrok（公网访问）
echo ================================================
echo.
echo 请按以下步骤操作：
echo.
echo 第1步：注册 Ngrok 账号（免费）
echo 网址：https://dashboard.ngrok.com/signup
echo.
echo 第2步：获取 authtoken
echo 网址：https://dashboard.ngrok.com/get-started/your-authtoken
echo 复制页面上的 authtoken（类似：2abc...xyz）
echo.
echo 第3步：在下方粘贴你的 authtoken
echo.
pause
echo.
set /p TOKEN="请输入你的 authtoken: "
echo.
echo 正在配置...
"C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe" config add-authtoken %TOKEN%
echo.
echo ================================================
echo 配置完成！
echo ================================================
echo.
echo 现在运行"启动公网访问.bat"来启动公网隧道
echo.
pause

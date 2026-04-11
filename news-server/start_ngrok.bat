@echo off
chcp 65001 >nul
echo ================================================
echo Starting Ngrok for News Website
echo ================================================
echo.
echo [1] Starting ngrok...
echo.
start "Ngrok Tunnel" "C:\Users\asus\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe" http 5000
echo.
echo [2] Ngrok started in new window!
echo.
echo [3] Waiting for tunnel to establish...
timeout /t 5 /nobreak >nul
echo.
echo [4] Fetching public URL...
echo.
echo ================================================
echo Your Public URL:
echo ================================================
echo.
echo Check the Ngrok window for your public URL
echo It looks like: https://xxxx.ngrok-free.app
echo.
echo ================================================
echo.
echo Press any key to open the URL in browser...
pause >nul
echo.
echo Opening http://127.0.0.1:4040 (Ngrok Web Interface)...
start http://127.0.0.1:4040
echo.
echo ================================================
echo Local:   http://localhost:5000
echo Public:  Check Ngrok window
echo ================================================
echo.
pause

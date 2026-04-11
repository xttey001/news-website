#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动服务器 - 简化版
"""
import os
import sys
import io

# 修复编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

os.chdir(r"C:\Users\asus\.qclaw\workspace\news-server")
sys.path.insert(0, r"C:\Users\asus\.qclaw\workspace\news-server")

from app import app

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Server starting...")
    print("="*60)
    print("\nAccess:")
    print("   Local: http://localhost:5000")
    print("   LAN: http://192.168.1.12:5000")
    print("\nPress Ctrl+C to stop\n")
    
    try:
        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\nServer stopped")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

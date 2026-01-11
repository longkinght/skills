#!/usr/bin/env python3
"""
微信朋友圈导出 - 浏览器启动脚本
启动带有远程调试端口的 Chrome 浏览器
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
# ]
# ///

import os
import sys
import subprocess
import socket
import time
from pathlib import Path

# 远程调试端口
DEBUG_PORT = 9222


def is_port_in_use(port: int) -> bool:
    """检查端口是否已被占用"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def find_chrome_path() -> str | None:
    """查找 Chrome 浏览器路径"""
    chrome_paths = [
        # Windows 常见路径
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
        # macOS 路径
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        # Linux 路径
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            return path
    return None


def start_chrome() -> bool:
    """启动带有远程调试端口的 Chrome"""
    if is_port_in_use(DEBUG_PORT):
        print(f"端口 {DEBUG_PORT} 已被占用，可能已有 Chrome 在运行")
        response = input("是否使用现有的 Chrome 实例？(y/n): ").strip().lower()
        if response == 'y':
            return True
        else:
            print("请先关闭现有的 Chrome 浏览器")
            return False

    chrome_path = find_chrome_path()
    if not chrome_path:
        print("错误：未找到 Chrome 浏览器")
        print("请安装 Chrome 浏览器后重试")
        return False

    # Chrome 启动参数
    chrome_args = [
        chrome_path,
        f"--remote-debugging-port={DEBUG_PORT}",
        "--user-data-dir=" + os.path.join(os.path.dirname(__file__), "..", "chrome_profile"),
    ]

    print(f"正在启动 Chrome 浏览器（调试端口：{DEBUG_PORT}）...")
    print("请稍候...")

    try:
        subprocess.Popen(chrome_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 等待 Chrome 启动
        for _ in range(20):
            time.sleep(0.5)
            if is_port_in_use(DEBUG_PORT):
                print("Chrome 启动成功！")
                print("\n" + "="*50)
                print("请在浏览器中：")
                print("1. 访问 weixin.qq.com 登录微信网页版")
                print("2. 或在电脑版微信中打开朋友圈")
                print("3. 确保朋友圈页面完全加载")
                print("="*50 + "\n")
                return True

        print("Chrome 启动超时，请手动检查")
        return False

    except Exception as e:
        print(f"启动 Chrome 失败：{e}")
        return False


def main():
    print("="*50)
    print("微信朋友圈导出 - 浏览器启动")
    print("="*50 + "\n")

    if start_chrome():
        print("\n浏览器已就绪，可以继续下一步操作")
        print("运行 extract.py 开始提取数据")
    else:
        print("\n浏览器启动失败")
        sys.exit(1)


if __name__ == "__main__":
    main()

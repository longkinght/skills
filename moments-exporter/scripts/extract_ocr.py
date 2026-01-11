#!/usr/bin/env python3
"""
微信朋友圈导出 - 截图 OCR 版
通过截图和 OCR 识别方式导出朋友圈数据
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
#     "pyautogui>=0.9.54",
#     "pytesseract>=0.3.10",
# ]
# ///

import os
import sys
import time
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional

try:
    import pyautogui
    from PIL import Image, ImageGrab
    import pytesseract
except ImportError as e:
    print(f"缺少依赖库：{e}")
    print("请运行: pip install pillow pyautogui pytesseract")
    sys.exit(1)


class MomentsOCRExtractor:
    """基于 OCR 的朋友圈数据提取器"""

    def __init__(self, output_dir: str = "screenshots"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.moments = []
        self.screenshot_count = 0

    def check_tesseract(self) -> bool:
        """检查 Tesseract 是否安装"""
        try:
            # 尝试常见路径
            tesseract_paths = [
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
                r"C:\Users\*scoop*\apps\tesseract-ocr\current\tesseract.exe",
            ]

            # 检查环境变量
            if os.path.exists("tesseract.exe") or self._which("tesseract"):
                pytesseract.pytesseract.tesseract_cmd = "tesseract"
                return True

            # 检查常见安装路径
            for path in tesseract_paths:
                expanded = os.path.expanduser(path)
                expanded = os.path.expandvars(expanded)
                if os.path.exists(expanded):
                    pytesseract.pytesseract.tesseract_cmd = expanded
                    print(f"找到 Tesseract: {expanded}")
                    return True

            return False

        except Exception:
            return False

    def _which(self, program: str) -> Optional[str]:
        """查找程序路径"""
        try:
            import shutil
            return shutil.which(program)
        except ImportError:
            return None

    def install_tesseract(self) -> bool:
        """安装 Tesseract OCR"""
        print("=" * 50)
        print("需要安装 Tesseract OCR")
        print("=" * 50)
        print("\n请选择安装方式：")
        print("1. 使用 scoop 安装（推荐）")
        print("2. 手动下载安装")
        print("3. 跳过（使用在线 OCR）\n")

        choice = input("请选择 (1/2/3): ").strip()

        if choice == "1":
            return self._install_with_scoop()
        elif choice == "2":
            print("\n请按以下步骤手动安装：")
            print("1. 访问: https://github.com/UB-Mannheim/tesseract/wiki")
            print("2. 下载并安装 Tesseract")
            print("3. 安装中文语言包（可选）")
            print("4. 重新运行此脚本\n")
            input("安装完成后按回车继续...")
            return self.check_tesseract()
        else:
            return False

    def _install_with_scoop(self) -> bool:
        """使用 scoop 安装 Tesseract"""
        try:
            print("\n正在使用 scoop 安装 Tesseract...")
            subprocess.run(["scoop", "install", "tesseract-ocr"], check=True,
                         capture_output=True, text=True)
            print("安装成功！")
            return self.check_tesseract()
        except FileNotFoundError:
            print("未找到 scoop，请先安装 scoop：")
            print("在 PowerShell 中运行: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser")
            print("然后运行: irm get.scoop.sh | iex")
            return False
        except subprocess.CalledProcessError:
            print("scoop 安装失败，请手动安装")
            return False

    def take_screenshot(self, region: tuple = None) -> Image.Image:
        """截取屏幕截图"""
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()

        # 保存截图
        screenshot_path = self.output_dir / f"screenshot_{self.screenshot_count:04d}.png"
        screenshot.save(screenshot_path)
        self.screenshot_count += 1

        return screenshot

    def ocr_image(self, image: Image.Image, lang: str = "chi_sim+eng") -> str:
        """使用 OCR 识别图片中的文字"""
        try:
            text = pytesseract.image_to_string(image, lang=lang)
            return text
        except Exception as e:
            print(f"OCR 识别失败: {e}")
            return ""

    def extract_from_screen(self, scrolls: int = 10, delay: float = 2.0) -> list:
        """从屏幕提取朋友圈数据"""
        print("\n" + "=" * 50)
        print("朋友圈数据提取（截图 OCR 模式）")
        print("=" * 50)

        print("\n【重要提示】")
        print("1. 请确保微信朋友圈窗口在最前面")
        print("2. 请将窗口调整到合适大小")
        print("3. 准备好后，此脚本将自动:")
        print("   - 截取屏幕")
        print("   - 使用 OCR 识别文字")
        print("   - 自动滚动并重复")

        input("\n按回车键开始...")

        # 首先选择区域（可选）
        print("\n将鼠标移到朋友圈区域左上角...")
        time.sleep(3)

        # 获取当前鼠标位置作为区域起点
        start_x, start_y = pyautogui.position()
        print(f"起点: ({start_x}, {start_y})")

        print("\n将鼠标移到朋友圈区域右下角...")
        time.sleep(3)

        end_x, end_y = pyautogui.position()
        print(f"终点: ({end_x}, {end_y})")

        region = (start_x, start_y, end_x - start_x, end_y - start_y)
        print(f"\n截图区域: {region}")

        input("\n确认区域后按回车开始提取...")

        all_text = []
        last_text_hash = ""

        for i in range(scrolls):
            print(f"\r进度: {i+1}/{scrolls}", end="")

            # 截图
            screenshot = self.take_screenshot(region=region)

            # OCR 识别
            text = self.ocr_image(screenshot)

            # 检查是否有新内容
            text_hash = hash(text)
            if text_hash != last_text_hash:
                all_text.append({
                    "scroll": i + 1,
                    "time": datetime.now().isoformat(),
                    "text": text,
                    "screenshot": f"screenshot_{self.screenshot_count-1:04d}.png"
                })
                last_text_hash = text_hash

            # 滚动
            pyautogui.scroll(-3)  # 向下滚动
            time.sleep(delay)

        print(f"\n\n完成！共截取 {len(all_text)} 次有效内容")

        return all_text

    def parse_moments_from_text(self, ocr_results: list) -> list:
        """从 OCR 结果中解析朋友圈结构"""
        parsed_moments = []

        for result in ocr_results:
            text = result["text"]
            lines = text.split("\n")

            # 简单的解析逻辑（可根据实际效果调整）
            current_moment = {
                "screenshot": result["screenshot"],
                "time": result["time"],
                "raw_text": text,
                "parsed_content": []
            }

            for line in lines:
                line = line.strip()
                if len(line) > 5:  # 过滤太短的行
                    current_moment["parsed_content"].append(line)

            parsed_moments.append(current_moment)

        return parsed_moments

    def save_results(self, ocr_results: list, parsed_moments: list, output_file: str = "moments_ocr.json"):
        """保存结果"""
        output_data = {
            "export_time": datetime.now().isoformat(),
            "total_screenshots": self.screenshot_count,
            "ocr_results": ocr_results,
            "parsed_moments": parsed_moments
        }

        output_path = Path(output_file)
        output_path.write_text(
            json.dumps(output_data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print(f"\n结果已保存到: {output_path.absolute()}")
        return output_path


def main():
    parser = argparse.ArgumentParser(description="通过截图 OCR 提取微信朋友圈")
    parser.add_argument("--scrolls", "-s", type=int, default=20, help="滚动次数")
    parser.add_argument("--delay", "-d", type=float, default=2.0, help="每次滚动后等待秒数")
    parser.add_argument("--output", "-o", default="moments_ocr.json", help="输出文件")
    parser.add_argument("--screenshots-dir", default="screenshots", help="截图保存目录")

    args = parser.parse_args()

    extractor = MomentsOCRExtractor(output_dir=args.screenshots_dir)

    # 检查 Tesseract
    if not extractor.check_tesseract():
        print("\n⚠️  未找到 Tesseract OCR")
        if not extractor.install_tesseract():
            print("\n将使用无 OCR 模式（仅截图）")

    # 提取数据
    ocr_results = extractor.extract_from_screen(
        scrolls=args.scrolls,
        delay=args.delay
    )

    # 解析结果
    parsed_moments = extractor.parse_moments_from_text(ocr_results)

    # 保存
    extractor.save_results(ocr_results, parsed_moments, args.output)

    print(f"\n截图保存在: {extractor.output_dir.absolute()}")


if __name__ == "__main__":
    main()

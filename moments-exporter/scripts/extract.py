#!/usr/bin/env python3
"""
微信朋友圈导出 - 数据提取脚本
通过 Chrome DevTools Protocol 提取朋友圈数据
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "websockets>=12.0",
#     "aiohttp>=3.9.0",
# ]
# ///

import os
import sys
import json
import asyncio
import argparse
import websockets
from datetime import datetime
from pathlib import Path

# Chrome 远程调试设置
DEBUG_PORT = 9222
DEBUG_URL = f"ws://localhost:{DEBUG_PORT}/devtools/page"


class MomentsExtractor:
    """朋友圈数据提取器"""

    def __init__(self, max_scroll: int = 50):
        self.max_scroll = max_scroll
        self.websocket = None
        self.message_id = 0
        self.moments = []

    def _next_id(self) -> int:
        """获取下一个消息 ID"""
        self.message_id += 1
        return self.message_id

    async def connect(self) -> bool:
        """连接到 Chrome DevTools"""
        try:
            # 首先获取可用的页面列表
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://localhost:{DEBUG_PORT}/json") as resp:
                    if resp.status != 200:
                        print("无法连接到 Chrome DevTools")
                        return False

                    pages = await resp.json()

                    # 查找微信相关的页面
                    weixin_pages = [p for p in pages if "weixin" in p.get("url", "").lower() or "wx" in p.get("title", "").lower()]

                    if weixin_pages:
                        target_url = weixin_pages[0]["webSocketDebuggerUrl"]
                        print(f"找到微信页面：{weixin_pages[0]['title']}")
                    else:
                        # 使用第一个页面
                        if not pages:
                            print("未找到打开的页面，请确保 Chrome 已打开朋友圈页面")
                            return False
                        target_url = pages[0]["webSocketDebuggerUrl"]
                        print(f"使用页面：{pages[0].get('title', 'Unknown')}")

            self.websocket = await websockets.connect(target_url)
            print("已连接到 Chrome DevTools")

            # 启用必要的域
            await self.send_command("Page.enable")
            await self.send_command("DOM.enable")
            await self.send_command("Runtime.enable")

            return True

        except Exception as e:
            print(f"连接失败：{e}")
            print("请确保：")
            print("1. 已运行 start_browser.py 启动 Chrome")
            print("2. 已在 Chrome 中打开微信朋友圈页面")
            return False

    async def send_command(self, method: str, params: dict = None) -> dict:
        """发送 DevTools 命令"""
        message = {
            "id": self._next_id(),
            "method": method,
            "params": params or {}
        }

        await self.websocket.send(json.dumps(message))

        # 等待响应
        while True:
            response = json.loads(await self.websocket.recv())
            if response.get("id") == message["id"]:
                return response

    async def execute_script(self, script: str) -> any:
        """在页面中执行 JavaScript"""
        result = await self.send_command("Runtime.evaluate", {
            "expression": script,
            "awaitPromise": True,
            "returnByValue": True
        })

        if "error" in result:
            print(f"脚本执行错误：{result['error']}")
            return None

        return result.get("result", {}).get("value")

    async def extract_moments(self) -> list:
        """提取朋友圈数据"""
        print("开始提取朋友圈数据...")

        # 通用的朋友圈提取脚本（适配多种微信版本）
        extract_script = """
        (function() {
            const moments = [];

            // 微信朋友圈的选择器可能变化，这里使用通用的选择策略
            const selectors = [
                '.moments',           // 常见选择器
                '.timeline',          // 时间线
                '[id*="moment"]',     // 包含 moment 的元素
                '[id*="timeline"]',   // 包含 timeline 的元素
                '.weixin-moments',    // 微信官方可能的选择器
            ];

            // 尝试找到朋友圈容器
            let container = null;
            for (const selector of selectors) {
                container = document.querySelector(selector);
                if (container) break;
            }

            // 如果没找到，尝试查找所有可能的帖子
            const posts = document.querySelectorAll('[class*="moment"], [class*="timeline"], [class*="post"]');

            posts.forEach((post, index) => {
                try {
                    // 提取文本内容
                    const contentEl = post.querySelector('[class*="content"], [class*="text"], p, span');
                    const content = contentEl ? contentEl.innerText.trim() : '';

                    // 提取图片
                    const images = [];
                    const imgEls = post.querySelectorAll('img');
                    imgEls.forEach(img => {
                        if (img.src && !img.src.includes('emoji')) {
                            images.push(img.src);
                        }
                    });

                    // 提取时间
                    const timeEl = post.querySelector('[class*="time"], [class*="date"]');
                    const time = timeEl ? timeEl.innerText.trim() : '';

                    // 提取作者
                    const authorEl = post.querySelector('[class*="author"], [class*="nickname"], [class*="name"]');
                    const author = authorEl ? authorEl.innerText.trim() : '';

                    if (content || images.length > 0) {
                        moments.push({
                            index: index,
                            author: author,
                            content: content,
                            publish_time: time,
                            images: images,
                            likes: [],
                            comments: []
                        });
                    }
                } catch (e) {
                    // 跳过解析失败的帖子
                }
            });

            return moments;
        })();
        """

        # 执行滚动和提取
        for i in range(self.max_scroll):
            print(f"\r滚动中... ({i+1}/{self.max_scroll})", end="")

            # 滚动到底部
            scroll_script = """
            (function() {
                window.scrollTo(0, document.body.scrollHeight);
                return true;
            })();
            """

            await self.execute_script(scroll_script)

            # 等待内容加载
            await asyncio.sleep(1)

        print("\n提取完成，正在解析数据...")

        # 执行提取脚本
        result = await self.execute_script(extract_script)

        if result and isinstance(result, list):
            self.moments = result
            print(f"成功提取 {len(self.moments)} 条朋友圈")
        else:
            print("未能提取到朋友圈数据")
            print("提示：请确保已正确打开微信朋友圈页面")

        return self.moments

    async def close(self):
        """关闭连接"""
        if self.websocket:
            await self.websocket.close()


async def main():
    parser = argparse.ArgumentParser(description="提取微信朋友圈数据")
    parser.add_argument("--url", help="朋友圈页面 URL（可选）")
    parser.add_argument("--output", "-o", default="moments.json", help="输出 JSON 文件路径")
    parser.add_argument("--max-scroll", type=int, default=50, help="最大滚动次数")

    args = parser.parse_args()

    print("="*50)
    print("微信朋友圈导出 - 数据提取")
    print("="*50 + "\n")

    extractor = MomentsExtractor(max_scroll=args.max_scroll)

    if not await extractor.connect():
        sys.exit(1)

    try:
        moments = await extractor.extract_moments()

        if moments:
            # 构建输出数据
            output_data = {
                "export_time": datetime.now().isoformat(),
                "total_count": len(moments),
                "moments": moments
            }

            # 保存到文件
            output_path = Path(args.output)
            output_path.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")

            print(f"\n数据已保存到：{output_path.absolute()}")
            print(f"共提取 {len(moments)} 条朋友圈")

            # 显示前几条预览
            if moments:
                print("\n预览前 3 条：")
                for i, moment in enumerate(moments[:3]):
                    print(f"\n{i+1}. {moment.get('publish_time', '未知时间')} - {moment.get('author', '未知作者')}")
                    content = moment.get('content', '')
                    print(f"   {content[:100]}{'...' if len(content) > 100 else ''}")

    finally:
        await extractor.close()


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3
"""
微信朋友圈导出 - 格式导出脚本
支持导出为 Markdown、JSON、PDF 格式
"""

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown2>=2.4.0",
# ]
# ///

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Any


class MomentsExporter:
    """朋友圈数据导出器"""

    def __init__(self, data: dict):
        self.data = data
        self.moments = data.get("moments", [])

    def export_markdown(self, output_path: str) -> bool:
        """导出为 Markdown 格式"""
        try:
            lines = []

            # 标题
            lines.append("# 微信朋友圈导出\n")
            lines.append(f"**导出时间**：{self.data.get('export_time', 'Unknown')}\n")
            lines.append(f"**总共**：{len(self.moments)} 条朋友圈\n")
            lines.append("\n---\n\n")

            # 按时间排序（如果有时间信息）
            sorted_moments = sorted(
                self.moments,
                key=lambda x: x.get("publish_time", ""),
                reverse=True
            )

            for moment in sorted_moments:
                # 标题（时间 + 作者）
                time_str = moment.get("publish_time", "未知时间")
                author = moment.get("author", "未知作者")
                lines.append(f"## {time_str} - {author}\n")

                # 内容
                content = moment.get("content", "")
                if content:
                    lines.append(f"{content}\n")

                # 图片
                images = moment.get("images", [])
                if images:
                    lines.append("\n**图片**：\n")
                    for img_url in images:
                        lines.append(f"\n")
                        lines.append(f"")
                        lines.append(f"\n")

                # 点赞
                likes = moment.get("likes", [])
                if likes:
                    lines.append(f"\n**点赞**：{'、'.join(likes)}\n")

                # 评论
                comments = moment.get("comments", [])
                if comments:
                    lines.append(f"\n**评论**：\n")
                    for comment in comments:
                        commenter = comment.get("author", "匿名")
                        comment_text = comment.get("content", "")
                        lines.append(f"- {commenter}：{comment_text}\n")

                lines.append("\n---\n\n")

            output = Path(output_path)
            output.write_text("".join(lines), encoding="utf-8")

            print(f"Markdown 文件已保存到：{output.absolute()}")
            return True

        except Exception as e:
            print(f"Markdown 导出失败：{e}")
            return False

    def export_json(self, output_path: str) -> bool:
        """导出为 JSON 格式（已是 JSON，直接复制）"""
        try:
            output = Path(output_path)
            output.write_text(
                json.dumps(self.data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

            print(f"JSON 文件已保存到：{output.absolute()}")
            return True

        except Exception as e:
            print(f"JSON 导出失败：{e}")
            return False

    def export_pdf(self, output_path: str) -> bool:
        """导出为 PDF 格式"""
        try:
            # 首先生成 HTML
            html_content = self._generate_html()

            # 保存临时 HTML 文件
            temp_html = Path(output_path).with_suffix(".html")
            temp_html.write_text(html_content, encoding="utf-8")

            print(f"HTML 文件已生成：{temp_html.absolute()}")
            print("\n要生成 PDF，请按以下步骤操作：")
            print("1. 在浏览器中打开上述 HTML 文件")
            print("2. 按 Ctrl+P 打开打印对话框")
            print("3. 选择「另存为 PDF」")
            print("4. 点击保存")

            # 尝试自动打开浏览器
            os.startfile(str(temp_html.absolute()))

            return True

        except Exception as e:
            print(f"PDF 导出失败：{e}")
            return False

    def _generate_html(self) -> str:
        """生成 HTML 内容"""
        template_path = Path(__file__).parent.parent / "lib" / "templates" / "report.html"

        if template_path.exists():
            template = template_path.read_text(encoding="utf-8")
        else:
            # 默认模板
            template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微信朋友圈导出</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
        }
        .header h1 { color: #07c160; }
        .meta { color: #666; font-size: 14px; margin-top: 10px; }
        .moment {
            border-left: 3px solid #07c160;
            padding-left: 20px;
            margin-bottom: 30px;
        }
        .moment-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .author { font-weight: bold; color: #333; }
        .time { color: #999; font-size: 14px; }
        .content { margin-bottom: 10px; white-space: pre-wrap; }
        .images {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 10px 0;
        }
        .images img {
            max-width: 200px;
            max-height: 200px;
            border-radius: 4px;
            cursor: pointer;
        }
        .likes, .comments { margin-top: 10px; font-size: 14px; }
        .likes { color: #07c160; }
        .comments { color: #666; }
        .divider { height: 1px; background: #eee; margin: 30px 0; }
        @media print {
            body { background: white; padding: 0; }
            .container { box-shadow: none; padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>微信朋友圈导出</h1>
            <div class="meta">
                <p>导出时间：{{ export_time }}</p>
                <p>总共：{{ total_count }} 条朋友圈</p>
            </div>
        </div>
        {{ moments_html }}
    </div>
</body>
</html>"""

        # 生成朋友圈 HTML
        moments_html = []

        for moment in self.moments:
            moment_html = f"""
            <div class="moment">
                <div class="moment-header">
                    <span class="author">{moment.get('author', '未知作者')}</span>
                    <span class="time">{moment.get('publish_time', '未知时间')}</span>
                </div>
                <div class="content">{moment.get('content', '')}</div>
            """

            # 图片
            images = moment.get("images", [])
            if images:
                moment_html += '<div class="images">'
                for img_url in images:
                    moment_html += f'<img src="{img_url}" alt="图片" onerror="this.style.display=\'none\'">'
                moment_html += '</div>'

            # 点赞
            likes = moment.get("likes", [])
            if likes:
                moment_html += f'<div class="likes">❤️ {", ".join(likes)}</div>'

            # 评论
            comments = moment.get("comments", [])
            if comments:
                moment_html += '<div class="comments">'
                for comment in comments:
                    commenter = comment.get("author", "匿名")
                    comment_text = comment.get("content", "")
                    moment_html += f'<div>💬 {commenter}：{comment_text}</div>'
                moment_html += '</div>'

            moment_html += '<div class="divider"></div></div>'
            moments_html.append(moment_html)

        # 替换模板变量
        html = template.replace("{{ export_time }}", self.data.get("export_time", "Unknown"))
        html = html.replace("{{ total_count }}", str(len(self.moments)))
        html = html.replace("{{ moments_html }}", "".join(moments_html))

        return html


def main():
    parser = argparse.ArgumentParser(description="导出朋友圈数据为指定格式")
    parser.add_argument("input", help="输入的 JSON 文件路径")
    parser.add_argument("--format", "-f", choices=["markdown", "json", "pdf"], default="markdown", help="输出格式")
    parser.add_argument("--output", "-o", help="输出文件路径（默认根据格式自动命名）")

    args = parser.parse_args()

    # 读取输入文件
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：文件不存在 - {args.input}")
        sys.exit(1)

    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"错误：无法解析 JSON 文件 - {e}")
        sys.exit(1)

    # 确定输出路径
    if args.output:
        output_path = args.output
    else:
        base_name = input_path.stem
        extensions = {
            "markdown": ".md",
            "json": ".json",
            "pdf": ".pdf"
        }
        output_path = f"{base_name}_export{extensions[args.format]}"

    print("="*50)
    print("微信朋友圈导出 - 格式转换")
    print("="*50 + "\n")

    # 导出
    exporter = MomentsExporter(data)

    if args.format == "markdown":
        success = exporter.export_markdown(output_path)
    elif args.format == "json":
        success = exporter.export_json(output_path)
    elif args.format == "pdf":
        success = exporter.export_pdf(output_path)

    if success:
        print(f"\n导出完成！")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

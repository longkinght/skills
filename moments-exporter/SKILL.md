---
name: moments-exporter
description: 导出微信朋友圈数据。使用截图 + OCR 方式提取朋友圈内容，支持导出为 Markdown、JSON、PDF 格式。当用户提到"导出朋友圈"、"备份朋友圈"、"朋友圈数据"时使用此 skill。
---

# 微信朋友圈导出工具

通过**截图 + OCR** 方式导出微信朋友圈数据，无需网页版，直接从电脑版微信窗口提取。

## 功能特性

- 自动截图并使用 OCR 识别文字内容
- 自动滚动并持续提取
- 保存原始截图供人工核对
- 支持导出为 Markdown、JSON、PDF 格式

## 前置条件

1. 电脑版微信已登录
2. Python 3.10+ 环境
3. （可选）Tesseract OCR 引擎，用于文字识别

## 使用方法

### 一键提取（推荐）

直接运行提取脚本，按提示操作：

```bash
python C:\Users\longk\.claude\skills\moments-exporter\scripts\extract_ocr.py
```

### 详细步骤

**第一步：打开朋友圈**

在电脑版微信中打开朋友圈，确保窗口可见。

**第二步：运行提取脚本**

```bash
python C:\Users\longk\.claude\skills\moments-exporter\scripts\extract_ocr.py --scrolls 30 --delay 1.5
```

参数说明：
- `--scrolls`: 滚动次数（默认 20 次）
- `--delay`: 每次滚动后等待秒数（默认 2 秒）
- `--output`: 输出文件路径（默认 moments_ocr.json）
- `--screenshots-dir`: 截图保存目录（默认 screenshots）

**第三步：按提示操作**

脚本会提示你：
1. 将鼠标移到朋友圈区域左上角，等待 3 秒
2. 将鼠标移到朋友圈区域右下角，等待 3 秒
3. 确认后自动开始截图和 OCR 识别

**第四步：查看结果**

- 截图保存在 `screenshots/` 目录
- OCR 识别结果保存在 `moments_ocr.json`
- 原始文字内容已提取并结构化

### 导出为其他格式

**导出为 Markdown：**
```bash
python C:\Users\longk\.claude\skills\moments-exporter\scripts\export.py moments_ocr.json --format markdown
```

**导出为 PDF：**
```bash
python C:\Users\longk\.claude\skills\moments-exporter\scripts\export.py moments_ocr.json --format pdf
```

## 输出格式说明

### JSON 格式
```json
{
  "export_time": "2025-01-10T12:00:00",
  "moments": [
    {
      "author": "昵称",
      "content": "朋友圈内容",
      "publish_time": "2025-01-09 18:30",
      "images": ["url1", "url2"],
      "likes": ["点赞者1", "点赞者2"],
      "comments": [
        {"author": "评论者", "content": "评论内容"}
      ]
    }
  ]
}
```

### Markdown 格式
```markdown
# 微信朋友圈导出

导出时间：2025-01-10 12:00:00

## 2025-01-09 18:30 - 昵称

朋友圈内容

![图片](url1)

**点赞**：点赞者1、点赞者2

**评论**：
- 评论者：评论内容
```

### PDF 格式
生成排版美观的 PDF 文档，包含图片和时间线。

## 示例工作流

```bash
# 1. 启动浏览器并登录微信
python scripts/start_browser.py

# 2. 在浏览器中打开朋友圈页面，然后运行提取脚本
python scripts/extract.py --max-scroll 100

# 3. 导出为多种格式
python scripts/export.py moments.json --format markdown
python scripts/export.py moments.json --format pdf
```

## 注意事项

1. 首次使用需要手动登录微信
2. 提取速度取决于网络和内容数量
3. 图片需要网络连接才能在导出文件中显示
4. 建议在电脑版微信中使用，网页版功能可能受限
5. 大量数据提取可能需要较长时间，请耐心等待

## 故障排除

**无法连接浏览器**：确保 Chrome 已启动并开启远程调试

**内容加载不全**：增加 `--max-scroll` 参数值

**图片无法显示**：检查网络连接和图片 URL 有效性

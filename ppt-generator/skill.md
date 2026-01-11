---
name: ppt-generator
description: 将文本内容转换为精美的 HTML PPT 演示文稿。当用户说"帮我做个 PPT"、"把内容转化为 PPT"、"生成演示文稿"、"做个幻灯片"或提到 PPT、演示、presentation 时使用。
allowed-tools: Read, Write, Edit
---

# PPT 生成器 (PPT Generator)

将任何文本内容转换为基于 card.md 设计规范的精美 HTML PPT 演示文稿。

## 触发关键词

用户可以通过以下方式触发此 skill：
- "帮我做个 PPT"
- "把 [文件名] 转化为 PPT"
- "生成一个关于 [主题] 的演示文稿"
- "做个幻灯片"
- "把这个内容做成 presentation"

## 工作流程

### 1. 获取归属标记
**重要：在开始生成之前，必须先询问用户需要在右上角显示什么归属标记。**

示例对话：
- "你希望在 PPT 右上角显示什么标记？（例如：你的名字、品牌名、公司名等）"
- 如果用户没有明确说明，不要擅自开始生成

### 2. 获取内容源
- 如果用户指定了文件（如 "把 xxx.md 做成 PPT"），使用 Read 工具读取文件内容
- 如果用户只提供了主题但没有文件，询问用户：
  - 是否有现成的内容文件？
  - 是否需要基于主题生成内容大纲？

### 3. 内容分析与结构化
分析内容并将其转换为适合 PPT 的结构：

**内容识别规则：**
- **标题识别**：
  - Markdown 的 `# 标题` 或 `## 标题` -> PPT 封面或章节标题
  - 文档第一行通常是主标题

- **章节划分**：
  - `## 章节名` -> 新的 PPT 页面
  - 每个章节独立成页

- **要点提取**：
  - 列表项 (`-` 或 `*` 开头) -> PPT 要点
  - 段落文字 -> 根据长度决定是否分页
  - 每页最多 3-5 个要点，避免信息过载

- **引用处理**：
  - `> 引用文字` -> 使用 quote 样式展示
  - 适合用于重要观点或名言

**分页原则：**
- 第 1 页：封面（主标题 + 副标题）
- 第 2-N 页：内容页（每个章节或主题一页）
- 最后一页：结束页（可选，如品牌信息、联系方式等）
- 每页内容简洁，宁可多分几页也不要挤在一起

### 4. 应用设计规范

**严格遵循 [card.md](card.md) 中的设计规范：**

#### 核心设计元素：
1. **琉光手稿风格**：印刷品秩序感 + 玻璃拟态未来感
2. **字体系统**：
   - 中文：Noto Serif SC (大字号, 粗字重)
   - 英文：Poppins (小字号, 轻字重)
3. **技术栈**：TailwindCSS + Google Fonts + Font Awesome (CDN)

#### 视觉精致化（参考 card.md 第 IV 章）：
1. **多层阴影系统**：4层渐进式阴影创造深度
2. **玻璃拟态效果**：blur(20px) + 渐变背景 + 内阴影
3. **渐变运用**：标题文字渐变、背景渐变、装饰渐变
4. **响应式排版**：clamp() + 2.0 行高 + 精心字间距
5. **装饰元素**：图标包装器、装饰线、引用装饰、高亮效果
6. **流畅动画**：页面切换动画 + 按钮悬停效果
7. **交互优化**：方向键 + 空格键翻页 + 下载功能
8. **色彩层次**：灰度层次创造深度
9. **视觉节奏**：统一间距系统 + 充足留白
10. **品质检查**：确保每个细节都经得起审视

### 5. 生成 HTML PPT

**HTML 结构模板：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[从内容中提取的标题]</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        /* 参考 card.md 中的完整样式系统 */
        /* 包括：阴影、玻璃拟态、渐变、排版、动画等 */
    </style>
</head>
<body>
    <!-- 下载按钮 -->
    <button id="downloadBtn" onclick="downloadSlide()">
        <i class="fas fa-download"></i> 下载当前页
    </button>

    <!-- 导航按钮 -->
    <button id="prevBtn" class="nav-btn" onclick="prevSlide()">
        <i class="fas fa-chevron-left"></i> 上一页
    </button>
    <button id="nextBtn" class="nav-btn" onclick="nextSlide()">
        下一页 <i class="fas fa-chevron-right"></i>
    </button>

    <!-- 页码指示器 -->
    <div class="page-indicator" id="pageIndicator"></div>

    <!-- 幻灯片内容 -->
    <div class="slide" id="slide1">
        <div class="absolute top-6 right-8 brand">[用户指定的归属标记]</div>
        <!-- 封面内容 -->
    </div>

    <div class="slide hidden" id="slide2">
        <div class="absolute top-6 right-8 brand">[用户指定的归属标记]</div>
        <!-- 内容页 -->
    </div>

    <!-- 更多幻灯片... -->

    <script>
        /* 页面切换逻辑 */
        /* 键盘导航支持 */
        /* 下载功能实现 */
    </script>
</body>
</html>
```

**关键实现细节：**
- 每个 slide 使用 `hidden` 类控制显示/隐藏
- 当前页面添加动画效果
- 右上角固定显示用户指定的归属标记
- 支持键盘导航（左右箭头 + 空格键）
- 下载时临时隐藏所有按钮和指示器

### 6. 保存文件

**文件命名规则：**
- 如果用户指定了输出文件名，使用用户指定的名称
- 如果用户没有指定，根据内容标题生成文件名
- 默认格式：`[内容标题]_presentation.html` 或 `presentation_[日期].html`
- 保存在当前工作目录

**保存后提示用户：**
- 文件保存位置
- 如何打开（在浏览器中打开）
- 如何使用（方向键或空格键翻页）
- 如何下载单页（点击左上角下载按钮）

## 设计原则

### 内容原则
1. **简洁至上**：每页最多 3-5 个要点
2. **视觉层次**：标题 > 副标题 > 正文 > 注释
3. **留白充足**：让内容呼吸，避免拥挤
4. **逻辑清晰**：按照内容的自然逻辑分页

### 视觉原则
1. **极简但不简陋**：通过细节创造品质感
2. **层次创造深度**：多层阴影、渐变、玻璃效果
3. **动画增强体验**：流畅的过渡和反馈
4. **响应式设计**：适配不同屏幕尺寸

### 交互原则
1. **直观易用**：键盘导航 + 页码指示
2. **即时反馈**：按钮悬停、点击效果
3. **功能完整**：下载、翻页、导航

## 示例对话

### 示例 1：基于现有文件生成

**用户**：帮我把 product_intro.md 做成 PPT

**助手**：
1. 询问："你希望在 PPT 右上角显示什么标记？"
2. 用户回答："codesome"
3. 读取 product_intro.md 文件
4. 分析内容结构（标题、章节、要点）
5. 读取 card.md 设计规范
6. 生成 HTML PPT，包含：
   - 封面页（产品介绍）
   - 内容页（根据章节分页）
   - 每页右上角显示 "codesome"
7. 保存为 `product_intro_presentation.html`
8. 提示用户如何使用

### 示例 2：基于主题生成

**用户**：生成一个关于 AI 技术的 PPT

**助手**：
1. 询问："你希望在 PPT 右上角显示什么标记？"
2. 询问："你有现成的内容文件吗？还是需要我基于主题生成大纲？"
3. 如果用户选择生成大纲：
   - 创建 AI 技术相关的内容大纲
   - 应用设计规范生成 PPT
4. 保存并提示用户

### 示例 3：指定输出文件名

**用户**：把 report.md 做成 PPT，保存为 annual_report.html

**助手**：
1. 询问归属标记
2. 读取 report.md
3. 生成 PPT
4. 保存为用户指定的 `annual_report.html`

## 品质保证

在生成 PPT 之前，确保：
- [ ] 已询问并获得用户的归属标记
- [ ] 内容已正确分页，每页不超过 5 个要点
- [ ] 应用了完整的设计规范（参考 card.md）
- [ ] 包含所有必需的 CDN 资源
- [ ] 实现了完整的交互功能（导航、下载）
- [ ] 代码格式正确，可以直接在浏览器中运行

在生成 PPT 之后，提醒用户：
- [ ] 文件保存位置
- [ ] 如何打开和使用
- [ ] 如何自定义（如果需要）

## 注意事项

1. **必须先询问归属标记**：这是 card.md 规范的强制要求
2. **严格遵循设计规范**：不要偷工减料，确保视觉品质
3. **内容适配**：根据内容长度合理分页
4. **测试可用性**：确保生成的 HTML 可以直接运行
5. **用户友好**：提供清晰的使用说明

## 技术要求

- 单一 HTML 文件，包含所有样式和脚本
- 使用 CDN 加载外部资源（字体、图标、库）
- 支持现代浏览器（Chrome、Firefox、Safari、Edge）
- 响应式设计，适配不同屏幕
- 无需服务器，可直接在浏览器中打开

## 参考资源

- 完整设计规范：lib/card.md

# 🎨 PPT Generator - AI驱动的演示文稿生成器

> 基于 Google Nano Banana Pro，一键将文档内容转化为高质量专业PPT

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Claude Code](https://img.shields.io/badge/Claude-Code%20Skill-orange.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

**作者**: 黄彬 | **平台**: Claude Code

[快速开始](#-一键使用提示词) • [功能特性](#-功能特性) • [安装指南](#-安装方法) • [风格展示](#-内置风格) • [使用示例](#-使用示例)

</div>

---

## 📖 项目简介

PPT Generator 是一个强大的 Claude Code Skill，能够智能分析你的文档内容，自动规划PPT结构，并使用 Google 最新的 **Nano Banana Pro** 图像生成模型，生成专业级的16:9高清PPT图片。

### ✨ 核心亮点

- 🤖 **智能文档分析** - 自动提取核心要点，规划最佳PPT结构
- 🎨 **多风格支持** - 内置渐变毛玻璃、矢量插画等专业风格
- 🖼️ **高质量输出** - 支持2K/4K分辨率，16:9比例
- 📊 **智能布局** - 自动识别封面页、内容页、数据页
- 🎬 **HTML5播放器** - 内置优雅的网页播放器，支持键盘导航
- ⚡ **快速生成** - 2K约30秒/页，5页PPT仅需2.5分钟

---

## 🚀 一键使用提示词

### 方法一：一键安装并使用（推荐）

> 复制下面的提示词，粘贴到 Claude Code 对话框，即可完成全自动安装配置

```
请帮我安装并配置 PPT Generator Skill，然后立即使用它：

## 第一步：克隆项目并安装
1. 克隆项目到本地：
   git clone https://github.com/longkinght/skills.git
   cd skills

2. 创建 Python 虚拟环境：
   python3 -m venv venv

   # macOS/Linux 激活环境
   source venv/bin/activate

   # Windows 激活环境（如果是Windows系统）
   # venv\Scripts\activate

3. 安装Python依赖：
   pip install google-genai pillow

## 第二步：配置环境变量
请将下面的 YOUR_GEMINI_API_KEY 替换为我的实际 API 密钥：

对于 macOS/Linux（zsh shell）：
echo 'export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"' >> ~/.zshrc
source ~/.zshrc

对于 macOS/Linux（bash shell）：
echo 'export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"' >> ~/.bashrc
source ~/.bashrc

对于 Windows（PowerShell）：
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY", "User")

## 第三步：验证安装
运行测试命令：
./run.sh --help

如果显示帮助信息，说明安装成功！

---

【重要】请在执行前提醒我：
1. 将所有 YOUR_GEMINI_API_KEY 替换为我的实际 Google AI API 密钥
2. API密钥获取地址：https://makersuite.google.com/app/apikey
3. 确认我使用的操作系统（macOS/Linux/Windows）

安装完成后，请告诉我如何使用这个 Skill 生成我的第一个PPT！
```

### 方法二：已安装用户快速使用

> 如果你已经安装好了项目，直接复制这个提示词使用

```
我想使用 PPT Generator 生成一个专业的演示文稿。

项目路径：skills/

请基于我提供的内容，生成一个 [5/10/15/20] 页的PPT，
使用 [渐变毛玻璃卡片风格/矢量插画风格]，分辨率选择 [2K/4K]。

我的文档内容是：
【在这里粘贴你的文档内容，或者提供文档路径】

例如：
---
# AI产品设计的未来

## 背景
当前AI产品设计面临的挑战...

## 核心观点
1. 用户体验优先
2. 技术与人性的平衡
3. 伦理考量

## 案例研究
...
---

请帮我分析内容并生成PPT！
```

---

## 📦 安装方法

### 前置要求

- **Python 3.8+**
- **Git**
- **Google AI API密钥** - [点击获取](https://makersuite.google.com/app/apikey)

### 手动安装步骤

#### 1️⃣ 克隆项目

```bash
git clone https://github.com/longkinght/skills.git
cd skills
```

#### 2️⃣ 创建虚拟环境

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

#### 3️⃣ 安装依赖

```bash
pip install google-genai pillow
```

#### 4️⃣ 配置API密钥

**推荐方式：系统环境变量**

```bash
# macOS/Linux (zsh)
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# macOS/Linux (bash)
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc

# Windows PowerShell
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "your-api-key-here", "User")
```

**替代方式：.env文件**

```bash
cp .env.example .env
# 编辑 .env 文件，将 your-api-key-here 替换为你的实际API密钥
```

#### 5️⃣ 验证安装

```bash
./run.sh --help
```

如果显示使用说明，说明安装成功！

---

## 💡 使用指南

### 在 Claude Code 中使用

#### 基础用法示例

```
我想基于这份产品文档生成一个10页的PPT：

【文档标题】产品路线图 2024 Q1

【内容】
1. 市场分析
   - 用户增长趋势
   - 竞争对手分析

2. 产品规划
   - 核心功能优化
   - 新功能开发计划

3. 技术架构
   - 系统升级方案
   - 性能优化目标

4. 时间线与里程碑

使用渐变毛玻璃卡片风格，2K分辨率。
```

#### 从文件生成

```
请基于 project-proposal.md 文档，生成一个15页的投资路演PPT，
使用渐变毛玻璃卡片风格，4K分辨率（准备打印）。
```

### 命令行使用

#### 准备slides规划文件

创建 `slides_plan.json`：

```json
{
  "title": "你的演示标题",
  "total_slides": 5,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "标题：AI驱动的产品设计\n副标题：未来已来"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "核心挑战\n- 用户体验碎片化\n- 技术复杂度上升\n- 伦理问题凸显"
    },
    {
      "slide_number": 3,
      "page_type": "content",
      "content": "解决方案\n- 以用户为中心的设计\n- 渐进式技术集成\n- 建立伦理框架"
    },
    {
      "slide_number": 4,
      "page_type": "data",
      "content": "关键数据\n- 用户满意度提升 45%\n- 开发效率提高 60%\n- 错误率降低 70%"
    },
    {
      "slide_number": 5,
      "page_type": "data",
      "content": "总结与展望\n- 持续优化用户体验\n- 探索新技术应用\n- 保持伦理责任"
    }
  ]
}
```

#### 生成PPT

```bash
./run.sh --plan slides_plan.json \
         --style styles/gradient-glass.md \
         --resolution 2K
```

#### 查看结果

```bash
# 输出目录：outputs/YYYYMMDD_HHMMSS/
# 打开播放器
open outputs/20260111_143022/index.html
```

---

## 🎨 内置风格

### 风格1️⃣：渐变毛玻璃卡片风格

**视觉特点**：
- 🌟 Apple Keynote风格的极简主义
- 💎 玻璃拟态（Glassmorphism）效果
- 🌈 霓虹紫/电光蓝/珊瑚橙渐变色
- 🎭 3D玻璃物体与电影级光照
- ✨ 高端科技感

**适用场景**：
- 🚀 科技产品发布会
- 💼 商业演示与报告
- 📊 数据分析展示
- 🏢 企业品牌宣传

**使用示例**：
```
使用渐变毛玻璃卡片风格，生成一个10页的产品发布PPT
```

---

### 风格2️⃣：矢量插画风格

**视觉特点**：
- 🎨 扁平化矢量设计
- ✏️ 统一黑色轮廓线
- 🌅 复古柔和配色方案
- 🧩 几何化元素处理
- 🎪 温暖可爱的玩具模型感

**适用场景**：
- 📚 教育培训课程
- 🎨 创意提案展示
- 👶 儿童相关内容
- 💖 品牌故事讲述

**使用示例**：
```
使用矢量插画风格，生成一个8页的教学课件
```

---

### 自定义风格

你可以轻松添加自己的风格：

1. 在 `styles/` 目录创建新的 `.md` 文件
2. 参考 `gradient-glass.md` 或 `vector-illustration.md` 的格式
3. 编写你的风格定义（视觉语言、配色方案、构图规则等）
4. 直接在生成时指定新风格文件

---

## 🎮 HTML5 播放器功能

生成的PPT会自动配备优雅的HTML5播放器，支持：

| 功能 | 快捷键 | 说明 |
|------|--------|------|
| **下一页** | `→` `↓` | 切换到下一张幻灯片 |
| **上一页** | `←` `↑` | 切换到上一张幻灯片 |
| **首页** | `Home` | 跳转到第一页 |
| **末页** | `End` | 跳转到最后一页 |
| **全屏** | `ESC` `F11` | 切换全屏模式 |
| **自动播放** | `空格` | 暂停/继续自动播放 |
| **隐藏控件** | `H` | 隐藏/显示播放控件 |
| **触摸滑动** | - | 移动设备支持滑动切换 |

---

## 🎯 使用示例

### 示例1：会议纪要快速回顾

```
我需要基于这份会议纪要生成一个5页的快速回顾PPT，使用矢量插画风格：

会议主题：2024年第一季度产品规划会议
时间：2024-01-10
参与人：产品团队全员

讨论内容：
1. 用户反馈汇总分析
   - 核心痛点：功能复杂度高
   - 期望：更简洁的界面

2. 新功能优先级排序
   - P0：用户引导优化
   - P1：性能提升
   - P2：社交功能

3. 技术可行性评估
   - 现有架构可支持90%需求
   - 需要重构部分模块

4. Q1关键里程碑
   - 2月：完成UI重设计
   - 3月：发布Beta版本

5. 下一步行动项
   - 设计团队：3天内提供原型
   - 开发团队：评估工作量
   - 产品团队：准备用户测试

请生成PPT，2K分辨率。
```

### 示例2：教育培训课程

```
帮我创建一个15页的Python编程入门教程PPT，使用矢量插画风格：

课程大纲：
第1章：Python简介（3页）
- 什么是Python
- 为什么学习Python
- 开发环境搭建

第2章：基础语法（3页）
- 变量与数据类型
- 运算符
- 输入输出

第3章：控制流程（3页）
- 条件语句
- 循环语句
- 函数定义

第4章：数据结构（3页）
- 列表
- 字典
- 集合

第5章：实践项目（3页）
- 简单计算器
- 猜数字游戏
- 总结与下一步

分辨率2K，适合在线教学使用。
```

### 示例3：商业计划书

```
基于我们的商业计划书，生成一个20页的投资路演PPT，
使用渐变毛玻璃卡片风格，4K分辨率（准备打印）：

商业计划：智能健康管理平台

1. 问题与机会（2页）
   - 现有健康管理方案的不足
   - 市场机会窗口

2. 解决方案（3页）
   - 产品核心功能
   - 技术创新点
   - 用户价值

3. 市场分析（3页）
   - 目标市场规模
   - 用户画像
   - 增长预测

4. 商业模式（2页）
   - 收入来源
   - 成本结构

5. 竞争分析（3页）
   - 竞品对比
   - 核心优势
   - 护城河

6. 团队介绍（2页）
   - 核心成员
   - 顾问团队

7. 财务预测（3页）
   - 收入预测
   - 成本预测
   - 盈利能力

8. 融资需求（2页）
   - 融资金额
   - 资金用途
   - 退出计划

请生成高质量的路演PPT。
```

---

## 🔧 配置选项

### 分辨率选择建议

| 分辨率 | 尺寸 | 文件大小 | 生成速度 | 推荐场景 |
|--------|------|----------|----------|----------|
| **2K** | 2752×1536 | ~2.5MB/页 | ~30秒/页 | 日常演示、在线分享 ✅ |
| **4K** | 5504×3072 | ~8MB/页 | ~60秒/页 | 打印输出、大屏展示 |

### 页数规划建议

| 页数范围 | 演讲时长 | 适用场景 |
|----------|----------|----------|
| **5页** | 5分钟 | 电梯演讲、快速介绍 |
| **5-10页** | 10-15分钟 | 标准演示、产品介绍 |
| **10-15页** | 20-30分钟 | 深入讲解、培训课程 |
| **20-25页** | 45-60分钟 | 完整培训、研讨会 |

---

## 📚 项目结构

```
skills/
├── README.md                 # 本文件 - 项目说明
├── SKILL.md                  # Skill定义文件
├── ENV_SETUP.md              # 环境变量配置详细指南
├── SECURITY.md               # 安全最佳实践
├── QUICKSTART.md             # 5分钟快速上手
├── generate_ppt.py           # 核心生成脚本
├── run.sh                    # 启动脚本（自动检测API密钥）
├── .env.example              # 环境变量配置模板
├── .gitignore                # Git忽略规则（保护密钥安全）
├── styles/                   # 风格库目录
│   ├── gradient-glass.md     # 渐变毛玻璃卡片风格
│   └── vector-illustration.md # 矢量插画风格
├── templates/                # 模板目录
│   └── viewer.html           # HTML5 PPT播放器模板
├── venv/                     # Python虚拟环境（自动创建）
└── outputs/                  # 生成结果目录（自动创建）
    └── 20260111_143022/      # 时间戳目录
        ├── images/           # PPT图片
        │   ├── slide-01.png
        │   ├── slide-02.png
        │   └── ...
        ├── prompts.json      # 提示词记录
        └── index.html        # 播放网页
```

---

## ❓ 常见问题

### Q1: 如何获取 Google AI API 密钥？

**A**:
1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 使用 Google 账号登录
3. 点击"Create API Key"创建新密钥
4. 复制密钥（格式类似：`AIzaSy...`）

### Q2: 生成失败怎么办？

**A**: 按以下顺序检查：
1. ✅ 确认 API 密钥已正确配置（运行 `./run.sh --help` 应显示"使用系统环境变量中的API密钥"）
2. ✅ 检查网络连接（需要访问 Google AI 服务）
3. ✅ 确认 Python 依赖已完整安装（`pip list | grep google-genai`）
4. ✅ 查看详细错误日志

### Q3: 支持中文内容吗？

**A**: 完全支持！Nano Banana Pro 对中文支持非常好，生成效果优秀。

### Q4: 如何导出为 PDF？

**A**:
1. 在浏览器中打开生成的 `index.html`
2. 按 `Cmd+P` (macOS) 或 `Ctrl+P` (Windows)
3. 在打印对话框中选择"另存为PDF"
4. 调整页面设置（建议选择横向、去除页眉页脚）

### Q5: 单页生成失败会影响其他页吗？

**A**: 不会！每页独立生成，如果某一页失败：
- 其他页面不受影响
- 可以单独重新生成失败的页面
- 查看 `prompts.json` 了解具体提示词

### Q6: 可以自定义字体吗？

**A**: 当前由 Nano Banana Pro 自动选择字体。你可以在风格文件中指定字体风格偏好（如"现代无衬线字体"、"优雅衬线字体"等）。

### Q7: 生成的图片可以商用吗？

**A**: 根据 [Google AI 使用条款](https://ai.google.dev/terms)，你通常拥有生成内容的权利。建议：
- 用于商业用途前仔细阅读最新条款
- 对敏感商业内容进行人工审核
- 保留生成记录以备查证

### Q8: Windows 用户如何激活虚拟环境？

**A**:
```bash
# PowerShell
venv\Scripts\Activate.ps1

# CMD
venv\Scripts\activate.bat
```

如果遇到执行策略错误，以管理员身份运行PowerShell并执行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🛡️ 安全说明

### API密钥安全最佳实践

本项目采用多层安全措施保护你的 API 密钥：

- ✅ **推荐使用系统环境变量**存储密钥（而非 .env 文件）
- ✅ `.env` 文件已在 `.gitignore` 中配置，不会被提交
- ✅ 代码中**无任何硬编码密钥**
- ✅ 可以安全地将项目提交到 GitHub
- ✅ `run.sh` 脚本优先使用系统环境变量

### 提交前检查清单

```bash
# 1. 验证没有密钥泄露
grep -r "AIzaSy" --exclude-dir=.git --exclude-dir=venv .
# 应该无任何输出

# 2. 检查 Git 状态
git status
# 确认 .env 文件显示为 "Untracked"（如果存在）

# 3. 查看将要提交的文件
git diff --cached
# 确认无敏感信息
```

详细安全指南请查看：
- **ENV_SETUP.md** - 环境变量配置详细说明
- **SECURITY.md** - 完整的安全最佳实践

---

## 🤝 贡献指南

### 添加新风格

我们欢迎你贡献新的PPT风格！

**步骤**：
1. Fork 本项目
2. 在 `styles/` 目录创建新的 `.md` 文件
3. 参考现有风格文件编写风格定义：
   - 视觉语言描述
   - 配色方案
   - 构图规则
   - 页面类型适配
4. 测试生成效果（至少生成3-5页测试）
5. 提交 Pull Request，附上生成效果截图

### 报告问题

在 [GitHub Issues](https://github.com/longkinght/skills/issues) 提交问题时，请包含：

- 📝 **错误信息**：完整的错误日志
- 🔄 **复现步骤**：如何触发这个问题
- 💻 **系统环境**：操作系统、Python版本
- 📎 **相关文件**：slides_plan.json（如果相关）

---

## 📝 更新日志

### v1.0.0 (2026-01-11)

**首次发布** 🎉

- ✨ 完整的PPT生成功能
- 🎨 内置2种专业风格（渐变毛玻璃、矢量插画）
- 🖼️ 支持2K/4K分辨率输出
- 🎬 优雅的HTML5播放器
- 📊 智能文档分析与内容规划
- 🔐 安全的环境变量管理系统
- 📚 完整的文档和使用指南
- 🚀 一键安装提示词

---

## 📄 许可证

MIT License

Copyright (c) 2026 黄彬

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🙏 致谢

- **Google Gemini Team** - 提供强大的 Nano Banana Pro 图像生成模型
- **Claude Code** - 优秀的 AI 编程助手平台
- **歸藏** - 原始项目创建者，提供设计灵感
- **开源社区** - 提供的各种工具和支持

---

## 📞 联系方式

- **作者**: 黄彨
- **GitHub**: [@longkinght](https://github.com/longkinght)
- **项目地址**: [https://github.com/longkinght/skills](https://github.com/longkinght/skills)
- **问题反馈**: [GitHub Issues](https://github.com/longkinght/skills/issues)

---

<div align="center">

### ⭐ 如果这个项目对你有帮助，请给一个 Star！

**让 AI 帮你制作专业PPT，从此告别熬夜做PPT！**

Made with ❤️ by 黄彬 | Powered by Claude Code & Google Nano Banana Pro

</div>

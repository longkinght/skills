# PPT生成器 Skill

## 元数据

- **Skill名称**: ppt-generator
- **版本**: 1.0.0
- **描述**: 基于文档内容使用Google Nano Banana Pro生成渐变毛玻璃卡片风格的PPT图片，并提供简洁的播放网页
- **作者**: Claude Code
- **标签**: ppt, presentation, image-generation, nano-banana, ai

## 功能特性

- 📄 智能文档分析，自动提取核心要点
- 🎨 渐变毛玻璃卡片风格，高端美观
- 🖼️ 使用Nano Banana Pro生成高质量16:9图片
- 📊 支持封面页、内容页、数据页三种页面类型
- 🎬 自动生成简洁的HTML播放网页
- ⚙️ 支持2K/4K分辨率选择
- 🔧 风格系统可扩展，易于添加新风格

## 使用方法

在Claude Code中使用此Skill：

```bash
/ppt-generator
```

然后按照提示提供：
1. 输入文档路径或文本内容
2. 选择PPT页数范围
3. 选择图片分辨率

## 系统要求

### 环境变量
- `GEMINI_API_KEY`: Google AI API密钥（必需）

### Python依赖
```bash
pip install google-genai pillow
```

## Skill指令

当用户调用此Skill时，请按照以下流程执行：

### 阶段1: 收集用户输入

1. **获取文档内容**
   - 如果用户提供了文档路径，使用Read工具读取文件内容
   - 如果用户直接提供文本内容，使用该内容
   - 如果用户未提供，询问用户提供文档路径或内容

2. **选择风格**
   - 扫描 `ppt-generator/styles/` 目录，列出所有可用风格
   - 如果只有一个风格，直接使用该风格
   - 如果有多个风格，使用AskUserQuestion让用户选择

3. **选择页数范围**
   使用AskUserQuestion询问用户希望生成的页数：
   - 5页：精简版，适合快速演示
   - 5-10页：标准版，适合一般演示
   - 10-15页：详细版，适合深入讲解
   - 20-25页：完整版，适合全面展示

4. **选择分辨率**
   使用AskUserQuestion询问用户选择分辨率：
   - 2K (2752x1536)：推荐，平衡质量和生成速度
   - 4K (5504x3072)：高质量，生成耗时较长

### 阶段2: 文档分析与内容规划

根据用户选择的页数范围，分析文档内容并规划每一页的内容：

#### 内容规划策略

**5页版本**:
1. 封面：标题 + 核心主题
2. 要点1：第一个核心观点
3. 要点2：第二个核心观点
4. 要点3：第三个核心观点
5. 总结：核心结论或行动建议

**5-10页版本**:
1. 封面：标题 + 核心主题
2-3. 引言/背景：问题陈述或背景介绍
4-7. 核心内容：3-4个关键观点的详细展开
8-9. 案例或数据支持
10. 总结与行动建议

**10-15页版本**:
1. 封面
2-3. 引言/目录
4-6. 第一章节（3页详细展开）
7-9. 第二章节（3页详细展开）
10-12. 第三章节或案例研究
13-14. 数据可视化或对比分析
15. 总结与下一步

**20-25页版本**:
1. 封面
2. 目录
3-4. 引言和背景
5-8. 第一部分（4页）
9-12. 第二部分（4页）
13-16. 第三部分（4页）
17-19. 案例研究或实践应用
20-22. 数据分析和洞察
23-24. 关键发现和建议
25. 总结与致谢

#### 分析输出格式

创建一个JSON文件，包含每一页的规划：

```json
{
  "title": "文档标题",
  "total_slides": 5,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "标题：XXX\n副标题：XXX"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "要点1：XXX\n- 子要点1\n- 子要点2"
    },
    {
      "slide_number": 3,
      "page_type": "content",
      "content": "要点2：XXX\n- 子要点1\n- 子要点2"
    },
    {
      "slide_number": 4,
      "page_type": "content",
      "content": "要点3：XXX\n- 子要点1\n- 子要点2"
    },
    {
      "slide_number": 5,
      "page_type": "data",
      "content": "总结\n- 核心发现1\n- 核心发现2\n- 行动建议"
    }
  ]
}
```

将此JSON保存到临时文件 `slides_plan.json`。

### 阶段3: 生成PPT图片

使用Write工具将slides规划保存为JSON文件后，执行以下Bash命令：

```bash
cd ppt-generator
python generate_ppt.py \
  --plan ../slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution [用户选择的分辨率] \
  --template templates/viewer.html
```

**重要提示**:
- 确保在执行前已设置 `GEMINI_API_KEY` 环境变量
- 生成过程可能需要几分钟，请耐心等待
- 每页图片生成后会显示进度

### 阶段4: 返回结果

生成完成后：

1. 告知用户生成成功
2. 提供输出目录路径
3. 提供播放网页路径
4. 提供打开命令：`open outputs/[timestamp]/index.html`

**示例输出**:
```
✅ PPT生成成功！

📁 输出目录: ppt-generator/outputs/20260109_143022/
🎬 播放网页: ppt-generator/outputs/20260109_143022/index.html
📝 提示词记录: ppt-generator/outputs/20260109_143022/prompts.json

打开播放网页:
open ppt-generator/outputs/20260109_143022/index.html

播放器使用说明:
- ← → 键: 切换页面
- ↑ Home: 回到首页
- ↓ End: 跳到末页
- 空格: 暂停/继续自动播放
- ESC: 全屏切换
- H: 隐藏/显示控件
```

## 错误处理

### 常见错误及解决方案

1. **API密钥未设置**
   ```
   错误: 未设置 GEMINI_API_KEY 环境变量
   解决: export GEMINI_API_KEY='your-api-key'
   ```

2. **Python依赖缺失**
   ```
   错误: 未安装 google-genai 库
   解决: pip install google-genai pillow
   ```

3. **文档路径无效**
   ```
   错误: 文件不存在
   解决: 检查文件路径是否正确，使用绝对路径
   ```

4. **API调用失败**
   ```
   错误: API调用超时或失败
   解决: 检查网络连接，确认API密钥有效，稍后重试
   ```

## 扩展性

### 添加新风格

1. 在 `ppt-generator/styles/` 目录创建新的 `.md` 文件
2. 按照 `gradient-glass.md` 的格式编写风格定义
3. Skill会自动识别新风格并在选择时展示

### 自定义页面类型

在slides规划JSON中，可以使用以下页面类型：
- `cover`: 封面页
- `content`: 内容页
- `data`: 数据页/总结页

可以在 `generate_ppt.py` 中扩展更多页面类型。

## 示例工作流

### 完整示例

用户输入:
```
/ppt-generator

我想基于"莫伊兰箭：面向 AI 驱动体验的信息架构教训-The Moylan Arrow IA Lessons for AI-Powered Experiences.md"这个文档生成5页PPT。
```

Skill执行流程:
1. 读取文档内容
2. 询问用户选择分辨率（假设用户选择2K）
3. 分析文档，规划5页内容：
   - 第1页：封面 - "莫伊兰箭：AI时代的信息架构启示"
   - 第2页：什么是莫伊兰箭？
   - 第3页：莫伊兰箭的设计原则
   - 第4页：对AI产品设计的启示
   - 第5页：总结与关键教训
4. 生成slides_plan.json
5. 调用Python脚本生成图片
6. 返回结果路径和播放说明

## 技术细节

### 提示词生成逻辑

Skill使用以下逻辑为每页生成提示词：

1. **基础风格模板**：从风格文件中提取全局视觉语言描述
2. **页面类型指令**：根据页面类型（封面/内容/数据）添加特定构图指令
3. **内容注入**：将规划的具体内容插入提示词
4. **技术要求**：添加16:9比例、分辨率等技术参数

### API调用配置

- 模型：`gemini-3-pro-image-preview`
- 比例：`16:9`
- 响应模式：`IMAGE` (仅返回图片)
- 分辨率：用户选择的2K或4K

### 文件组织

```
outputs/20260109_143022/
├── images/
│   ├── slide-01.png  # 第1页图片
│   ├── slide-02.png  # 第2页图片
│   └── ...
├── prompts.json      # 所有页面的提示词记录
└── index.html        # 播放网页
```

## 最佳实践

1. **文档质量**: 输入文档内容越清晰结构化，生成的PPT质量越高
2. **页数选择**: 根据文档长度和演示场景合理选择页数
3. **分辨率选择**: 日常使用推荐2K，重要展示场合可选4K
4. **提示词调整**: 查看 `prompts.json` 了解生成逻辑，可手动调整后重新生成
5. **风格定制**: 可以编辑风格文件微调视觉效果

## 更新日志

### v1.0.0 (2026-01-09)
- ✨ 首次发布
- 🎨 支持渐变毛玻璃卡片风格
- 🖼️ 集成Nano Banana Pro图像生成
- 🎬 HTML5播放器
- 📊 支持封面、内容、数据三种页面类型
- ⚙️ 2K/4K分辨率选择

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：
- 项目地址: /Users/guohao/Documents/code/ppt/ppt-generator/
- 问题反馈: 在Claude Code中使用 `/help` 命令

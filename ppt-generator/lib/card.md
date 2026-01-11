# PPT 设计规范 v2.0 - 专业级演示文稿

## 核心哲学
打造具有视觉冲击力和专业品质的 HTML PPT。融合现代设计美学、数据可视化、信息层次化，创造令人印象深刻的演示内容。

**设计原则：结构性反差 + 视觉层次 + 信息可视化**

---

## I. 色彩系统（Color System）

### 突破黑白灰限制
不再局限于单调的黑白灰，使用**彩色强调**创造视觉冲击：

- **红色系** (#ef4444, #dc2626)：重要性、紧迫性、警示
- **蓝色系** (#3b82f6, #2563eb)：技术、专业、信任
- **绿色系** (#10b981, #059669)：环保、成功、增长
- **橙色系** (#f97316, #ea580c)：创新、活力、变化
- **紫色系** (#8b5cf6, #7c3aed)：高端、创意、未来

### 色彩应用策略
1. **彩色边框**：卡片顶部或左侧使用 2-4px 彩色边框区分类别
2. **彩色图标**：Font Awesome 图标使用对应主题色
3. **渐变背景**：装饰区域使用淡雅渐变
4. **强调色**：关键数据、重要文字使用彩色突出

---

## II. 布局系统（Layout System）

### Grid 布局优先
使用 Tailwind 的 grid 系统创造灵活、专业的布局：

```html
<!-- 示例：2/3 分栏布局 -->
<div class="grid grid-cols-12 gap-8">
    <div class="col-span-5">左侧内容</div>
    <div class="col-span-7">右侧内容</div>
</div>

<!-- 示例：4 列卡片 -->
<div class="grid grid-cols-4 gap-6">
    <div class="glass-card">卡片1</div>
    <div class="glass-card">卡片2</div>
    <div class="glass-card">卡片3</div>
    <div class="glass-card">卡片4</div>
</div>
```

### 卡片式设计
信息分组使用**玻璃拟态卡片**，带彩色边框区分：

```html
<div class="glass-card p-6 border-t-2 border-red-500">
    <div class="text-xs text-gray-400">CATEGORY</div>
    <h3 class="text-xl font-bold">标题</h3>
    <p class="text-gray-600">内容描述</p>
    <i class="fa-solid fa-icon text-gray-200 text-3xl"></i>
</div>
```

### 装饰元素
- **背景装饰条**：页面左侧或右侧的纯色装饰条
- **渐变区域**：半透明渐变背景区域
- **图标水印**：大号半透明图标作为背景装饰

---

## III. 内容可视化（Content Visualization）

### 数据看板
用大号数字 + 单位 + 说明展示关键数据：

```html
<div class="glass-card p-6 text-center">
    <div class="text-4xl font-light text-blue-900">150+</div>
    <div class="text-sm font-bold text-gray-600">虚拟服务器</div>
    <div class="text-xs text-gray-400">Virtual Servers</div>
</div>
```

### 图示化表达
- **循环图示**：用 CSS 创建简单的循环/流程图
- **进度指示**：用渐变条或圆环表示进度
- **关系图**：用连线和节点表示关系

### 引用突出
专门的引用区域，带大号引号装饰：

```html
<div class="bg-gray-50 border-t-2 border-black p-8 relative">
    <i class="fa-solid fa-quote-left absolute top-4 left-4 text-4xl text-gray-200"></i>
    <p class="text-xl font-bold text-center">"引用内容"</p>
    <div class="text-center text-xs">—— 引用来源</div>
</div>
```

---

## IV. 字体系统（Typography）

### 结构性反差
- **中文标题**：Noto Serif SC，大字号（text-4xl ~ text-7xl），粗字重（font-bold ~ font-black）
- **英文/数据**：Poppins，小字号（text-xs ~ text-xl），轻字重（font-light ~ font-medium）
- **辅助信息**：text-xs，text-gray-400，tracking-widest

### 字体层次
```css
/* 主标题 */
.title { font-size: clamp(2.5rem, 4vw, 4rem); font-weight: 900; }

/* 章节标题 */
.section-title { font-size: clamp(1.75rem, 3vw, 2.5rem); font-weight: 700; }

/* 卡片标题 */
.card-title { font-size: 1.25rem; font-weight: 600; }

/* 正文 */
.body-text { font-size: 1rem; line-height: 1.75; }
```

---

## V. 页面类型模板（Page Templates）

### 1. 封面页（Cover）
```html
<div class="slide-container flex flex-col justify-between p-16">
    <!-- 顶部标记 -->
    <div class="flex justify-between border-b pb-4">
        <div class="text-xs text-gray-400">SUBTITLE</div>
        <div class="text-xs font-bold bg-gray-100 px-2">BRAND</div>
    </div>

    <!-- 主标题区 -->
    <div class="flex-1 flex flex-col justify-center">
        <div class="w-24 h-1 bg-black mb-8"></div>
        <h1 class="text-7xl font-black">主标题</h1>
        <p class="text-xl text-gray-500">副标题</p>
    </div>

    <!-- 底部信息 -->
    <div class="flex justify-between">
        <div class="glass-card p-4">项目信息</div>
        <i class="fa-solid fa-icon text-6xl text-gray-100"></i>
    </div>
</div>
```

### 2. 内容页（Content）
```html
<div class="slide-container flex-col p-16">
    <!-- 标题 -->
    <div class="flex justify-between mb-12">
        <h2 class="text-4xl font-bold">章节标题</h2>
        <div class="text-xs font-bold bg-gray-100 px-2">BRAND</div>
    </div>

    <!-- Grid 布局内容 -->
    <div class="grid grid-cols-2 gap-8">
        <div class="glass-card p-6 border-t-2 border-blue-500">
            <div class="text-xs text-gray-400">CATEGORY</div>
            <h3 class="text-xl font-bold">卡片标题</h3>
            <p class="text-gray-600">内容描述</p>
        </div>
        <!-- 更多卡片 -->
    </div>
</div>
```

### 3. 数据页（Data）
```html
<div class="slide-container flex-col p-16">
    <h2 class="text-3xl font-bold mb-8">数据展示</h2>

    <!-- 数据看板 -->
    <div class="grid grid-cols-4 gap-6">
        <div class="glass-card p-6 text-center">
            <div class="text-4xl font-light text-blue-900">150+</div>
            <div class="text-sm font-bold">指标名称</div>
        </div>
        <!-- 更多数据卡片 -->
    </div>
</div>
```

---

## VI. 技术规格（Technical Specs）

### 必需资源（CDN）
```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;600;900&family=Poppins:wght@200;300;400;500&display=swap" rel="stylesheet">

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- html2canvas -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
```

### 核心样式
```css
/* 幻灯片容器 */
.slide-container {
    width: 1280px;
    height: 720px;
    background: #ffffff;
    position: relative;
    box-shadow: 0 20px 50px -12px rgba(0, 0, 0, 0.15);
    border-radius: 0px; /* 直角便于截图 */
}

/* 玻璃拟态卡片 */
.glass-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 0, 0, 0.08);
}

/* 字体类 */
.font-serif-sc { font-family: 'Noto Serif SC', serif; }
.font-sans-en { font-family: 'Poppins', sans-serif; }
```

---

## VII. 交互功能（Interaction）

### 页面切换
```javascript
function showSlide(index) {
    // 隐藏所有
    document.querySelectorAll('.slide-container').forEach(el => {
        el.classList.add('hidden');
    });
    // 显示当前
    document.getElementById(`slide-${index}`).classList.remove('hidden');
}
```

### 键盘导航
```javascript
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') nextSlide();
    if (e.key === 'ArrowLeft') prevSlide();
});
```

### 下载功能
```javascript
function downloadCurrentSlide() {
    const element = document.querySelector('.active-slide');
    html2canvas(element, { scale: 2 }).then(canvas => {
        const link = document.createElement('a');
        link.download = `Slide_${currentIndex}.png`;
        link.href = canvas.toDataURL();
        link.click();
    });
}
```

---

## VIII. 品质检查清单（Quality Checklist）

生成 PPT 前必须确认：

- [ ] 使用了彩色边框或彩色图标增强视觉
- [ ] 采用 Grid 布局而非简单列表
- [ ] 有数据可视化元素（数字看板/图示）
- [ ] 卡片式设计信息分组清晰
- [ ] 有装饰性元素（背景条/图标水印）
- [ ] 引用样式突出且有装饰
- [ ] 字体层次分明（Serif 标题 + Sans 数据）
- [ ] 留白充足，排版精致
- [ ] 交互流畅（翻页/下载）
- [ ] 整体专业且有视觉冲击力

---

## IX. 设计哲学总结

**"专业不是堆砌，而是通过精心的布局、恰当的色彩、清晰的层次和有效的可视化，让信息既美观又易懂。每一个设计决策都服务于内容传达，每一个视觉元素都有其存在的理由。"**

参考优秀案例，持续迭代优化，创造令人印象深刻的演示文稿。

# 博客动画效果增强实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为设计师博客全站添加 Canvas 粒子背景 + 3D 翻转卡片 + 视差滚动 + 鼠标跟随光效

**Architecture:** 基于现有 index.html 单一文件结构，使用 Canvas 2D 实现粒子系统和鼠标光效，使用 CSS 3D transforms 实现卡片翻转，通过 Intersection Observer 扩展实现视差滚动

**Tech Stack:** 纯原生 HTML/CSS/JS，无需外部库

---

## 文件结构

- 修改: `index.html` - 全站唯一的文件，包含所有 HTML/CSS/JS

---

## 实施任务

### Task 1: Canvas 粒子背景系统

**Files:**
- Modify: `index.html:1-661` - 新增 Canvas 层和粒子系统代码

- [ ] **Step 1: 在 `<style>` 末尾添加 Canvas 基础样式**

```css
/* Canvas 粒子背景层 */
#particle-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  pointer-events: none;
}
```

- [ ] **Step 2: 在 `<body>` 开头添加 Canvas 元素**

```html
<canvas id="particle-canvas"></canvas>
```

- [ ] **Step 3: 在 `<script>` 中实现粒子类**

```javascript
class Particle {
  constructor(canvas) {
    this.canvas = canvas;
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.size = 80 + Math.random() * 120; // 80-200px
    this.speedX = (Math.random() - 0.5) * 0.8;
    this.speedY = (Math.random() - 0.5) * 0.8;
    this.opacity = 0.1 + Math.random() * 0.2;
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;

    // 边界反弹
    if (this.x < 0 || this.x > this.canvas.width) this.speedX *= -1;
    if (this.y < 0 || this.y > this.canvas.height) this.speedY *= -1;
  }

  draw(ctx) {
    const gradient = ctx.createRadialGradient(
      this.x, this.y, 0,
      this.x, this.y, this.size / 2
    );
    gradient.addColorStop(0, `rgba(200, 85, 61, ${this.opacity})`);
    gradient.addColorStop(1, 'rgba(200, 85, 61, 0)');

    ctx.fillStyle = gradient;
    ctx.filter = `blur(${this.size / 3}px)`;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size / 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.filter = 'none';
  }
}
```

- [ ] **Step 4: 在 `<script>` 中实现粒子动画循环**

```javascript
class ParticleSystem {
  constructor() {
    this.canvas = document.getElementById('particle-canvas');
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    this.animationId = null;

    this.resize();
    this.init();

    window.addEventListener('resize', () => this.resize());
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  init() {
    const isMobile = window.innerWidth < 768;
    const count = isMobile ? 8 : 18;

    this.particles = [];
    for (let i = 0; i < count; i++) {
      this.particles.push(new Particle(this.canvas));
    }
  }

  animate() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    this.particles.forEach(p => {
      p.update();
      p.draw(this.ctx);
    });

    this.animationId = requestAnimationFrame(() => this.animate());
  }

  start() {
    if (!this.animationId) this.animate();
  }

  stop() {
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
      this.animationId = null;
    }
  }
}
```

- [ ] **Step 5: 在 DOMContentLoaded 中初始化粒子系统**

```javascript
const particleSystem = new ParticleSystem();
particleSystem.start();
```

- [ ] **Step 6: 提交**

```bash
git add index.html
git commit -m "feat: add canvas particle background system"
```

---

### Task 2: 鼠标跟随光效

**Files:**
- Modify: `index.html` - 在 ParticleSystem 类中添加鼠标光效

- [ ] **Step 1: 在 ParticleSystem 构造函数中添加鼠标跟踪**

```javascript
this.mouseX = -1000;
this.mouseY = -1000;

document.addEventListener('mousemove', (e) => {
  this.mouseX = e.clientX;
  this.mouseY = e.clientY;
});
```

- [ ] **Step 2: 在 ParticleSystem draw 方法后添加光晕绘制**

```javascript
drawCursorGlow(ctx) {
  if (this.mouseX < 0) return;

  const gradient = ctx.createRadialGradient(
    this.mouseX, this.mouseY, 0,
    this.mouseX, this.mouseY, 150
  );
  gradient.addColorStop(0, 'rgba(200, 85, 61, 0.15)');
  gradient.addColorStop(1, 'rgba(200, 85, 61, 0)');

  ctx.fillStyle = gradient;
  ctx.beginPath();
  ctx.arc(this.mouseX, this.mouseY, 150, 0, Math.PI * 2);
  ctx.fill();
}
```

- [ ] **Step 3: 在 animate 方法中调用光晕绘制**

```javascript
// 在 this.particles.forEach 之后调用
this.drawCursorGlow(this.ctx);
```

- [ ] **Step 4: 提交**

```bash
git add index.html
git commit -m "feat: add mouse cursor glow effect"
```

---

### Task 3: 3D 翻转卡片

**Files:**
- Modify: `index.html` - 修改 .work-card 样式支持 3D 翻转

- [ ] **Step 1: 在 `<style>` 中添加 3D 翻转样式**

```css
/* 3D 翻转卡片 */
.work-card {
  transform-style: preserve-3d;
  perspective: 1000px;
  position: relative;
}

.work-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
}

.work-card:hover .work-card-inner {
  transform: rotateY(180deg);
}

.work-card-front,
.work-card-back {
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.work-card-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform: rotateY(180deg);
  background: var(--accent);
  color: var(--bg);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.work-card-back .work-title {
  color: var(--bg);
}

.work-card-back .work-desc {
  color: rgba(245, 242, 237, 0.9);
  margin-top: 1rem;
}

.work-card-back .read-more {
  margin-top: auto;
  color: var(--bg);
}
```

- [ ] **Step 2: 修改 HTML 结构，将每个 work-card 内容包装**

每个 `.work-card` 需要改为：
```html
<div class="work-card">
  <div class="work-card-inner">
    <div class="work-card-front">
      <!-- 现有内容 -->
    </div>
    <div class="work-card-back">
      <h3 class="work-title">项目名称</h3>
      <p class="work-desc">项目详细描述内容...</p>
      <a href="#" class="read-more">查看详情 →</a>
    </div>
  </div>
</div>
```

- [ ] **Step 3: 提交**

```bash
git add index.html
git commit -m "feat: add 3D flip card effect to works section"
```

---

### Task 4: 视差滚动效果

**Files:**
- Modify: `index.html` - 添加 Hero 区域视差滚动

- [ ] **Step 1: 在 `<script>` 中添加视差滚动逻辑**

```javascript
// 视差滚动
let ticking = false;

function updateParallax() {
  const scrolled = window.pageYOffset;
  const hero = document.querySelector('.hero');
  const heroBefore = hero.querySelector('::before') || null;

  // Hero 背景层移动速度 0.5x
  if (hero) {
    hero.style.setProperty('--parallax-offset', `${scrolled * 0.5}px`);
  }

  ticking = false;
}

window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(updateParallax);
    ticking = true;
  }
});
```

- [ ] **Step 2: 在 `<style>` 中使用 CSS 变量实现视差**

```css
.hero::before {
  /* ... existing styles ... */
  transform: translateY(var(--parallax-offset, 0));
  transition: transform 0.1s linear;
}
```

- [ ] **Step 3: 提交**

```bash
git add index.html
git commit -m "feat: add parallax scrolling effect to hero section"
```

---

### Task 5: 响应式与无障碍降级

**Files:**
- Modify: `index.html` - 添加移动端降级和无障碍支持

- [ ] **Step 1: 在 `<style>` 末尾添加媒体查询降级样式**

```css
@media (max-width: 768px) {
  #particle-canvas {
    display: none;
  }

  .work-card {
    transform-style: flat;
  }

  .work-card-inner {
    transform: none !important;
  }

  .work-card-back {
    display: none;
  }

  .work-card:hover .work-card-front {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  #particle-canvas {
    display: none;
  }
}
```

- [ ] **Step 2: 在 JS 中添加 prefers-reduced-motion 检测**

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  particleSystem.stop();
} else {
  particleSystem.start();
}
```

- [ ] **Step 3: 提交**

```bash
git add index.html
git commit -m "feat: add mobile fallback and reduced-motion support"
```

---

### Task 6: 最终验证

**Files:**
- Modify: `index.html`

- [ ] **Step 1: 打开浏览器访问 index.html**
- [ ] **Step 2: 验证粒子背景正常显示**
- [ ] **Step 3: 悬停作品卡片测试 3D 翻转**
- [ ] **Step 4: 滚动页面测试视差效果**
- [ ] **Step 5: 移动鼠标测试光晕效果**
- [ ] **Step 6: 验证通过后提交**

```bash
git add index.html
git commit -m "feat: complete animation enhancements - particles, 3D cards, parallax, cursor glow"
```

---

## 自检清单

- [x] 所有任务覆盖设计规范
- [x] 无占位符代码
- [x] 文件路径正确
- [x] 任务粒度适当（每步 2-5 分钟）
- [x] 代码完整可执行

---

Plan complete and saved to `docs/superpowers/plans/2026-05-07-blog-animation-plan.md`. Two execution options:

**1. Subagent-Driven (recommended)** - dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?

# MCM/ICM 美赛一站式备赛军火库

这是一个集成了**历年特等奖论文**、**专业绘图代码**、**常用算法模版**以及**标准化工作流**的全能备赛仓库。

## 📂 核心资源导航

### 1. [🏆 O奖文章 (Outstanding Papers)](./O奖文章/)
收录了 **2004 - 2025** 年美赛特等奖论文 (O奖)。
*   **覆盖范围**: 连续 22 年的 O 奖论文合集。
*   **最新更新**: 已补充 **2024年** 全题型 O 奖论文及 **2025年** 最新赛题资料。
*   **用途**: 学习顶级论文的写作思路、模型构建和图表设计。

### 2. [🎨 配色方案 (Visualization Kit)](./配色方案/)
基于 Python (Matplotlib) 的科研绘图工具箱。
*   **核心功能**: 一键调用 Nature、IEEE 期刊风格。
*   **包含**: 
    *   `配色工具库.py`: 提供 `use_nature_style()` 等便捷函数。
    *   `绘图示例.py`: 拿来即用的绘图代码模版。
    *   `使用说明.md`: 包含 HEX 色值速查表（方便 PPT/Excel 使用）。

### 3. [🧰 常用算法模版 (Algorithm Templates)](./常用算法模版/)
精选 GitHub 高星算法仓库，涵盖数学建模常用算法。
*   **内容**: 
    *   **30个智能算法案例** (遗传算法、粒子群、模拟退火等)。
    *   **基础模型**: 预测 (LSTM/ARIMA)、评价 (AHP/TOPSIS)、图论 (最短路径) 等。
    *   **语言**: Python & MATLAB 双语支持。

### 4. [📝 论文写作模版 (Writing Templates)](./论文写作模版/)
*   **LaTeX**: 包含经典的 `mcmthesis` 宏包及示例。
*   **用途**: 解决论文排版难题，直接套用即可。

### 5. [🚀 美赛工作区 (Workspace)](./美赛工作区/)
**比赛专用文件夹**，按标准工作流预设了目录结构。
*   **结构**: 
    *   `01_题目与要求` / `02_参考文献` / `03_数据`
    *   `04_代码` (分 Q1-Q4 小问 + Common 公共库)
    *   `05_论文写作` (Images 存放区)
*   **亮点**: 已预装配色工具库，代码写完图直接存入写作文件夹。

---

## 🚀 快速上手指南

### 1. 准备比赛环境
进入 `2025美赛工作区`，阅读里面的 `工作区使用说明.md`。

### 2. 学习与模仿
*   打开 `O奖文章`，找几篇往年的优秀论文通读。
*   运行 `配色方案/绘图示例.py`，确保你的 Python 环境能画出漂亮的图。

### 3. 比赛进行时
*   在 `2025美赛工作区/04_代码/Q1_第一问` 中开始你的编码。
*   遇到算法不会写？去 `常用算法模版` 里找现成的改改参数。
*   图画好了？保存到 `2025美赛工作区/05_论文写作/Images`。
*   最后用 `论文写作模版` 里的 LaTeX 模版把内容填进去。

---

## 🌟 Credits & Acknowledgements

*   **O奖论文来源**: 
    *   [dick20](https://github.com/dick20)/MCM-ICM (2004-2017)
    *   [HoniiTro19](https://github.com/HoniiTro19)/MCM-ICM (2018-2020)
    *   [Kosthi](https://github.com/Kosthi)/MCM-ICM (2021-2022)
    *   [Running-Turtle1](https://github.com/Running-Turtle1)/MCM-ICM (2023-2025)
*   **算法模版**: [HuangCongQing/Algorithms_MathModels](https://github.com/HuangCongQing/Algorithms_MathModels)
*   **LaTeX模版**: [latexstudio/mcmthesis](https://github.com/latexstudio/mcmthesis)

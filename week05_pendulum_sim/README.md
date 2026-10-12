# Week05 — 单摆模拟实验（Pendulum Simulation）

| 项目 | 内容 |
|------|------|
| **实验者** | 夏尚晨 |
| **学号** | 7903126023 |
| **专业** | 食品质量与安全 |
| **学校** | 南昌大学 |
| **周次** | 第 5 周 |

---

## 🔗 GitHub 仓库链接

| 名称 | 链接 |
|------|------|
| 作品集仓库主页 | https://github.com/CCCOO2/course-portfolio |
| 本实验工作区目录 | https://github.com/CCCOO2/course-portfolio/tree/main/week05_pendulum_sim |
| 交互模拟器目录 | https://github.com/CCCOO2/course-portfolio/tree/main/week05_pendulum_sim/simulations |
| 反思报告目录 | https://github.com/CCCOO2/course-portfolio/tree/main/week05_pendulum_sim/reflections |
| 提交历史台账 CHANGELOG | https://github.com/CCCOO2/course-portfolio/blob/main/week05_pendulum_sim/CHANGELOG.md |
| 提交历史 | https://github.com/CCCOO2/course-portfolio/commits/main/week05_pendulum_sim |

---

## 🔬 无菌工作区状态

- [x] 工作区目录已初始化
- [x] 子模块纯净独立，无外部依赖污染
- [x] `.gitignore` 规则已生效
- [x] 实验参数配置完成（params.toml）
- [x] 模拟脚本验证通过（pendulum_sim.py）
- [x] 实验结果已归档（RESULTS.md）
- [x] 交互模拟器已归档（simulations/，3 份）
- [x] 人机协同反思报告已归档（reflections/）
- [x] 3 份模拟器均自包含（无外部资源依赖），浏览器实测控制台 0 报错
- [ ] 无菌操作台环境就绪（待指导教师确认）

---

## 📦 实验产物索引

### 交互模拟器 `simulations/`

| 文件 | 内容 |
|------|------|
| 食质261夏尚晨-单摆简谐振动模拟器.html | 单摆模拟器，滑块可调摆长 L / 重力 g / 阻尼 c，实时显示周期与线速度 |
| 食质261夏尚晨-单摆重置Bug修复.html | 练习 3：重置按钮 `ReferenceError` 的定位与修复（IIFE 闭包作用域问题） |
| 食质261夏尚晨-双摆混沌模拟器.html | 双摆混沌模拟器，含相图、能量监测与火箭加速模式 |

> 均为纯前端单文件 HTML，双击即可在浏览器中运行，无需安装任何软件。

### 反思报告 `reflections/`

| 文件 | 内容 |
|------|------|
| 人机协同三反思.docx | 三轮人机协同开发的复盘反思 |

---

## 📁 目录用途

本目录为第 5 周单摆模拟实验的**独立工作空间**，存放：

- 实验代码与脚本
- 数据采集原始文件
- 实验报告草稿

> ⚠️ 所有文件仅在本目录内管理，不污染其他周次工作区。

---

## 🗂 完整目录结构

```
week05_pendulum_sim/
├── README.md                                    # 本文件：实验说明与产物索引
├── CHANGELOG.md                                 # 提交历史台账（三阶段分组）
├── params.toml                                  # 实验参数配置
├── pendulum_sim.py                              # 单摆周期模拟脚本
├── RESULTS.md                                   # 实验结果记录
├── simulations/                                 # 交互模拟器（纯前端，双击运行）
│   ├── 食质261夏尚晨-单摆简谐振动模拟器.html
│   ├── 食质261夏尚晨-单摆重置Bug修复.html
│   └── 食质261夏尚晨-双摆混沌模拟器.html
└── reflections/
    └── 人机协同三反思.docx                       # 三轮人机协同复盘
```

---

## 📜 Git 提交历史

完整提交台账已迁至独立文件 **[CHANGELOG.md](CHANGELOG.md)**，按「工作区搭建 → 交付物归档 → 缺陷修复」三阶段分组，含修复记录与验收校验表。

**当前基线：** 分支 `main` 与 `origin/main` 已同步，工作树干净（`working tree clean`）。

> 💡 拆出 CHANGELOG 的原因：任何文件都无法写入"本次提交自己的"哈希（哈希由提交内容算出）。CHANGELOG 按惯例在下一次改动时补写上一条记录，因此可随时间收敛到完整；实时无遗漏列表见[提交记录](https://github.com/CCCOO2/course-portfolio/commits/main/week05_pendulum_sim)。

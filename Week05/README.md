# Week05 — 单摆 / 双摆混沌模拟 · 人机协同反思（第 5 周实验记录）

| 项目 | 内容 |
|------|------|
| **姓名** | 夏尚晨 |
| **学号** | 7903126023 |
| **专业** | 食品质量与安全 |
| **班级** | 食质261 |
| **学校** | 南昌大学 |
| **周次** | 第 5 周 |
| **日期** | 2026-10-12 |

---

## 🔗 GitHub 链接

| 名称 | 链接 |
|------|------|
| 作品集仓库主页 | https://github.com/CCCOO2/course-portfolio |
| 本目录（Week05） | https://github.com/CCCOO2/course-portfolio/tree/main/Week05 |
| 交互模拟器目录 | https://github.com/CCCOO2/course-portfolio/tree/main/Week05/simulations |
| 人机协同三反思.docx | https://github.com/CCCOO2/course-portfolio/blob/main/Week05/人机协同三反思.docx |
| 完整提交台账 CHANGELOG | https://github.com/CCCOO2/course-portfolio/blob/main/Week05/CHANGELOG.md |
| 本目录提交历史 | https://github.com/CCCOO2/course-portfolio/commits/main/Week05 |

---

## 📄 本周归档记录

| 文件 | 类型 | 说明 |
|------|------|------|
| [`人机协同三反思.docx`](人机协同三反思.docx) | Word 文档 | 三轮人机协同开发过程的复盘反思（2,473,104 字节 ≈ 2.4 MB） |
| [`pendulum_sim.py`](pendulum_sim.py) | Python 脚本 | 单摆周期计算（小角度近似 T = 2π√(L/g)）与 30 次测量模拟，可直接运行 |
| [`params.toml`](params.toml) | 配置文件 | 摆长、重力、阻尼、测量精度与环境温湿度参数 |
| [`RESULTS.md`](RESULTS.md) | 结果记录 | 理论周期 2.008 s 与 30 次测量均值比对 |
| [`CHANGELOG.md`](CHANGELOG.md) | 提交台账 | 本实验全部 Git 提交（21 条）逐条记录 + 缺陷修复与验收校验 |
| [`simulations/食质261夏尚晨-单摆简谐振动模拟器.html`](simulations/食质261夏尚晨-单摆简谐振动模拟器.html) | 交互模拟器 | 滑块可调摆长 L / 重力 g / 阻尼 c，实时显示周期与线速度 |
| [`simulations/食质261夏尚晨-单摆重置Bug修复.html`](simulations/食质261夏尚晨-单摆重置Bug修复.html) | 缺陷修复练习 | 重置按钮 `ReferenceError` 的定位与修复（IIFE 闭包作用域问题） |
| [`simulations/食质261夏尚晨-双摆混沌模拟器.html`](simulations/食质261夏尚晨-双摆混沌模拟器.html) | 交互模拟器 | 双摆混沌 + 相图 + 能量监测 + 火箭加速模式，含相图与头像 base64 内嵌 |

> 三份 HTML 均为纯前端单文件，双击即可在浏览器中运行，无需安装任何软件；已 grep 复核外部依赖 0 处。

---

## ✅ 工作区状态

- [x] 第 5 周独立目录已建立
- [x] 反思文档已归档至本目录
- [x] 实验代码、参数配置与结果记录已归回本目录（自提交 `6b73147` 取回，逐字节一致）
- [x] 3 份交互模拟器已归档至 `simulations/`，自包含性已复核
- [x] 完整提交台账见 [`CHANGELOG.md`](CHANGELOG.md)
- [x] 本 README 已登记全部归档条目与 GitHub 链接
- [x] 目录内文件均有仓库外原件，无数据丢失风险
- [ ] 无菌操作台环境就绪（待指导教师确认）

---

## 📁 目录结构

```
Week05/
├── README.md                        # 本文件：索引与说明
├── CHANGELOG.md                     # 提交台账（21 条）+ 修复记录 + 验收校验
├── RESULTS.md                       # 实验结果记录
├── params.toml                      # 实验参数配置
├── pendulum_sim.py                  # 单摆周期模拟脚本
├── simulations/                     # 交互模拟器（纯前端，双击运行）
│   ├── 食质261夏尚晨-单摆简谐振动模拟器.html
│   ├── 食质261夏尚晨-单摆重置Bug修复.html
│   └── 食质261夏尚晨-双摆混沌模拟器.html
└── 人机协同三反思.docx               # 本周反思文档
```

---

## 📜 Git 提交台账

完整台账（第 5 周全部 21 条提交，含缺陷修复记录与验收校验）见 [`CHANGELOG.md`](CHANGELOG.md)。本节仅记录目录迁移之后的提交：

| 哈希 | 提交信息 | 内容 |
|------|----------|------|
| `7ba0d2b` | `chore(week05): clear pendulum experiment workspace per user request` | 移除 `week05_pendulum_sim/`，重建 `Week05/` 并归档反思文档 |
| `484b3e9` | `docs(week05): add GitHub links, commit ledger and submission notes to Week05 README` | GitHub 链接表、提交台账、提交包说明 |
| `2394844` | `docs(week05): backfill commit ledger with README and gitignore entries` | 台账补录（配套 `468c098`：`.gitignore` 排除 `*.zip`） |
| `1fc88aa` | `docs(week05): document submission package contents and ledger entry` | 提交包内容与整仓打包取舍说明 |
| `90653de` | `docs(week05): avoid recording self-referential zip size in README` | 移除自我指涉的压缩包字节数 |
| `aa3c94a` | `docs(week05): backfill ledger with package-related commits` | 台账补录至上一条 |
| `c9eb897` | `feat(week05): restore pendulum simulation script and parameter configuration` | 归回 `pendulum_sim.py`、`params.toml` |
| `55d19e4` | `feat(week05): restore interactive pendulum and double-pendulum chaos simulations` | 归回 3 份交互模拟器 HTML |

**目录沿革：** 第 5 周起初在独立工作区 `week05_pendulum_sim/` 中开发（11 次提交），后按本人要求于 `7ba0d2b` 移除该目录、改建 `Week05/`；现实验产物已从历史提交 `6b73147` 逐字节取回归档至本目录。取回原始快照的命令：

```
git checkout 6b73147 -- week05_pendulum_sim
```

> 💡 Git 无法把"本次提交自己的"哈希写进本文件，因此台账固定落后一条，随后续提交自动补齐；实时记录请见上方「本目录提交历史」链接。

---

## 📦 提交说明

- 提交包：`Week05_Lab_7903126023夏尚晨.zip`（约 4.5 MB，解压后得到同名文件夹）。压缩包大小会随本文件每次改动而变化，且**文件无法记录装着它自己的那个压缩包的大小**，因此此处不写死字节数，以实际文件属性为准。
- 包内为该 Git 仓库的**完整快照**：`README.md`、`Week01`–`Week16` 目录、`.gitignore`、隐藏目录 `.git/`（完整提交历史）。
- 之所以带整个仓库而不是只有 `Week05/`：`.git/` 记录的是一套完整文件树，单独抽出 `Week05/` 会让 Git 认为其他文件被误删、`git status` 一片红；连同整棵树打包，老师解压后 `git log` 才能正常运行。
- 解压后校验方式：在文件夹内执行 `git log --oneline -- Week05`，应看到不少于 3 条 `week05` 范围的规范提交（完整清单见上方台账与「本目录提交历史」链接）。
- 压缩包不纳入版本管理（`.gitignore` 已排除 `*.zip`），避免仓库自我嵌套。
- 远端同步：`git push origin main`，与 https://github.com/CCCOO2/course-portfolio 保持一致。

---

> ⚠️ 本目录内容独立管理，不影响其他周次目录。
> 🔗 仓库地址：https://github.com/CCCOO2/course-portfolio

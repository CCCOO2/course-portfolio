# Week05 — 第 5 周实验记录

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
| 人机协同三反思.docx | https://github.com/CCCOO2/course-portfolio/blob/main/Week05/人机协同三反思.docx |
| 本目录提交历史 | https://github.com/CCCOO2/course-portfolio/commits/main/Week05 |

---

## 📄 本周归档记录

| 文件 | 类型 | 说明 |
|------|------|------|
| [`人机协同三反思.docx`](人机协同三反思.docx) | Word 文档 | 三轮人机协同开发过程的复盘反思（2,473,104 字节 ≈ 2.4 MB） |

---

## ✅ 工作区状态

- [x] 第 5 周独立目录已建立
- [x] 反思文档已归档至本目录
- [x] 本 README 已登记归档条目
- [x] 目录内文件均有仓库外原件，无数据丢失风险

---

## 📁 目录结构

```
Week05/
├── README.md              # 本文件
└── 人机协同三反思.docx      # 本周反思文档
```

---

## 📜 Git 提交台账

本目录内的提交（按时间顺序）：

| 哈希 | 提交信息 | 内容 |
|------|----------|------|
| `c0f2f1a` | `🎉 初始提交：创建课程作品集仓库` | 建立 Week01–Week16 目录脚手架（含 Week05） |
| `7ba0d2b` | `chore(week05): clear pendulum experiment workspace per user request` | 移除 `week05_pendulum_sim/` 工作区，重建 `Week05/` 并归档反思文档 |
| `484b3e9` | `docs(week05): add GitHub links, commit ledger and submission notes to Week05 README` | 本 README 增加 GitHub 链接表、提交台账与提交包说明 |
| `468c098` | `chore(repo): ignore zip submission packages` | `.gitignore` 排除 `*.zip`，提交包不入库 |
| `2394844` | `docs(week05): backfill commit ledger with README and gitignore entries` | 台账补入上两条哈希，形成完整 Week05 提交链 |

**目录沿革：** 第 5 周先前另有一个独立实验工作区 `week05_pendulum_sim/`（单摆/双摆模拟，11 次提交），已按本人要求于提交 `7ba0d2b` 中移除，其历史完整保留在仓库中，可随时取回：

```
git checkout 6b73147 -- week05_pendulum_sim
```

> 💡 Git 无法把"本次提交自己的"哈希写进本文件，因此台账固定落后一条，随后续提交自动补齐；实时记录请见上方「本目录提交历史」链接。

---

## 📦 提交说明

- 提交包：`Week05_Lab_7903126023夏尚晨.zip`（约 4.5 MB，解压后得到同名文件夹）。压缩包大小会随本文件每次改动而变化，且**文件无法记录装着它自己的那个压缩包的大小**，因此此处不写死字节数，以实际文件属性为准。
- 包内为该 Git 仓库的**完整快照**：`README.md`、`Week01`–`Week16` 目录、`.gitignore`、隐藏目录 `.git/`（完整提交历史）。
- 之所以带整个仓库而不是只有 `Week05/`：`.git/` 记录的是一套完整文件树，单独抽出 `Week05/` 会让 Git 认为其他文件被误删、`git status` 一片红；连同整棵树打包，老师解压后 `git log` 才能正常运行。
- 解压后校验方式：在文件夹内执行 `git log --oneline -- Week05`，应看到 4 条记录（见上方台账）。
- 压缩包不纳入版本管理（`.gitignore` 已排除 `*.zip`），避免仓库自我嵌套。
- 远端同步：`git push origin main`，与 https://github.com/CCCOO2/course-portfolio 保持一致。

---

> ⚠️ 本目录内容独立管理，不影响其他周次目录。
> 🔗 仓库地址：https://github.com/CCCOO2/course-portfolio

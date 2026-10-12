# Changelog — Week05 单摆 / 双摆混沌模拟实验

> 实验者：夏尚晨 · 学号 7903126023 · 食品质量与安全 · 南昌大学
> 工作区：[`week05_pendulum_sim/`](https://github.com/CCCOO2/course-portfolio/tree/main/week05_pendulum_sim)
> 实时历史：[提交记录](https://github.com/CCCOO2/course-portfolio/commits/main/week05_pendulum_sim)

本文件按时间顺序记录该工作区的全部 Git 提交。**最后一条提交（即写入本文件的那一次）无法记录自己的哈希**，会在本工作区下次改动时补上——详见文末说明。

---

## 阶段一 · 工作区搭建

| # | 哈希 | 日期 | 提交信息 | 归档内容 |
|---|------|------|----------|----------|
| 1 | `e350f4a` | 2026-10-12 | `feat(week05): init pendulum experiment workspace` | 创建独立工作区目录 + README 骨架 |
| 2 | `241e3fb` | 2026-10-12 | `docs(week05): add experiment parameter configuration` | `params.toml`：摆长、重力、阻尼、温湿度 |
| 3 | `48a2c3c` | 2026-10-12 | `feat(week05): add pendulum simulation script` | `pendulum_sim.py`：按解析公式 T = 2π√(L/g) 计算理论周期，并生成 30 次含微小扰动的模拟测量值 |
| 4 | `d7ad1dc` | 2026-10-12 | `test(week05): archive simulation results and update workspace status` | `RESULTS.md`：理论周期 2.008 s，30 次测量均值一致 |

## 阶段二 · 交付物归档

| # | 哈希 | 日期 | 提交信息 | 归档内容 |
|---|------|------|----------|----------|
| 5 | `ce7b940` | 2026-10-12 | `feat(week05): add interactive pendulum and double-pendulum chaos simulations` | `simulations/`：3 份交互模拟器 HTML |
| 6 | `a503622` | 2026-10-12 | `docs(week05): archive human-AI collaboration reflection report` | `reflections/人机协同三反思.docx` |
| 7 | `5171d0b` | 2026-10-12 | `docs(week05): index archived simulations and reflection report in README` | README 产物索引 + 无菌清单更新 |
| 8 | `beb49e9` | 2026-10-12 | `docs(week05): add repo links, tree and commit baseline to READMEs` | README 仓库链接、完整目录树、基线记录 |

## 阶段三 · 缺陷修复与文档完善

| # | 哈希 | 日期 | 提交信息 | 归档内容 |
|---|------|------|----------|----------|
| 9 | `4742ad9` | 2026-10-12 | `fix(week05): inline kobe image as base64 to remove broken assets dependency` | 双摆模拟器改用自包含版本（28,041 → 44,451 字节） |
| 10 | `ab20c4c` | 2026-10-12 | `docs(week05): complete commit-history table and add self-containment check` | 补全提交历史表 + 自包含验证项 |
| 11 | `667822e` | 2026-10-12 | `docs(week05): extract commit ledger into CHANGELOG.md` | 提交台账拆分至本文件；两份 README 增加 CHANGELOG 入口 |

---

## 🔧 修复记录

### `assets/` 外部依赖导致图片空白（提交 9 解决）

**现象：** 归档版 `食质261夏尚晨-双摆混沌模拟器.html` 中摆球位置的人物头像不显示。

**原因：** 该 HTML 用 `kobeImg.src = 'assets/kobe.png'` 引用同目录外的图片，但归档时只拷贝了 HTML 本身、未拷贝 `assets/` 文件夹。文件被单独提交后引用路径落空。

**解决：** 改为用户提供的 base64 内嵌版本，图片数据直接写进 HTML，文件彻底自包含。

**验证：** 另两份模拟器经 grep 确认从未使用图片（`new Image()`、`data:image`、`assets/` 命中数均为 0），不受此问题影响。

---

## ✅ 验收校验

| 校验项 | 方法 | 结果 |
|--------|------|------|
| 双摆模拟器可运行 | 浏览器加载 + `evaluate_script` | 标题正确、2 画布、3 滑块、重置／火箭加速按钮齐全、θ 实时变化 |
| 控制台报错 | 浏览器错误监听 | **0 报错** |
| 三份 HTML 自包含 | grep `assets/` / `src=` / `new Image` | 外部依赖 0 处 |
| 工作区纯净独立 | `git status` 逐次比对 | 第 1–10 条提交**仅**改动 `week05_pendulum_sim/` 内部文件；第 667822e（本台账拆分之提交）额外更新了根目录 `README.md` 的快捷入口，属跨文件链接同步，未触碰其他周次目录 |

---

## 📌 关于"少一行"的机制说明

Git 提交哈希由提交内容计算得出，因此**任何文件都无法写入"本次提交自己的"哈希**——就像人没法把自己举起来。

CHANGELOG 的惯用做法恰好化解了这点：每条记录在**下一次**改动时补写。本文件当前已记录至第 11 条（`667822e`）；为本次修订而做的提交将顺位成为第 12 条，由本工作区后续任一次提交补入——台账因此始终只落后一条，并随每次改动自动收敛到完整。实时、无遗漏的列表请见文首「提交记录」链接。

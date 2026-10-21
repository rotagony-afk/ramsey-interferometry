# Ramsey 量子干涉仪 · 调研资料包

**整理日期**：2026-10 ｜ **用途**：开展 Ramsey 干涉仪科研前的文献与理论准备 ｜ **位置**：本仓库根目录（GitHub 版不含 PDF，见下）

> **仓库说明**：本仓库只发布文本资产（笔记、题录、清单、图、脚本）。papers 下的 PDF 因版权与体积原因已通过 .gitignore 排除；如需全文，请按 papers/INDEX.md 中的 DOI 自行获取（途径见 14_全文获取清单.md）。上传/托管方法见 GITHUB上传指南.md。


---

## 0. 三分钟读懂这个资料包

- **合并文献库 209 条**：本资料包精选 45 条（期刊 40 + 专著 5，DOI 逐条 Crossref 核对）+ 外部调研报告去重后 164 条（题录已核验）；总表见 06_文献总表.md，字段见 06_文献清单.csv。
- **全文 PDF 38 篇**：arXiv 开放获取版 + 出版社版（12 篇由图书馆下载），必读 32 篇已全部到手；清单见 papers/INDEX.md，获取策略见 14_全文获取清单.md。
- **7 篇自写文档**：文献综述（01）、核心文献精读笔记（02）、理论公式与推导（03）、研究路线与实验方案建议（04）、科研方向清单（07）、一年期论文与大挑作战计划（08）、PRL 可行性评估（09）。
- **外部调研报告已导入并核查**：原件（10，170 条引用）、扩展 BibTeX（11，176 条）、核查说明（12）、文献清单（13）；176 条题录中 173 条已用 Crossref/arXiv 逐条核验。
- **1 个可复现工具**：tools/ramsey_fringe_plot.py，用 numpy + Pillow 算出并画出 Ramsey 条纹（figures/ramsey_fringes.png），公式已与 2×2 矩阵传播逐点核对（最大偏差 5.6e-16）。

一句话总结这个领域：**Ramsey 方法把"一次长脉冲的拉比谱"换成"两段短脉冲 + 中间自由演化 T"，用 T 换取谱线宽度 ~1/(2T)；它既是原子钟的谱学骨架，也是原子干涉仪、量子传感器与多体量子模拟中"相位放大—读取"的通用协议。**

---

## 1. 目录与阅读顺序

| 文件 | 内容 | 建议何时看 |
|---|---|---|
| 01_Ramsey干涉仪_文献综述.md | 物理内核、历史脉络、四种现代形态、平台比较、关键技术问题、选题地图 | **先看**，建立全局图景 |
| 02_核心文献_精读笔记.md | 40 条文献逐条精读：贡献、核心内容、与本课题的关系、阅读建议 | 边读原文边看 |
| 03_理论公式与推导.md | 从哈密顿量到精确条纹公式、灵敏度/Allan 偏差、压缩增益、光频移抑制、原子干涉相位 | 动手推一遍，做实验前必看 |
| 04_研究路线与实验方案建议.md | 四条可选技术路线、设备与指标、6 个月里程碑、风险、可直接执行的第一个实验 | 定方向时看 |
| 07_科研方向清单.md | 18 个适合本平台的方向（难度/周期/设备/产出）、三套实施方案与「不建议现在做」清单 | **选方向时看**（与 04 互补） |
| 08_大挑与论文年度计划.md | 以"论文 + 大挑"为目标的 12 个月倒排计划：选题定案、甘特表、论文方案、大挑材料、实物搬运三方案、预算与风险 | **定了目标就看** |
| 09_PRL可行性评估.md | 能否上 PRL 的坦率评估：PRL 标准、本工作差距、PRL 级工作的特征、现实投稿阶梯与时间成本 | **讨论目标时看** |
| 10_外部调研报告_原始版.md | 外部调研报告原文（2026-10-21，170 条引用 + 6 条附录，按四条路线组织） | 查广度、找引用 |
| 11_外部调研报告_参考文献176条.bib | 由该报告生成的扩展 BibTeX（176 条，题录已核验） | 扩充个人文献库 |
| 12_外部调研报告_核查说明.md | 核查结果、发现的问题、与本资料包的重合与互补、13 条建议精读 | **合并前必看** |
| 13_外部调研报告_文献清单.csv | 176 条的表格版（编号/类型/年份/DOI/核查状态） | Excel 筛选 |
| 14_全文获取清单.md | 全文获取现状（必读 32 篇全齐，38 篇本地 PDF）与重点/拓展层补全策略 | 准备读全文时看 |
| GITHUB上传指南.md | 上传到 GitHub 的完整操作（公开/私有、Desktop/命令行/网页三种路线、LFS、认证与常见问题） | 上传前看 |
| .gitignore / .gitattributes | 默认排除 papers 下的 PDF；含 Git LFS 模板 | 上传前检查 |
| 15_数据库覆盖对照.md | 图书馆 13 个数据库对本资料包 209 条的覆盖对照：能下哪些、APS 盲区、必读 12 篇的逐条获取路线 | 下载全文前看 |
| 05_参考文献.bib | 合并 BibTeX 209 条（精选键 A_/B_/C_… + 外部 ext<编号>_…） | 写论文时用 |
| 06_文献总表.md | 209 条合并总表（按优先级/类别浏览） | 找文献时用 |
| 06_文献清单.csv | 209 条表格（UTF-8 BOM，Excel 直接打开；含优先级、PDF 有无、来源） | 建个人文献库 |
| figures/ramsey_fringes.png | Ramsey 条纹与线宽标度图 | 做组会 PPT 可直接用 |
| tools/ramsey_fringe_plot.py | 图与数值的生成脚本（numpy + Pillow，无需 matplotlib） | 改参数自己算 |
| papers/ | 38 篇 PDF + INDEX.md 索引（必读 32 篇全齐） | 直接读 |

---

## 2. 一页速览：Ramsey 方法到底是什么

1. **单脉冲（Rabi）**：一个持续 τ 的驱动场，谱线宽度由脉冲时长决定，线宽 ~ 1/τ，无法靠"加长脉冲"无限提高分辨率（扫描越久、谱越窄，但单次测量只给一条宽谱）。
2. **分离场（Ramsey）**：把同样的驱动切成两个短脉冲（各 ~τ），中间让原子自由演化 T。原子带着第一个脉冲写下的相位走过 T，第二个脉冲把这份相位"读"成布居差。条纹间距 **1/T**，中心条纹半高全宽 **≈ 1/(2T)**，于是用两个短脉冲就得到等效于"长脉冲 T"的分辨率，而脉冲之间的原子不受光场干扰——这正是频标与干涉仪需要的。
3. **数学内核**（约定 δ = ω₀ − ω，详见 03）：

   P(δ) = 4 sin²(θ/2) · (Ω_R/Ω_eff)² · [ cos(θ/2)cos(δT/2) − (δ/Ω_eff) sin(θ/2) sin(δT/2) ]²

   其中 θ = Ω_eff τ 为脉冲面积，Ω_eff = √(Ω_R² + δ²)。理想短脉冲、π/2–π/2 情形退化为 P = cos²(δT/2)。

**五个关键结论**（后面文档反复用到）：

| 量 | 表达式 | 含义 |
|---|---|---|
| 条纹间距 | 1/T（Hz） | 决定"看多远"：T = 10 ms → 100 Hz |
| 中心条纹宽度（短脉冲极限） | 1/(2T)（FWHM，Hz） | 决定"多准"：T = 10 ms → 50 Hz |
| 品质因数 | Q ≈ νT | 微波 6.8 GHz、T = 1 s 时 Q ≈ 7×10⁹ |
| 单次频率灵敏度（投影噪声极限） | δν = 1/(2πT√N) | N 为原子数；这正是标准量子极限（SQL） |
| 压缩后的灵敏度 | δν ∝ 1/(2πT·ξ√N) | ξ² < 1 为压缩参数；4.4 dB 增益 ≈ ξ² = 0.36 |

---

## 3. 文献覆盖与分类

| 类别 | 条数 | 代表文献 | 覆盖度自评 |
|---|---|---|---|
| A 奠基与经典（Rabi、Ramsey 原始论文、诺奖演讲） | 6 | Ramsey 1950；Ramsey 1990 | 强，一手文献齐全 |
| B 原子干涉仪与 Ramsey–Bordé | 11 | Bordé 1989；Kasevich–Chu 1991/1992；Cronin RMP 2009 | 强 |
| C 原子钟与 Ramsey 谱（喷泉、光钟、晶格钟、CPT、hyper-Ramsey） | 7 | Ludlow RMP 2015；Yudin 2010；Sanner 2018；Campbell 2017 | 强 |
| D 量子增强与量子计量（投影噪声、压缩、纠缠、Fisher） | 9 | Itano 1993；Wineland 1994；Pezzè RMP 2018；Pedrozo 2020；Eckner 2023 | 强 |
| E 平台拓展（离子、NV 色心） | 5 | Wineland 1998；Barry RMP 2020；Degen RMP 2017 | 中 |
| F 空间与前沿（SAGE） | 1 | Tino 2019 | 弱（仅作展望） |
| G 多体与量子模拟（Ramsey 型多体谱学） | 1 | Islam 2015 | 弱（可选方向） |

**尚未覆盖、后续可补的**：超导量子比特上的 Ramsey（cQED 教科书与 RMP 93, 025005）；分子/里德堡微波谱学；Ramsey 在量子计算中的门校准；中文期刊综述（《物理学报》《物理学进展》）与国内学位论文。如果你告诉我具体平台，我可以按平台再补一轮。

---

## 4. 推荐阅读路径（4 周）

| 阶段 | 任务 | 产出 |
|---|---|---|
| 第 1 天 | 读 **Ramsey 1950**（只看第 I–II 节与结论）+ **Ramsey 1990 诺奖演讲**；读本资料包 01 的 §1–2 | 能用三句话说清"为什么两个短脉冲比一个长脉冲好" |
| 第 1 周 | 把 **03 的公式自己推一遍**（两能级 → 旋转坐标系 → 双脉冲精确解 → 条纹参数）；跑一遍 tools/ramsey_fringe_plot.py，改 T、τ、Ω_R 看条纹怎么变 | 一页手写推导 + 一张自己算的图 |
| 第 2 周 | 读 **Cronin RMP 2009**（原子干涉部分）与 **Ludlow RMP 2015**（光钟谱学与系统误差部分，按需选读）；对照 02 的笔记 | 画出"哪类系统误差来自脉冲、哪类来自自由演化"的分类表 |
| 第 3 周 | 按 **04** 选定路线，精读该路线 5 篇核心文献（02 已给出阅读重点） | 一页"我打算做什么、需要什么设备、预期指标" |
| 第 4 周 | 写 2–3 页开题式综述（用 01 的框架 + 自己的公式推导），把 05 的 bib 导入 Zotero | 可交给导师/组会讨论的文档 |

**不要做的三件事**：① 一上来就读 Pezzè RMP（900 多条文献的综述，容易淹死）；② 把"Ramsey 条纹"和"Rabi 振荡"混为一谈（前者是频率域的干涉条纹，后者是时间域的布居振荡）；③ 只看综述不推公式（Ramsey 方法的细节几乎全在公式的符号与相位约定里）。

---

## 5. 精选速查表（40 条期刊文献）

> 完整合并库（209 条）见 **06_文献总表.md** 与 **06_文献清单.csv**；本表只保留最核心的 40 条，便于贴在墙上。

说明：DOI 已逐条核对；RMP 的文章号（035005、015004 等）Crossref 未给出，按期刊卷页规则人工补录；"优先级"为**必读 / 重点 / 拓展**三档（合并库统计：必读 32、重点 54、拓展 123）。完整 PDF 列表见 papers/。

| # | 文献 | 出处 | DOI / arXiv | 优先级 |
|---|---|---|---|---|
| 1 | Rabi 分子束磁共振方法（Ramsey 方法的前身） | Rabi, Millman, Kusch 等 1939, *Physical Review* 55, 526-535 | 10.1103/physrev.55.526 | 必读 |
| 2 | 分离振荡场方法首篇通讯（1949） | Ramsey 1949, *Physical Review* 76, 996-996 | 10.1103/physrev.76.996 | 必读 |
| 3 | 分离振荡场方法原始论文（Ramsey 1950） | Ramsey 1950, *Physical Review* 78, 695-699 | 10.1103/physrev.78.695 | 必读 |
| 4 | Physics Today：连续振荡场方法回顾 | Ramsey 1980, *Physics Today* 33, 25-30 | 10.1063/1.2914161 | 重点 |
| 5 | Ramsey 诺贝尔演讲：分离振荡场与氢激射器 | Ramsey 1990, *Reviews of Modern Physics* 62, 541-552 | 10.1103/revmodphys.62.541 | 必读 |
| 6 | 早期原子钟历史 | Ramsey 2005, *Metrologia* 42, S1-S3 | 10.1088/0026-1394/42/3/s01 | 拓展 |
| 7 | 内部态标记原子干涉仪（Ramsey–Bordé） | Bordé 1989, *Physics Letters A* 140, 10-12 | 10.1016/0375-9601(89)90537-9 | 必读 |
| 8 | 受激拉曼跃迁原子干涉仪（Kasevich–Chu） | Kasevich, Chu 1991, *Physical Review Letters* 67, 181-184 | 10.1103/physrevlett.67.181 | 必读 |
| 9 | 受激拉曼跃迁的速度选择 | Kasevich, Weiss, Riis 等 1991, *Physical Review Letters* 66, 2297-2300 | 10.1103/physrevlett.66.2297 | 重点 |
| 10 | 光脉冲原子干涉仪测重力加速度 | Kasevich, Chu 1992, *Applied Physics B Photophysics and Laser Chemistry* 54, 321-332 | 10.1007/bf00325375 | 必读 |
| 11 | 自由落体原子测 g（Nature 1999） | Peters, Chung, Chu 1999, *Nature* 400, 849-852 | 10.1038/23655 | 重点 |
| 12 | 原子干涉陀螺仪测转动 | Gustavson, Bouyer, Kasevich 1997, *Physical Review Letters* 78, 2046-2049 | 10.1103/physrevlett.78.2046 | 重点 |
| 13 | 原子干涉测引力红移 | Müller, Peters, Chu 2010, *Nature* 463, 926-929 | 10.1038/nature08776 | 拓展 |
| 14 | RMP 综述：原子与分子的光学与干涉 | Cronin, Schmiedmayer, Pritchard 2009, *Reviews of Modern Physics* 81, 1051-1129 | 10.1103/revmodphys.81.1051 · arXiv:0712.3703 | 必读 |
| 15 | 原子干涉测量精细结构常数 | Parker, Yu, Zhong 等 2018, *Science* 360, 191-195 | 10.1126/science.aap7706 | 重点 |
| 16 | 规避海森堡不确定性原理的等效原理检验 | Roura 2017, *Physical Review Letters* 118 | 10.1103/physrevlett.118.160401 · arXiv:1509.08098 | 拓展 |
| 17 | 冷原子干涉检验弱等效原理：现状与展望（中文作者综述） | Yuan, Wu, Yang 2023, *Symmetry* 15, 1769 | 10.3390/sym15091769 | 重点 |
| 18 | RMP 综述：光学原子钟 | Ludlow, Boyd, Ye 等 2015, *Reviews of Modern Physics* 87, 637-701 | 10.1103/revmodphys.87.637 · arXiv:1407.3493 | 必读 |
| 19 | 原子喷泉钟综述 | Wynands, Weyers 2005, *Metrologia* 42, S64-S79 | 10.1088/0026-1394/42/3/s08 | 重点 |
| 20 | 费米简并三维光晶格钟 | Campbell, Hutson, Marti 等 2017, *Science* 358, 90-94 | 10.1126/science.aam5538 · arXiv:1702.01210 | 重点 |
| 21 | Hyper-Ramsey 谱：抑制光频移 | Yudin, Taichenachev, Oates 等 2010, *Physical Review A* 82, 011804 | 10.1103/physreva.82.011804 · arXiv:0910.5948 | 必读 |
| 22 | 自平衡 Ramsey 谱 | Sanner, Huntemann, Lange 等 2018, *Physical Review Letters* 120, 053602 | 10.1103/physrevlett.120.053602 · arXiv:1707.02630 | 必读 |
| 23 | CPT 原子钟综述 | Vanier 2005, *Applied Physics B* 81, 421-442 | 10.1007/s00340-005-1905-3 | 拓展 |
| 24 | 冷原子 CPT 中的 Ramsey 干涉（2024 综述） | Han, Lu, Lee 2024, *Advances in Physics: X* 9, 2317896 | 10.1080/23746149.2024.2317896 | 必读 |
| 25 | 量子投影噪声 | Itano, Bergquist, Bollinger 等 1993, *Physical Review A* 47, 3554-3570 | 10.1103/physreva.47.3554 | 必读 |
| 26 | 压缩原子态与投影噪声谱学 | Wineland, Bollinger, Itano 等 1994, *Physical Review A* 50, 67-88 | 10.1103/physreva.50.67 | 必读 |
| 27 | 量子纠缠改善频标 | Huelga, Macchiavello, Pellizzari 等 1997, *Physical Review Letters* 79, 3865-3868 | 10.1103/physrevlett.79.3865 | 重点 |
| 28 | 最大关联态的最优频率测量 | Bollinger, Itano, Wineland 等 1996, *Physical Review A* 54, R4649-R4652 | 10.1103/physreva.54.r4649 | 重点 |
| 29 | Nature Photonics 综述：量子计量进展 | Giovannetti, Lloyd, Maccone 2011, *Nature Photonics* 5, 222-229 | 10.1038/nphoton.2011.35 · arXiv:1102.2318 | 必读 |
| 30 | RMP 综述：原子系综非经典态量子计量 | Pezzè, Smerzi, Oberthaler 等 2018, *Reviews of Modern Physics* 90, 035005 | 10.1103/revmodphys.90.035005 · arXiv:1609.01609 | 必读 |
| 31 | 量子自旋压缩综述 | Ma, Wang, Sun 等 2011, *Physics Reports* 509, 89-165 | 10.1016/j.physrep.2011.08.003 · arXiv:1011.2978 | 重点 |
| 32 | 光钟跃迁上的纠缠（Nature 2020） | Pedrozo-Peñafiel, Colombo, Shu 等 2020, *Nature* 588, 414-418 | 10.1038/s41586-020-3006-1 · arXiv:2006.07501 | 必读 |
| 33 | 里德堡相互作用实现光钟自旋压缩（Nature 2023） | Eckner, Darkwah Oppong, Cao 等 2023, *Nature* 621, 734-739 | 10.1038/s41586-023-06360-6 · arXiv:2303.08078 | 必读 |
| 34 | 离子量子态相干操控的实验问题（含 Ramsey 谱） | Wineland, Monroe, Itano 等 1998, *Journal of Research of the National Institute of Standards and Technology* 103, 259 | 10.6028/jres.103.019 | 重点 |
| 35 | NV 色心动力学解耦（Ramsey 型序列） | de Lange, Wang, Ristè 等 2010, *Science* 330, 60-63 | 10.1126/science.1192739 | 重点 |
| 36 | RMP 综述：NV 金刚石磁测量灵敏度优化 | Barry, Schloss, Bauch 等 2020, *Reviews of Modern Physics* 92, 015004 | 10.1103/revmodphys.92.015004 · arXiv:1903.08176 | 必读 |
| 37 | 用 Ramsey 干涉检验因果非线性量子力学（离子） | Broz, You, Khan 等 2023, *Physical Review Letters* 130, 200201 | 10.1103/physrevlett.130.200201 · arXiv:2206.12976 | 拓展 |
| 38 | SAGE：空间原子重力探测计划 | Tino, Bassi, Bianco 等 2019, *The European Physical Journal D* 73 | 10.1140/epjd/e2019-100324-6 · arXiv:1907.03867 | 拓展 |
| 39 | Ramsey 型干涉测多体纠缠熵 | Islam, Ma, Preiss 等 2015, *Nature* 528, 77-83 | 10.1038/nature15750 · arXiv:1509.01160 | 重点 |
| 40 | 量子传感综述：NV/离子/原子平台，Ramsey 作为相干探针 | Degen, Reinhard, Cappellaro 2017, *Reviews of Modern Physics* 89, 035002 | 10.1103/revmodphys.89.035002 | 必读 |

**5 本专著**（不占上表编号，bib 中已收录）：

1. N. F. Ramsey, *Molecular Beams*, Oxford University Press, 1956 —— Ramsey 方法的"圣经"，第 V 章讲分离振荡场。
2. P. R. Berman (ed.), *Atom Interferometry*, Academic Press, 1997 —— 原子干涉仪经典文集。
3. H. J. Metcalf, P. van der Straten, *Laser Cooling and Trapping*, Springer, 1999 —— 冷原子基础。
4. C. J. Foot, *Atomic Physics*, Oxford University Press, 2005 —— 两能级、拉比、拉姆齐条纹的最佳入门教材。
5. 王义遒, 《原子的激光冷却与陷俘》, 北京大学出版社, 2007 —— 中文教材（版本信息请按图书馆编目核对）。

---

## 6. 术语表（读文献时对照）

| 英文 | 中文 | 一句话解释 |
|---|---|---|
| separated oscillatory fields | 分离振荡场 | Ramsey 方法的本名，1950 年论文标题 |
| Ramsey fringes | 拉姆齐条纹 | 扫频得到的周期性布居条纹，间距 1/T |
| free precession / interrogation time | 自由演化时间 /  interrogation 时间 T | 两个脉冲之间的间隔，决定线宽 |
| fringe contrast | 条纹对比度 | (P_max−P_min)/(P_max+P_min)，受退相干与脉宽影响 |
| Rabi frequency | 拉比频率 Ω_R | 驱动场与原子耦合强度，决定 π/2 脉冲时长 |
| pulse area | 脉冲面积 θ | Ω_R τ；π/2 脉冲即 θ = π/2 |
| light shift / AC Stark shift | 光频移 | 探测光或钟激光导致的能级移动，Ramsey 谱的主要系统误差 |
| hyper-Ramsey / autobalanced Ramsey | 超拉姆齐 / 自平衡拉姆齐 | 用复合脉冲或成对序列抵消光频移的两类方法 |
| projection noise (SQL) | 投影噪声（标准量子极限） | N 个独立原子测量布居差时的 1/√N 涨落 |
| spin squeezing | 自旋压缩 | 把一个正交分量的噪声压到 SQL 以下（ξ² < 1） |
| quantum Fisher information | 量子费希尔信息 | 参数估计的最终精度上限（Cramér–Rao） |
| Allan deviation σ_y(τ) | 阿伦偏差 | 频标稳定度的标准表征，随平均时间按 1/√τ 下降 |
| Dick effect | 迪克效应 | 本地振荡器噪声经"死时间"混叠进频标稳定度 |
| dead time | 死时间 | 两次 interrogation 之间的准备/探测时间，带来 Dick 效应 |
| Ramsey–Bordé interferometer | 拉姆齐–博尔德干涉仪 | 用内部态标记的四区原子干涉仪，对转动/重力敏感 |
| k_eff | 有效波矢 | 拉曼双光子过程的动量转移，~1.6×10⁷ m⁻¹（780 nm 反向） |
| recoil frequency | 反冲频率 | 光子反冲导致的频率移动，用于测 h/m 与精细结构常数 |
| equivalence principle (UFF) | 等效原理（自由落体普适性） | 原子干涉仪检验引力理论的核心目标 |
| systematic uncertainty | 系统不确定度 | 与统计误差相对，Ramsey 谱学研究的重心 |

---

## 7. 数据、版权与核对说明

- **元数据核对**：40 条期刊文献的 DOI 全部通过 Crossref API 逐条读取（2026-10），标题/作者/卷/页/年份以 Crossref 记录为准；少数 Crossref 缺页的条目（RMP 文章号）按期刊排版规则补录，已在表与 bib 中保留 DOI 以便复核。
- **PDF 来源**：papers/ 中 38 个 PDF——26 篇为 arXiv/开放获取版本（文件名标注 arXiv 编号），12 篇为出版社版（由图书馆下载，其中 Rabi 1939、Bordé 1989 为扫描件、无文字层）；它们**不等于**正式发表版（排版、页码、勘误可能不同），引用时请以 DOI 指向的版本为准。
- **已知待核对项**：① 王义遒《原子的激光冷却与陷俘》的版次与出版年（按图书馆编目核对）；② Tino et al. 2019 EPJ D 的文章号 228（Crossref 未返回页信息）。
- **数值来源**：figures/ 与 03 中的所有数字（条纹宽度、FWHM、灵敏度算例）都由 tools/ramsey_fringe_plot.py 及同款公式计算得到，可复现；与 2×2 矩阵传播的偏差 ≤ 6×10⁻¹⁶。

---

## 8. 待确认的三件事（确认后我可以把资料包收窄成"可执行方案"）

1. **平台**：是冷原子（MOT/喷泉/光晶格）、热原子束、离子、NV 色心，还是以"教学演示 + 冷原子"为主？现有工作区里的 MOT 教案与 MOT-Thesis 文献暗示你在做**铷冷原子**，若如此，04 的 R1（微波 Ramsey）与 R2（拉曼 Ramsey / 原子重力仪）是最顺的入口。
2. **目标**：频标（稳定度/准确度）、惯性传感（g、转动、重力梯度）、基础物理检验（等效原理、洛伦兹破坏）、量子增强（压缩/纠缠），还是教学实验？
3. **设备**：现有微波源/拉曼光路/稳频激光/磁屏蔽/隔振平台的情况 —— 这决定 04 里哪条路线能在 6 个月内出结果。

补一句：如果需要 **DOCX 版综述**（便于打印或交给导师）、**Zotero 可直接导入的 RIS 文件**、或**每周自动抓取 arXiv 新预印本的脚本**，告诉我即可，这些都能在现有材料上快速生成。

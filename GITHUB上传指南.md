# 把文献库上传到 GitHub：操作指南

> 适用环境：Windows。本机目前**没有安装 git**（已确认），但 winget 可用。
> 本目录已完成准备：.gitignore 与 .gitattributes 已就位，papers 下的 PDF 默认被排除。

---

## 0. 先做一个决定：公开还是私有？

| 方案 | 仓库内容 | 体积 | 版权风险 | 建议 |
|---|---|---|---|---|
| A. 公开仓库（推荐） | 只放文本资产：15 篇 md、bib、csv、图、脚本、papers/INDEX.md | 约 0.6 MB | 无（不含出版社 PDF） | 适合分享方法、笔记、代码 |
| B. 私有仓库 | 全部内容 + 38 篇 PDF | 约 170 MB（需 Git LFS） | 出版社版 PDF 仅限个人使用；私有仓库也属于再分发，风险自担 | 只想自己备份 |
| C. 公开 + 只放 arXiv 版 | 38 篇里挑 license 允许再分发的 | 数十 MB | 需逐篇查 license，麻烦 | 不推荐 |

**本文档默认按方案 A 写**；方案 B 的差异见第 4 节。

---

## 1. 仓库里会包含什么

| 文件 / 目录 | 入库 | 说明 |
|---|---|---|
| README.md、01 到 15 号的 md | 是 | 综述、精读、公式、路线、计划、核查等全部文本 |
| 05 参考文献.bib、06 文献清单.csv、06 文献总表.md | 是 | 题录与清单（事实性数据） |
| figures/、tools/、papers/INDEX.md | 是 | 图、可复现脚本、PDF 索引 |
| papers 下的 38 篇 PDF | 否（默认排除） | 版权 + 体积；别人可按 INDEX 里的 DOI 自行获取 |
| .gitignore、.gitattributes | 是 | 已生成 |

---

## 2. 路线 A：GitHub Desktop（最省事，适合本机没装 git）

1. 下载安装 GitHub Desktop：https://desktop.github.com/ ，用 GitHub 账号登录。
2. 菜单 File → Add local repository，选择本目录。
3. 若提示 not a git repository，点 create a repository（它会自动执行 git init）。
4. 左下角填 Summary，例如「初始化：Ramsey 文献调研资料包」，点 Commit to main。
5. 右上角 Publish repository：
   - Name 建议英文：ramsey-interferometry-notes
   - 需要私有就勾选 Keep this code private（即方案 B）
6. 之后每次修改：Commit，然后 Push。

> GitHub Desktop 自带 git 与凭据管理，不需要自己配 PAT。

---

## 3. 路线 B：安装 Git + 命令行（最可控）

第一步，安装 Git，二选一：

    winget install --id Git.Git -e

或下载 https://git-scm.com/download/win

第二步，打开 PowerShell，逐条执行：

    cd "E:\My Project\Quantum\Ramsey干涉仪_调研"

    git init
    git config user.name  "你的名字"
    git config user.email "你的邮箱"
    git config core.quotepath false          # 中文文件名显示正常

    git add .
    git status                                # 关键：确认列表里没有 papers 下的 pdf

    git commit -m "Ramsey 量子干涉仪调研资料包（文本/元数据/代码，PDF 不含）"
    git branch -M main
    git remote add origin https://github.com/你的用户名/ramsey-interferometry-notes.git
    git push -u origin main

认证：GitHub 不允许用账号密码 push，两种方式——

- PAT（个人访问令牌）：GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → 勾选 repo → 生成并复制；push 时用户名填 GitHub 用户名、密码填 PAT。
- 或者装 GitHub CLI：winget install --id GitHub.cli -e，然后 gh auth login，再 gh repo create ramsey-interferometry-notes --source . --push。

方案 A 只有 0.6 MB，push 几秒完成；方案 B 首次 push 170 MB 会很慢。

---

## 4. 如果你坚持要把 PDF 放进去（方案 B，私有仓库）

1. 删掉 .gitignore 里 papers/*.pdf 这一行；
2. 启用 Git LFS（GitHub 对单文件超过 50 MB 会警告，LFS 是推荐做法）：

    git lfs install
    git lfs track "*.pdf"
    git add .gitattributes
    git add .
    git commit -m "加入 38 篇文献 PDF（Git LFS）"
    git push -u origin main

注意事项：

- 仓库总大小约 170 MB；最大单文件 36 MB（Han 2024 Adv. Phys. X）和 33 MB（Huang 2024 Appl. Phys. Rev.）。
- GitHub 免费 LFS 额度：存储 1 GB、流量 1 GB/月，个人偶尔克隆够用。
- 版权：APS（PRL/PRA/RMP）、Nature、Elsevier、Optica 的出版社版 PDF 只授权个人阅读；放进 GitHub（即使私有）严格说仍是再分发，风险自担。真要备份，更稳的是本地 + 加密云盘。
- 公开仓库绝对不能放这些 PDF，会被 DMCA 下架并影响账号。

---

## 5. 路线 C：网页上传（只适合纯文本部分）

1. GitHub 网页 → New repository（勾选 README 初始化）。
2. Add file → Upload files，拖入：README.md、01 到 15 号的 md、05/06 的 bib 与 csv、figures/、tools/、papers/INDEX.md、.gitignore。
3. 浏览器上传单文件上限 25 MB、一次最多 100 个文件，所以 36 MB 和 33 MB 的两篇 PDF 一定失败；方案 C 不要含 PDF。

---

## 6. 上传前检查清单

- git status 里没有 papers 下的 pdf（方案 A）
- README 开头已说明「PDF 不随仓库发布」（已写好）
- 没有个人敏感信息（本目录只有本机路径，无姓名/邮箱/学号）
- 仓库名英文、描述与 topics 填好（见第 7 节）
- 若公开：确认没有未发表数据、导师未公开结果
- 想好许可：文本部分可加 CC BY 4.0 或 CC BY-NC 4.0，或不加（默认保留所有权利）

---

## 7. 推荐的仓库设置

- 名称：ramsey-interferometry-notes
- 描述：Ramsey 干涉仪文献调研：209 条题录、40 条精读、公式推导与实验路线（PDF 不含）
- Topics：ramsey-interferometry、cold-atoms、quantum-metrology、atomic-clocks、chinese
- 可选：Settings → Pages，用 GitHub Pages 把 01 号综述渲染成网页，阅读体验更好。
- 以后更新：git add -A，git commit -m "更新 xxx"，git push

---

## 8. 常见问题

| 现象 | 原因 | 解决 |
|---|---|---|
| git 不是可识别的命令 | 本机未安装 git | 安装 Git 或用 GitHub Desktop |
| push 报 403 / Authentication failed | 用了账号密码 | 改用 PAT 或 gh auth login |
| 中文文件名显示成转义串 | git 默认转义 | git config --global core.quotepath false |
| 单个 PDF 上传失败 | 超过 25 MB（网页）或 50 MB 警告 | 用 Git LFS，或按方案 A 排除 PDF |
| 仓库太大、clone 慢 | 含 170 MB PDF | 用方案 A；或 git lfs migrate 清理历史 |

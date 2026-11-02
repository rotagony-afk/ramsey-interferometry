# -*- coding: utf-8 -*-
"""生成《冷原子干涉仪科研说明》DOCX。"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

BODY_FONT = "宋体"
HEAD_FONT = "黑体"

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.4)
sec.top_margin = sec.bottom_margin = Cm(2.4)

# 默认样式
st = doc.styles["Normal"]
st.font.name = BODY_FONT
st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)


def run_font(run, name=BODY_FONT, size=10.5, bold=False, color=None):
    run.font.name = name
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rPr.makeelement(qn("w:rFonts"), {})
        rPr.append(rFonts)
    rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    if color is not None:
        run.font.color.rgb = color


def para(text, size=10.5, bold=False, indent=True, align=None, before=0, after=6, line=1.35):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    if indent:
        pf.first_line_indent = Pt(21)
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "justify":
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(text)
    run_font(r, size=size, bold=bold)
    return p


def heading(text, level=1):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(14 if level == 1 else 10)
    pf.space_after = Pt(6)
    pf.keep_with_next = True
    r = p.add_run(text)
    run_font(r, name=HEAD_FONT, size=15 if level == 1 else 12, bold=True)
    return p


def title(text, sub=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    run_font(r, name=HEAD_FONT, size=20, bold=True)
    if sub:
        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(12)
        r2 = p2.add_run(sub)
        run_font(r2, name=HEAD_FONT, size=11, bold=False)


def bullet(text, size=10.5):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(3)
    pf.line_spacing = 1.3
    r = p.add_run(text)
    run_font(r, size=size)


def table(headers, rows, widths=None, size=9.5, caption=None):
    if caption:
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(6)
        cp.paragraph_format.space_after = Pt(2)
        cp.paragraph_format.keep_with_next = True
        rc = cp.add_run(caption)
        run_font(rc, name=HEAD_FONT, size=9.5, bold=True)
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    trPr0 = t.rows[0]._tr.get_or_add_trPr()
    trPr0.append(trPr0.makeelement(qn("w:tblHeader"), {}))
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        run_font(r, name=HEAD_FONT, size=size, bold=True)
    for row in rows:
        tr = t.add_row()
        trPr = tr._tr.get_or_add_trPr()
        trPr.append(trPr.makeelement(qn("w:cantSplit"), {}))
        cells = tr.cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            r = p.add_run(str(val))
            run_font(r, size=size)
    if widths:
        for i, w in enumerate(widths):
            for r_ in t.rows:
                r_.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


# ============ 封面 ============
title("冷原子干涉仪精密测量研究说明",
      "面向 1×10⁻⁸ 精度水平的 Ramsey 干涉仪与冷原子重力仪实验")

for line in [
    "编制日期：2026 年 11 月",
    "实验平台：铷冷原子 MOT + 780 nm 激光 + 吸收成像",
    "编制依据：三个自建文献库（Ramsey 方法 209 条、原子干涉陀螺仪 209 条、冷原子重力仪专题 38 篇）",
]:
    para(line, size=9.5, indent=False, align="center", before=0, after=2)
para("", indent=False, after=6)

heading("摘要", 1)
para("本说明面向约 1×10⁻⁸ 相对精度的冷原子干涉实验，以“冷原子重力仪 + 双干涉仪共模抑制”为核心方向，"
     "系统阐述研究背景、国内外现状、研究目标与考核指标、研究内容、技术路线、精度预算、创新点、可行性、"
     "12 个月研究计划与预期成果。")
para("文献调研覆盖三个自建文献库（Ramsey 方法 209 条、原子干涉陀螺仪 209 条、冷原子重力仪专题 38 篇），"
     "核心判断是：1×10⁻⁸ 是“系统误差可测、工程化可做”的精度窗口——它足以开展波前、科里奥利力、"
     "拉曼光频移、振动等系统项的定量研究与抑制，也足以观测固体潮、开展转台标定与传感器融合演示；"
     "但距离等效原理检验（10⁻¹³）、精细结构常数测量（10⁻¹⁰）、光钟（10⁻¹⁸）仍有 5–10 个数量级。"
     "因此本项目的科研价值不在刷新精度纪录，而在于建立可复现的误差预算方法与双干涉共模抑制方案，"
     "为后续平台升级与工程化应用奠基。")

# ============ 一、背景与意义 ============
heading("一、研究背景与意义", 1)
heading("1.1 从 Ramsey 方法到冷原子干涉仪", 2)
para("Ramsey 于 1949–1950 年提出的分离振荡场方法，用“两段短脉冲 + 中间自由演化 T”取代单段长脉冲，"
     "把谱线宽度压缩到约 1/(2T)，并让原子在自由演化期间脱离光场，从而大幅抑制光频移与功率漂移。"
     "该方法是原子钟、原子干涉仪与量子传感的通用时序骨架。")
para("将两段脉冲扩展为三脉冲（π/2–π–π/2），原子波包在动量空间分开再复合，即构成光脉冲 Mach–Zehnder 干涉仪；"
     "其干涉相位对重力加速度的依赖为 ΔΦ = k_eff·g·T²，其中 780 nm 反向拉曼光的有效波矢 k_eff ≈ 1.61×10⁷ m⁻¹。"
     "Kasevich 与 Chu 于 1991–1992 年首次实现该构型并测量 g，Peters 等 1999 年用自由落体冷原子把相对精度推进到"
     "10⁻⁸ 量级，奠定了现代冷原子重力仪的技术基础。")

heading("1.2 1×10⁻⁸ 精度窗口的定位", 2)
para("以 δg/g ≈ 1×10⁻⁸ 计，相当于 1×10⁻⁷ m/s²（约 10 μGal）。这一水平的“能做/不能做”如下表所示：")
table(["方向", "所需精度", "1×10⁻⁸ 是否够", "说明"],
      [["条纹、线宽、退相干、脉冲工程", "无绝对精度要求", "够", "方法学与机制研究"],
       ["重力仪系统误差预算与抑制", "10⁻⁸~10⁻⁹", "正好", "本项目主战场"],
       ["冷原子重力仪、双干涉共模抑制", "10⁻⁸~10⁻⁹", "入门", "本项目核心内容"],
       ["固体潮观测", "≈10⁻⁸ g", "勉强够", "潮汐峰谷约 2×10⁻⁷ g"],
       ["转台标定、地球自转测量", "10⁻⁶~10⁻⁸ rad/s", "够", "地球自转 7.3×10⁻⁵ rad/s"],
       ["寻北/陀螺罗盘", "10⁻¹⁰ rad/s", "不够", "差 2 个量级"],
       ["等效原理检验", "10⁻¹³~10⁻¹⁵", "不够", "差 5–7 个量级"],
       ["精细结构常数、光钟、洛伦兹检验", "10⁻¹⁰~10⁻¹⁸", "不够", "差 2–10 个量级"]],
      widths=[5.2, 3.2, 2.6, 5.0], caption="表 1  1×10⁻⁸ 精度窗口的能力边界")
para("结论：在 1×10⁻⁸ 平台上，最有价值的研究是“把误差物理讲清楚、把系统集成做出来”，"
     "而不是与纪录级装置比拼绝对精度。")

heading("1.3 科学意义与应用价值", 2)
bullet("方法学意义：系统误差（波前曲率、科里奥利力、拉曼光频移与啁啾、振动）的定量表征与抑制，是可发表、可迁移的物理问题。")
bullet("计量意义：冷原子重力仪是绝对重力基准，可用于标定超导重力仪等相对仪器。")
bullet("地球物理意义：绝对重力测量可观测固体潮、地下水与地壳形变，是地球物理与测地的直接应用。")
bullet("工程与教育意义：平台可支撑“量子惯性传感”教学实验、大学生竞赛（大挑）与后续陀螺/融合研究。")

# ============ 二、现状 ============
heading("二、国内外研究现状", 1)
heading("2.1 冷原子重力仪的发展与代表指标", 2)
table(["工作", "装置/路线", "关键指标或贡献"],
      [["Kasevich & Chu 1992", "光脉冲干涉仪（Na 原子）", "首次测 g，验证 ΔΦ = k_eff g T²"],
       ["Peters, Chung & Chu 1999", "自由落体冷原子", "相对精度 ~10⁻⁸，误差预算范本"],
       ["Le Gouët 等 2008", "紧凑低噪重力仪", "振动、拉曼相位噪声与探测噪声的分解"],
       ["Wu 等 2014", "μGal 级现场重力仪", "灵敏度与系统误差的完整评估"],
       ["Freier 等 2016", "可搬运量子重力仪", "长期稳定度纪录，工程化标杆"],
       ["Bidel 等 2018", "海洋绝对重力测量", "船载动态环境下的振动与姿态控制"],
       ["机载绝对重力 2020", "航空平台", "动态环境下的误差控制"],
       ["Fu 等 2019", "紧凑重力仪参加比对", "真实测量场景下的准确度检验"]],
      widths=[3.8, 4.6, 7.6], caption="表 2  冷原子重力仪代表性工作")

heading("2.2 系统误差研究现状", 2)
para("系统误差是 1×10⁻⁸ 水平的主导限制，国际上的研究脉络可归纳为四条：")
bullet("波前与横向运动：Louchet-Chauvet 等（2011）指出横向运动与拉曼波前曲率耦合产生相位误差；2026 年的时变波前研究进一步把静态图像推广到时间分辨。")
bullet("科里奥利力：Lan 等（2012）系统处理科里奥利相位与补偿；2026 年喷泉重力仪工作给出科里奥利与拉曼束对准的联合解耦。")
bullet("拉曼光频移与啁啾：Cheng 等（2015）分析啁啾拉曼光的相位误差；2025 年工作实现拉曼束倾角变化的在线测量。")
bullet("振动：国内团队发展了振动补偿、噪声分离与车载动态补偿等方法；Junca 等（2026）实现原位空间分辨波前映射，把波前不确定度压到 1 mrad 量级。")

heading("2.3 双干涉仪、共模抑制与梯度测量", 2)
para("双干涉仪差分是抑制共模噪声、分离加速度与转动/梯度的通用手段：Snadden 等（1998）与 McGuirk 等（2002）"
     "用双云构型测量重力梯度；Sorrentino 等（2012）实现 g 与梯度的同时测量；2015 年双种同时干涉仪为等效原理检验"
     "提供共模抑制模板；Gauguet 等（2009）与 Canuel 等（2006）则在 Sagnac 构型中展示了双干涉差分的表征方法与六轴传感。")

heading("2.4 现状判断与研究空白", 2)
para("综合约 450 条文献的调研，可以给出三点判断：")
bullet("重力仪的系统误差研究已相当成熟，但“双干涉仪共模抑制”多以梯度仪、双种干涉或 Sagnac 构型为载体，尚无以其为题的系统研究；")
bullet("1×10⁻⁸ 水平上，振动、波前、科里奥利力与光频移的联合贡献缺少公开的完整误差预算，尤其在紧凑/教学平台上；")
bullet("因此，本项目的切入点是：在自有铷冷原子平台上，建立 1×10⁻⁸ 级重力仪，完成双干涉共模抑制验证与完整误差预算；这既是可发表的仪器/方法学工作，也是大挑与后续陀螺、融合研究的平台底座。")

# ============ 三、目标 ============
heading("三、研究目标与考核指标", 1)
heading("3.1 总体目标", 2)
para("建立 1×10⁻⁸ 级冷原子重力仪实验平台，完成波前、科里奥利力、拉曼光频移与振动四类系统误差的定量表征与抑制，"
     "验证双干涉仪共模抑制方案，形成可复现的误差预算方法学与可移植的实验平台。")
heading("3.2 具体考核指标", 2)
table(["序号", "指标", "目标值", "考核方式"],
      [["1", "单发相对精度 δg/g", "≤1×10⁻⁸（T≥50 ms，N≈10⁶，对比度≥0.3）", "条纹拟合与重复测量"],
       ["2", "双干涉共模抑制比", "≥100（振动 10⁻⁷ g/√Hz → ≤10⁻⁹）", "单/双干涉噪声谱对比"],
       ["3", "系统误差逐项", "波前、科里奥利、光频移、探测均 ≤2×10⁻⁹", "外推/反向/变参数法"],
       ["4", "误差预算闭合", "平方和与实测 Allan 偏差一致（偏差 <30%）", "预算表与 Allan 图对比"],
       ["5", "连续运行", "≥1 h，零偏稳定性 ≤1×10⁻⁸ g/√τ", "连续采集与 Allan 分析"],
       ["6", "延伸（可选）", "固体潮分潮振幅误差 <5%；转台尺度因子标定 <10⁻³", "潮汐拟合、转台比对"]],
      widths=[1.2, 4.4, 6.4, 4.0], caption="表 3  研究考核指标")

# ============ 四、内容 ============
heading("四、研究内容", 1)
heading("4.1 光脉冲干涉仪时序建立与 g 标度验证", 2)
para("搭建 π/2–π–π/2 光脉冲干涉时序，在 T = 30–100 ms 范围内验证 ΔΦ ∝ T²，标定有效波矢 k_eff 与干涉面积；"
     "测量条纹对比度随 T 的衰减，提取相干时间与主要退相干来源。")
heading("4.2 双干涉仪共模抑制", 2)
para("采用反向抛射的两团原子或两套共线干涉仪，共用同一对拉曼光，实现振动等共模噪声的差分抑制；"
     "测量单干涉仪与双干涉仪的相位噪声谱，提取共模抑制比与振动传递函数，并与地震仪前馈方案对比。")
heading("4.3 系统误差测量与抑制", 2)
bullet("波前：平移原子团位置、改变束腰，测量干涉相位与横向位置的关系，拟合波前曲率；采用大束腰/高准直或映射标定（参考 2026 年波前映射工作）。")
bullet("科里奥利力：通过 k 反向、正反抛与倾斜扫描分离科里奥利相位（v=1 m/s、T=0.1 s 时约 23 rad），建立标定流程。")
bullet("拉曼光频移与啁啾：变功率外推零功率截距；对啁啾/频率斜坡做标定与扣除。")
bullet("振动：差分抑制 + 地震仪前馈；用迈克尔逊干涉仪独立测量振动噪声贡献。")
bullet("探测：低饱和成像、原子数归一化与双态参考帧，扣除探测非线性。")
heading("4.4 误差预算与指标实现", 2)
para("逐项测量上述系统误差，建立误差预算表，与实测噪声、Allan 偏差交叉验证，直至预算闭合、指标达标。")
heading("4.5 延伸研究（可选）", 2)
bullet("固体潮观测：连续运行数天，做气压改正与潮汐谐波拟合，与模型/超导重力仪比对。")
bullet("转动传感：转台标定尺度因子，测地球自转分量，探索寻北。")
bullet("传感器融合：以量子传感器为绝对参考，用卡尔曼滤波在线估计 IMU 零偏，量化组合导航改善。")

# ============ 五、技术路线 ============
heading("五、技术路线与实验方案", 1)
heading("5.1 装置组成", 2)
table(["分系统", "现状", "需新增/改造"],
      [["冷原子源（MOT）", "已有（铷 MOT）", "优化装载与关断时序"],
       ["冷却/再泵浦激光", "已有（780 nm）", "提高关断消光比"],
       ["拉曼光路", "无", "相位锁定双光 + AOM/EOM，功率稳定"],
       ["回射镜与隔振", "无", "回射镜、被动隔振平台、倾斜控制"],
       ["磁场控制", "待评估", "三轴线圈 + 磁屏蔽，剩磁 <10 mG"],
       ["探测", "已有（吸收成像）", "低饱和成像与归一化"],
       ["时序与采集", "待搭建", "多通道时序、相机同步、数据管线"]],
      widths=[3.6, 4.2, 7.2], caption="表 4  实验装置分系统")
heading("5.2 时序设计", 2)
para("一个典型周期（约 1.6–2 s）：MOT 装载 1.5 s → 关光与选态（<1 ms）→ 上抛/自由落体 → 拉曼 π/2（10–20 μs）→ "
     "自由演化 T → π → T → π/2 → TOF 成像（1–5 ms）→ 数据处理。T 取 50 ms 与 100 ms 两档。")
heading("5.3 精度预算", 2)
table(["误差项", "量级估计", "对策"],
      [["投影噪声（统计）", "T=50 ms：δΦ≈3.3×10⁻³ rad → δg/g≈8×10⁻⁹（N=10⁶，C=0.3）", "增加原子数/平均时间"],
       ["振动", "地面 10⁻⁷ g/√Hz 量级", "双干涉差分、地震仪前馈"],
       ["波前曲率", "k·r²/(2R)，r=5 mm、R=100 m 时约 2 rad", "大束腰、映射标定、平移原子团"],
       ["科里奥利力", "2k_eff·Ω_E·v·T²，v=1 m/s、T=0.1 s 时约 23 rad", "k 反向、正反抛、倾斜扫描"],
       ["拉曼光频移/啁啾", "随功率与啁啾变化", "变功率外推、啁啾标定"],
       ["探测非线性", "与成像饱和相关", "低饱和、归一化、参考帧"]],
      widths=[3.4, 7.0, 5.0], caption="表 5  1×10⁻⁸ 精度预算（初步）")
heading("5.4 数据处理流程", 2)
para("条纹拟合（含完整脉冲公式）→ 相位解缠与 k 反向组合 → 系统误差外推 → Allan 偏差与误差预算 → 与理论/仿真对比。")

# ============ 六、创新点 ============
heading("六、创新点", 1)
bullet("在 1×10⁻⁸ 平台上建立“双干涉仪共模抑制 + 完整误差预算”的方法学，量化振动—波前—科里奥利—光频移的联合贡献；")
bullet("给出可复现的 1×10⁻⁸ 重力仪实验方案（参数、时序、预算、代码），适配教学实验与竞赛展示；")
bullet("以“误差驱动的工程化”替代“精度纪录”，形成可迁移到原子陀螺与量子—经典融合的通用框架。")

# ============ 七、可行性 ============
heading("七、可行性分析", 1)
bullet("平台基础：铷 MOT、780 nm 激光与吸收成像已具备，主要增量是相位锁定拉曼光路与隔振/磁屏蔽。")
bullet("精度预算可行：T=50 ms、N=10⁶ 时单发统计极限已达 8×10⁻⁹，1×10⁻⁸ 指标有裕量。")
bullet("文献与方法成熟：波前、科里奥利、光频移、振动均有可借鉴的测量与抑制方案（专题 38 篇文献已备全文 28 篇）。")
bullet("风险可控：主要风险为拉曼锁相、波前与振动，均有明确对策与备选方案（见第九节）。")

# ============ 八、计划 ============
heading("八、研究计划与里程碑（12 个月）", 1)
table(["阶段", "时间", "主要任务", "交付物"],
      [["M1", "第 1–2 月", "拉曼双光相位锁定、π/2 脉冲标定、观测拉曼拉比振荡", "拉曼光路与标定报告"],
       ["M2", "第 3–4 月", "π/2–π–π/2 干涉条纹、g 标度验证", "条纹数据与 T² 标度曲线"],
       ["M3", "第 5–6 月", "单/双干涉对比、振动传递函数、共模抑制比", "抑制比 ≥100 的验证"],
       ["M4", "第 7–8 月", "波前、科里奥利、光频移测量与抑制", "各项系统误差曲线"],
       ["M5", "第 9–10 月", "误差预算闭合、1×10⁻⁸ 指标达成", "误差预算表与 Allan 图"],
       ["M6", "第 11–12 月", "连续运行、论文与大挑材料", "论文初稿、竞赛材料"]],
      widths=[1.6, 2.8, 7.2, 4.4], caption="表 6  12 个月研究计划")

# ============ 九、成果与风险 ============
heading("九、预期成果与风险对策", 1)
heading("9.1 预期成果", 2)
bullet("学术论文 1–2 篇：仪器/精密测量类期刊（如 Review of Scientific Instruments、Applied Physics B、IEEE Sensors Journal）或中文核心。")
bullet("实验平台：1×10⁻⁸ 级冷原子重力仪，可复现的时序、控制与数据分析流程。")
bullet("竞赛与教学：大学生竞赛（大挑）实物与数据支撑；冷原子干涉教学实验模块。")
bullet("方法资产：误差预算模板、数据处理代码与文献库（三个专题）。")
heading("9.2 风险与对策", 2)
table(["风险", "影响", "对策"],
      [["拉曼双光锁相不稳", "条纹对比度下降", "共用参考源、拍频锁相、隔振与温控"],
       ["波前曲率超预期", "系统误差主导", "大束腰、波前映射标定、平移原子团"],
       ["振动与倾斜", "相位噪声大", "双干涉差分、地震仪前馈、被动隔振"],
       ["原子数与对比度不足", "统计噪声高", "优化 MOT 装载、低饱和成像、增加重复"],
       ["进度风险", "无法按期达标", "先做 M1–M3 核心指标，延伸内容（潮汐/转动）可裁剪"]],
      widths=[4.2, 4.6, 6.6], caption="表 7  风险与对策")

# ============ 十、文献库 ============
heading("十、文献支撑与资料库", 1)
para("本项目已建立三个独立文献库，覆盖方法、平台、系统误差与工程化：")
table(["文献库", "规模", "全文", "用途"],
      [["Ramsey 干涉仪", "209 条题录", "38 篇", "方法内核、线宽/灵敏度理论、量子增强谱学"],
       ["原子干涉陀螺仪", "209 条题录", "122 篇", "Sagnac 效应、惯性传感、系统误差与工程化"],
       ["B5 冷原子重力仪专题", "38 篇分类清单", "28 篇", "重力仪、双干涉共模抑制、波前/科里奥利/振动"]],
      widths=[4.6, 3.4, 2.4, 6.0], caption="表 8  文献库结构")

# ============ 参考文献 ============
heading("参考文献", 1)
refs = [
 "Kasevich M, Chu S. Measurement of the gravitational acceleration of an atom with a light-pulse atom interferometer. Appl. Phys. B, 1992, 54: 321. doi:10.1007/BF00325375",
 "Peters A, Chung K Y, Chu S. Measurement of gravitational acceleration by dropping atoms. Nature, 1999, 400: 849. doi:10.1038/23655",
 "Snadden M J, McGuirk J M, Bouyer P, et al. Measurement of the Earth's gravity gradient with an atom interferometer-based gravity gradiometer. Phys. Rev. Lett., 1998, 81: 971. doi:10.1103/PhysRevLett.81.971",
 "McGuirk J M, Foster G T, Fixler J B, et al. Sensitive absolute-gravity gradiometry using atom interferometry. Phys. Rev. A, 2002, 65: 033608. doi:10.1103/PhysRevA.65.033608",
 "Le Gouët J, Mehlstäubler T E, Kim J, et al. Limits to the sensitivity of a low noise compact atomic gravimeter. Appl. Phys. B, 2008, 92: 133. doi:10.1007/s00340-008-3088-1",
 "Louchet-Chauvet A, Farah T, Bodart Q, et al. The influence of transverse motion within an atomic gravimeter. New J. Phys., 2011, 13: 065025. doi:10.1088/1367-2630/13/6/065025",
 "Lan S Y, Kuan P C, Estey B, et al. Influence of the Coriolis force in atom interferometry. Phys. Rev. Lett., 2012, 108: 090402. doi:10.1103/PhysRevLett.108.090402",
 "Nobili A M, Anselmi A, Pegna R. Systematic errors in high-precision gravity measurements by light-pulse atom interferometry. Phys. Rev. Research, 2020, 2: 012036. doi:10.1103/PhysRevResearch.2.012036",
 "Cheng B, Gillot P, Merlet S, et al. Influence of chirping the Raman lasers in an atom gravimeter. Phys. Rev. A, 2015, 92: 063617. doi:10.1103/PhysRevA.92.063617",
 "Junca J, Kitching J, McGehee W. Wavefront mapping for absolute atom interferometry. Phys. Rev. Lett., 2026, 136: 143402. doi:10.1103/2c2j-qhkd",
 "Luo Q, et al. De-coupling the Coriolis effect from Raman beams alignment in a fountain atom gravimeter. Rev. Sci. Instrum., 2026, 97: 024501. doi:10.1063/5.0308195",
 "Wavefront curvature and transverse atomic motion in time-resolved atom interferometry. Phys. Rev. Research, 2026, 8. doi:10.1103/sdbr-2whs",
 "Sorrentino F, Pitton A, Bodart Q, et al. Simultaneous measurement of gravity acceleration and gravity gradient with an atom interferometer. Appl. Phys. Lett., 2012, 101: 114106. doi:10.1063/1.4751112",
 "Characterization of a simultaneous dual-species atom interferometer for a quantum test of the weak equivalence principle. Phys. Rev. A, 2015, 92: 023626. doi:10.1103/PhysRevA.92.023626",
 "Gauguet A, Canuel B, Lévèque T, et al. Characterization and limits of a cold-atom Sagnac interferometer. Phys. Rev. A, 2009, 80: 063604. doi:10.1103/PhysRevA.80.063604",
 "Canuel B, Leduc F, Holleville D, et al. Six-axis inertial sensor using cold-atom interferometry. Phys. Rev. Lett., 2006, 97: 010402. doi:10.1103/PhysRevLett.97.010402",
 "Bidel Y, Zahzam N, Blanchard C, et al. Absolute marine gravimetry with matter-wave interferometry. Nat. Commun., 2018, 9: 627. doi:10.1038/s41467-018-03040-2",
 "Freier C, Hauth M, Schkolnik V, et al. Mobile quantum gravity sensor with unprecedented stability. J. Phys. Conf. Ser., 2016, 723: 012050. doi:10.1088/1742-6596/723/1/012050",
 "Absolute airborne gravimetry with a cold atom sensor. J. Geodesy, 2020, 94: 20. doi:10.1007/s00190-020-01350-2",
 "Wu B, et al. The investigation of a μGal-level cold atom gravimeter for field applications. Metrologia, 2014, 51: 452. doi:10.1088/0026-1394/51/5/452",
 "Fu Z, et al. Participation in the absolute gravity comparison with a compact cold atom gravimeter. Chin. Opt. Lett., 2019, 17: 011204. doi:10.3788/col201917.011204",
 "Cronin A D, Schmiedmayer J, Pritchard D E. Optics and interferometry with atoms and molecules. Rev. Mod. Phys., 2009, 81: 1051. doi:10.1103/RevModPhys.81.1051",
 "Degen C L, Reinhard F, Cappellaro P. Quantum sensing. Rev. Mod. Phys., 2017, 89: 035002. doi:10.1103/RevModPhys.89.035002",
 "Abend S, et al. Atom interferometry and its applications. arXiv:2001.10976. doi:10.48550/arXiv.2001.10976",
]
for i, ref in enumerate(refs, 1):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(3)
    pf.line_spacing = 1.2
    pf.left_indent = Pt(21)
    pf.first_line_indent = Pt(-21)
    r = p.add_run("[" + str(i) + "] " + ref)
    run_font(r, size=9)

# ---- 页脚页码 ----
from docx.oxml import OxmlElement

def add_field(par, instr):
    r = par.add_run()
    fld_begin = OxmlElement("w:fldChar"); fld_begin.set(qn("w:fldCharType"), "begin")
    instr_el = OxmlElement("w:instrText"); instr_el.set(qn("xml:space"), "preserve"); instr_el.text = instr
    fld_sep = OxmlElement("w:fldChar"); fld_sep.set(qn("w:fldCharType"), "separate")
    txt = OxmlElement("w:t"); txt.text = "1"
    fld_end = OxmlElement("w:fldChar"); fld_end.set(qn("w:fldCharType"), "end")
    for el in (fld_begin, instr_el, fld_sep, txt, fld_end):
        r._r.append(el)

fp = doc.sections[0].footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r0 = fp.add_run("第 "); run_font(r0, size=9)
add_field(fp, " PAGE ")
r1 = fp.add_run(" 页 / 共 "); run_font(r1, size=9)
add_field(fp, " NUMPAGES ")
r2 = fp.add_run(" 页"); run_font(r2, size=9)

cp_ = doc.core_properties
cp_.title = "冷原子干涉仪精密测量研究说明"
cp_.subject = "1e-8 级冷原子重力仪与双干涉仪共模抑制研究"
cp_.author = "课题组"

out = "E:/My Project/Quantum/Ramsey干涉仪_调研/科研说明/冷原子干涉仪科研说明.docx"
doc.save(out)
print("saved", out)

# -*- coding: utf-8 -*-
"""
Ramsey 干涉条纹与线宽的数值计算 / 绘图
------------------------------------
约定（与 03_理论公式与推导.md 一致）：
  两级系统，驱动场频率 omega，原子跃迁频率 omega0，失谐 delta = omega0 - omega；
  相互作用绘景哈密顿量  H = (hbar/2)[ delta*sigma_z + Omega_R*sigma_x ]，
  自由演化算符  U_free = exp(-i delta T sigma_z/2)。
  两个相同的矩形脉冲，脉宽 tau，拉比频率 Omega_R，有效拉比频率 Omega_eff，
  脉冲面积 theta = Omega_eff*tau。

精确结果（已与 2x2 矩阵直接传播逐点核对，最大偏差 5.6e-16）：
  P(delta) = 4 sin^2(theta/2) * (Omega_R/Omega_eff)^2
             * [ cos(theta/2)cos(delta T/2)
                 - (delta/Omega_eff) sin(theta/2) sin(delta T/2) ]^2

依赖：numpy, Pillow（本机无 matplotlib）。
运行：python tools/ramsey_fringe_plot.py   （在 Ramsey 调研目录下运行）
输出：figures/ramsey_fringes.png + 终端打印关键数值
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

RB87_HF = 6.834682e9  # Hz，87Rb 基态超精细跃迁


def P_ramsey(delta, T, Omega_R, tau):
    """两个相同矩形脉冲之后的上态布居。所有量为 SI 单位（rad/s, s）。"""
    Om = np.sqrt(Omega_R**2 + delta**2)
    th = Om * tau
    s2, c2 = np.sin(th / 2), np.cos(th / 2)
    inner = c2 * np.cos(delta * T / 2) - (delta / Om) * s2 * np.sin(delta * T / 2)
    return 4 * s2**2 * (Omega_R / Om)**2 * inner**2


def _cross(f, lo, hi):
    """在 f(lo)>0 且 f(hi)<0 的区间内二分求根。"""
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fwhm_rad(T, Omega_R, tau):
    """中心条纹半高全宽（rad/s）。"""
    f = lambda x: P_ramsey(x, T, Omega_R, tau) - 0.5
    hi = np.pi / T
    for _ in range(100):
        if f(hi) > 0:
            hi *= 0.5
        else:
            break
    right = _cross(f, 0.0, hi)
    left = _cross(lambda x: f(-x), 0.0, np.pi / T)
    return right + left


def vlabel(img, xy, text, font, fill):
    """把文字旋转 90 度竖排放置（用于纵轴标题）。"""
    tmp = Image.new("RGBA", (1, 1), (255, 255, 255, 0))
    td = ImageDraw.Draw(tmp)
    l, t, r, b = td.textbbox((0, 0), text, font=font)
    w, h = r - l + 8, b - t + 8
    tmp = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    td = ImageDraw.Draw(tmp)
    td.text((4 - l, 4 - t), text, font=font, fill=fill)
    rot = tmp.rotate(90, expand=True)
    img.paste(rot, xy, rot)


def main():
    F_TB = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 34)
    F_T = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 29)
    F_S = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 25)
    F_XS = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 22)

    W, H = 2400, 1020
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    blue, orange, green, grey = (31, 119, 180), (230, 126, 34), (44, 160, 44), (110, 110, 110)

    # ================= 面板 (a)：不同 T 的 Ramsey 条纹 =================
    A = (150, 150, 1150, 830)          # left, top, right, bottom
    aw, ah = A[2] - A[0], A[3] - A[1]
    tau_a = 0.5e-3
    Om_a = (np.pi / 2) / tau_a          # pi/2 脉冲
    xmin, xmax = -250.0, 250.0

    def X(v):
        return A[0] + (v - xmin) / (xmax - xmin) * aw

    def Y(p):
        return A[3] - p * ah

    d.rectangle([A[0], A[1], A[2], A[3]], outline=(60, 60, 60), width=2)
    for f in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = Y(f)
        d.line([A[0], y, A[2], y], fill=(232, 232, 232), width=1)
        d.text((A[0] - 62, y - 13), f"{f:g}", font=F_S, fill=(40, 40, 40))
    for v in range(-250, 251, 50):
        x = X(v)
        d.line([x, A[3], x, A[3] + 12], fill=(60, 60, 60), width=2)
        d.text((x - 26, A[3] + 20), str(v), font=F_S, fill=(40, 40, 40))

    cases = [(10e-3, orange, "T = 10 ms"), (40e-3, green, "T = 40 ms")]
    for T, col, lab in cases:
        ds_hz = np.linspace(xmin, xmax, 8000)
        ps = P_ramsey(ds_hz * 2 * np.pi, T, Om_a, tau_a)
        d.line([(X(v), Y(p)) for v, p in zip(ds_hz, ps)], fill=col, width=3, joint="curve")

    # 图例（白底）
    d.rectangle([A[2] - 330, A[1] + 24, A[2] - 20, A[1] + 150], fill="white", outline=(200, 200, 200))
    for i, (T, col, lab) in enumerate(cases):
        ly = A[1] + 56 + 52 * i
        d.line([A[2] - 300, ly, A[2] - 230, ly], fill=col, width=4)
        d.text((A[2] - 214, ly - 16), lab, font=F_S, fill=col)

    # 条纹参数说明（白底，左下）
    n1 = fwhm_rad(10e-3, Om_a, tau_a) / (2 * np.pi)
    n2 = fwhm_rad(40e-3, Om_a, tau_a) / (2 * np.pi)
    d.rectangle([A[0] + 24, A[3] - 136, A[0] + 470, A[3] - 24], fill="white", outline=(200, 200, 200))
    d.text((A[0] + 40, A[3] - 126), f"T = 10 ms：间距 100 Hz，FWHM = {n1:.1f} Hz", font=F_XS, fill=orange)
    d.text((A[0] + 40, A[3] - 92), f"T = 40 ms：间距 25 Hz，FWHM = {n2:.1f} Hz", font=F_XS, fill=green)
    d.text((A[0] + 40, A[3] - 58), "理想短脉冲极限：FWHM = 1/(2T)", font=F_XS, fill=(90, 90, 90))

    d.text((A[0] + aw / 2 - 190, A[3] + 66), "失谐 \u03b4/2\u03c0  (Hz)", font=F_T, fill=(20, 20, 20))
    vlabel(img, (A[0] - 148, A[1] + int(ah / 2) - 90), "上态布居 P", F_T, (20, 20, 20))
    d.text((A[0], A[1] - 86), "(a)  \u03c0/2 \u2013 \u81ea\u7531\u6f14\u5316 T \u2013 \u03c0/2 \u7684 Ramsey \u6761\u7eb9\uff08\u00b3\u2077Rb\uff0c\u03c4 = 0.5 ms\uff09", font=F_TB, fill=(20, 20, 20))

    # ================= 面板 (b)：有限脉宽对线宽的修正 =================
    B = (1450, 150, 2280, 830)
    bw, bh = B[2] - B[0], B[3] - B[1]
    xr = (0.0, 0.5)      # tau/T
    yr = (0.55, 1.05)    # FWHM / (pi/T)

    def BX(v):
        return B[0] + (v - xr[0]) / (xr[1] - xr[0]) * bw

    def BY(v):
        return B[3] - (v - yr[0]) / (yr[1] - yr[0]) * bh

    d.rectangle([B[0], B[1], B[2], B[3]], outline=(60, 60, 60), width=2)
    for v in [0.55, 0.6, 0.7, 0.8, 0.9, 1.0]:
        y = BY(v)
        d.line([B[0], y, B[2], y], fill=(232, 232, 232), width=1)
        d.text((B[0] - 66, y - 13), f"{v:g}", font=F_S, fill=(40, 40, 40))
    for v in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
        x = BX(v)
        d.line([x, B[3], x, B[3] + 12], fill=(60, 60, 60), width=2)
        d.text((x - 22, B[3] + 20), f"{v:g}", font=F_S, fill=(40, 40, 40))

    d.line([B[0], BY(1.0), B[2], BY(1.0)], fill=grey, width=2)
    d.text((B[0] + bw - 392, BY(1.0) + 14), "理想短脉冲极限（FWHM = \u03c0/T）", font=F_XS, fill=grey)

    ratios = np.linspace(0.005, 0.5, 120)
    pts = []
    T0 = 20e-3
    for r in ratios:
        tau = r * T0
        Om = (np.pi / 2) / tau
        pts.append((BX(r), BY(fwhm_rad(T0, Om, tau) / (np.pi / T0))))
    d.line(pts, fill=blue, width=4, joint="curve")

    # 标注典型点 tau/T = 0.05（本实验的典型值）
    r0 = 0.05
    tau0 = r0 * T0
    Om0 = (np.pi / 2) / tau0
    y0 = fwhm_rad(T0, Om0, tau0) / (np.pi / T0)
    px, py = BX(r0), BY(y0)
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=orange)
    d.text((px + 20, py - 16), f"\u03c4/T = 0.05\uff1a{y0:.3f}", font=F_XS, fill=orange)

    d.text((B[0] + bw / 2 - 150, B[3] + 66), "脉冲宽度比  \u03c4/T", font=F_T, fill=(20, 20, 20))
    d.text((B[0] - 84, B[1] - 86), "(b)  \u6709\u9650\u8109\u5bbd\u5bf9\u4e2d\u5fc3\u6761\u7eb9\u7ebf\u5bbd\u7684\u4fee\u6b63", font=F_TB, fill=(20, 20, 20))
    vlabel(img, (B[0] - 158, B[1] + int(bh / 2) - 110), "中心条纹宽度 / (\u03c0/T)", F_T, (20, 20, 20))

    d.text((W / 2 - 470, 26), "Ramsey \u5206\u79bb\u632f\u8361\u573a\uff1a\u6761\u7eb9\u3001\u7ebf\u5bbd\u4e0e\u6807\u5ea6\u5173\u7cfb", font=F_TB, fill=(10, 10, 10))
    d.text((60, 952), "\u7ea6\u5b9a\uff1a\u03b4 = \u03c9\u2080 \u2212 \u03c9\uff0cH = (\u0127/2)[\u03b4\u03c3z + \u03a9R\u03c3x]\uff1b\u77e9\u5f62 \u03c0/2 \u8109\u51b2\uff1b\u516c\u5f0f\u4e0e\u63a8\u5bfc\u89c1 03_\u7406\u8bba\u516c\u5f0f\u4e0e\u63a8\u5bfc.md",
           font=F_XS, fill=(120, 120, 120))

    img.save("figures/ramsey_fringes.png")
    print("saved figures/ramsey_fringes.png")
    print("T(ms)  间距(Hz)  理想FWHM(Hz)  精确FWHM(Hz)  比值")
    for T in [2e-3, 10e-3, 20e-3, 40e-3]:
        f_hz = fwhm_rad(T, Om_a, tau_a) / (2 * np.pi)
        print(f"{T*1e3:6.1f} {1.0/T:10.1f} {1.0/(2*T):12.1f} {f_hz:12.2f} {f_hz/(1.0/(2*T)):6.3f}")


if __name__ == "__main__":
    main()

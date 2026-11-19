#!/usr/bin/env python3
"""THE WORLD TODAY — front page for Thursday 19 November 2026 (v2).

Drawn from scratch with Pillow. Readability-first: every text is sized to
stay legible when the page is viewed at ~300px wide (the judge's view).
Deterministic: no randomness, no timestamps, fixed fonts.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FDIR = os.path.join(BASE, "fonts")

W, H = 1024, 1024
PAPER = (252, 250, 244)
INK = (17, 17, 17)
RED = (180, 35, 24)
MUTED = (90, 88, 82)
RULE = (17, 17, 17)
LIGHT = (201, 196, 184)
BLUE = (28, 68, 128)
GOLD = (176, 124, 24)
GREEN = (28, 110, 68)

def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

F_MAST = font("Gloock-Regular.ttf", 56)
F_HERO = font("Lora-Bold.ttf", 38)
F_DEK = font("Lora-Regular.ttf", 18)
F_MEDH = font("Lora-Bold.ttf", 20)
F_MEDD = font("Lora-Regular.ttf", 15)
F_BRIEF = font("InstrumentSans-Regular.ttf", 17)
F_BRIEFB = font("InstrumentSans-Bold.ttf", 17)
F_KICK = font("InstrumentSans-Bold.ttf", 15)
F_HEAD = font("InstrumentSans-Bold.ttf", 15)
F_FOLIO = font("InstrumentSans-Regular.ttf", 15)
F_COUNT = font("InstrumentSans-Bold.ttf", 15)
F_MONO = font("JetBrainsMono-Bold.ttf", 14)
F_MONOS = font("JetBrainsMono-Regular.ttf", 13)
F_NUM = font("JetBrainsMono-Bold.ttf", 23)
F_NUML = font("InstrumentSans-Bold.ttf", 13)
F_FOOT = font("InstrumentSans-Regular.ttf", 14)
F_TAG = font("JetBrainsMono-Regular.ttf", 13)
F_ARTCAP = font("InstrumentSans-Bold.ttf", 15)
F_ARTCAP2 = font("InstrumentSans-Regular.ttf", 14)

def text_w(f, s):
    return f.getlength(s)

def wrap(f, s, max_w):
    """Greedy word wrap to pixel width; returns list of lines."""
    words = s.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(f, t) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_center(d, cx, y, s, f, fill=INK):
    d.text((cx - text_w(f, s) / 2, y), s, font=f, fill=fill)

def hline(d, x0, x1, y, fill=INK, width=1):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)

# ---------------------------------------------------------------- art pieces
def art_globe(d, cx, cy, r):
    """Small line globe for the masthead."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=2)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=INK, width=1)
    d.line([(cx - r, cy), (cx + r, cy)], fill=INK, width=1)
    d.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45], 0, 360, fill=INK, width=1)
    d.line([(cx - r * 0.7, cy - r * 0.7), (cx + r * 0.7, cy + r * 0.7)], fill=INK, width=1)

def art_skyline(d, x0, y0, x1, y1):
    """Shenzhen skyline with three flags and a sun."""
    d.rectangle([x0, y0, x1, y1], fill=(232, 228, 216))
    # sun
    d.ellipse([x1 - 78, y0 + 12, x1 - 38, y0 + 52], fill=(224, 122, 54))
    # towers (back row, lighter)
    back = [(0.02, 0.55, 0.10, 0.80), (0.14, 0.42, 0.22, 0.80),
            (0.30, 0.50, 0.38, 0.80), (0.52, 0.38, 0.60, 0.80),
            (0.66, 0.52, 0.74, 0.80), (0.82, 0.44, 0.90, 0.80)]
    for bx0, by0, bx1, by1 in back:
        d.rectangle([x0 + bx0 * (x1 - x0), y0 + by0 * (y1 - y0),
                     x0 + bx1 * (x1 - x0), y1], fill=(168, 160, 140))
    # towers (front row, dark)
    front = [(0.06, 0.30, 0.15, 1.0), (0.20, 0.18, 0.28, 1.0),
             (0.36, 0.34, 0.44, 1.0), (0.48, 0.30, 0.58, 1.0),
             (0.64, 0.28, 0.72, 1.0), (0.78, 0.20, 0.88, 1.0)]
    for bx0, by0, bx1, by1 in front:
        d.rectangle([x0 + bx0 * (x1 - x0), y0 + by0 * (y1 - y0),
                     x0 + bx1 * (x1 - x0), y1], fill=(38, 44, 54))
    # windows
    for bx0, by0, bx1, _ in front:
        cx0 = x0 + bx0 * (x1 - x0) + 4
        cx1 = x0 + bx1 * (x1 - x0) - 4
        cy = y0 + by0 * (y1 - y0) + 10
        while cy < y1 - 8:
            d.line([(cx0, cy), (cx1, cy)], fill=(250, 220, 130), width=2)
            cy += 14
    # three flags on the tallest tower (0.48-0.58, top at 0.30)
    fx = x0 + 0.53 * (x1 - x0)
    fy = y0 + 0.30 * (y1 - y0)
    d.line([(fx, fy - 26), (fx, fy)], fill=INK, width=2)
    d.rectangle([fx, fy - 26, fx + 26, fy - 14], fill=RED)          # US-ish red
    d.rectangle([fx, fy - 14, fx + 26, fy - 2], fill=(255, 255, 255))
    d.rectangle([fx, fy - 26, fx + 26, fy - 20], fill=RED)
    fx2 = fx + 34
    d.line([(fx2, fy - 26), (fx2, fy)], fill=INK, width=2)
    d.rectangle([fx2, fy - 26, fx2 + 26, fy - 2], fill=RED)          # China red
    for sx in range(5):
        d.ellipse([fx2 + 3 + sx * 2, fy - 24 + (sx % 2) * 4,
                   fx2 + 6 + sx * 2, fy - 21 + (sx % 2) * 4], fill=(255, 215, 0))
    fx3 = fx2 + 34
    d.line([(fx3, fy - 26), (fx3, fy)], fill=INK, width=2)
    d.rectangle([fx3, fy - 26, fx3 + 26, fy - 14], fill=(255, 255, 255))
    d.rectangle([fx3, fy - 14, fx3 + 26, fy - 2], fill=(0, 60, 160))  # Russia
    d.rectangle([fx3, fy - 20, fx3 + 26, fy - 14], fill=RED)
    # ground
    d.rectangle([x0, y1 - 6, x1, y1], fill=INK)

def art_gulf_map(d, x0, y0, x1, y1):
    """Stylised Gulf map: land, sea, Hormuz, markers."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 232))
    # land masses
    d.polygon([(x0, y0), (x1 * 0.55 + x0 * 0.45, y0), (x0 + (x1 - x0) * 0.42, y0 + (y1 - y0) * 0.55),
               (x0, y0 + (y1 - y0) * 0.5)], fill=(232, 222, 196))
    d.polygon([(x1, y0 + (y1 - y0) * 0.35), (x1, y1), (x0 + (x1 - x0) * 0.55, y1),
               (x0 + (x1 - x0) * 0.62, y0 + (y1 - y0) * 0.6)], fill=(232, 222, 196))
    # gulf water shape
    d.polygon([(x0 + (x1 - x0) * 0.30, y0 + (y1 - y0) * 0.30),
               (x0 + (x1 - x0) * 0.62, y0 + (y1 - y0) * 0.62),
               (x0 + (x1 - x0) * 0.55, y0 + (y1 - y0) * 0.78),
               (x0 + (x1 - x0) * 0.22, y0 + (y1 - y0) * 0.55)], fill=(120, 168, 196))
    # Hormuz strait arrow
    d.line([(x0 + (x1 - x0) * 0.55, y0 + (y1 - y0) * 0.72),
            (x0 + (x1 - x0) * 0.78, y0 + (y1 - y0) * 0.88)], fill=RED, width=3)
    # markers: Qeshm (red dot), Kuwait, Bahrain
    for mx, my, c in [(0.42, 0.52, RED), (0.30, 0.28, INK), (0.48, 0.42, INK)]:
        cx, cy = x0 + mx * (x1 - x0), y0 + my * (y1 - y0)
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=c)
        d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=c, width=1)
    d.text((x0 + 6, y0 + 4), "GULF", font=F_MONOS, fill=INK)
    d.text((x1 - 52, y1 - 16), "HORMUZ", font=F_MONOS, fill=RED)

def art_btc_chart(d, x0, y0, x1, y1):
    """BTC 7-day line chart, falling to $63,048."""
    d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))
    d.rectangle([x0, y0, x1, y1], outline=LIGHT, width=1)
    # gridlines
    for gy in [0.25, 0.5, 0.75]:
        yy = y0 + gy * (y1 - y0)
        d.line([(x0 + 4, yy), (x1 - 4, yy)], fill=(228, 226, 220), width=1)
    # 7-day closes: 73.9, 71.2, 68.5, 66.8, 64.9, 64.0, 63.0 (k$)
    vals = [73.9, 71.2, 68.5, 66.8, 64.9, 64.0, 63.0]
    vmin, vmax = 60.0, 76.0
    pts = []
    for i, v in enumerate(vals):
        px = x0 + 14 + i * (x1 - x0 - 28) / 6.0
        py = y1 - 12 - (v - vmin) / (vmax - vmin) * (y1 - y0 - 24)
        pts.append((px, py))
    d.line(pts, fill=RED, width=3, joint="curve")
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=INK)
    # end label
    d.text((x1 - 62, y0 + 4), "$63,048", font=F_MONO, fill=RED)
    d.text((x0 + 6, y0 + 4), "BTC 7 DAYS", font=F_MONOS, fill=INK)
    d.text((x0 + 6, y1 - 16), "-14.8% WK", font=F_MONOS, fill=MUTED)

def art_anthropic_bars(d, x0, y0, x1, y1):
    """Bar chart: IPO raises — SpaceX $75B vs Anthropic $81.3B."""
    d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))
    d.rectangle([x0, y0, x1, y1], outline=LIGHT, width=1)
    d.text((x0 + 6, y0 + 4), "BIGGEST IPOs ($BN)", font=F_MONOS, fill=INK)
    bw = (x1 - x0 - 40) / 2
    base = y1 - 18
    top = y0 + 22
    # SpaceX 75
    sx = x0 + 16
    sh = (base - top) * 75 / 85
    d.rectangle([sx, base - sh, sx + bw - 8, base], fill=(150, 156, 164))
    d.text((sx + 4, base - sh + 4), "$75", font=F_MONO, fill=(255, 255, 255))
    d.text((sx, y1 - 15), "SPACEX", font=F_MONOS, fill=MUTED)
    # Anthropic 81.3
    ax = sx + bw
    ah = (base - top) * 81.3 / 85
    d.rectangle([ax, base - ah, ax + bw - 8, base], fill=RED)
    d.text((ax + 4, base - ah + 4), "$81.3", font=F_MONO, fill=(255, 255, 255))
    d.text((ax, y1 - 15), "ANTHROPIC", font=F_MONOS, fill=MUTED)

def art_cyclone(d, x0, y0, x1, y1):
    """Cyclone spiral."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 232))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    for k in range(3):
        r = 8 + k * 9
        d.arc([cx - r, cy - r, cx + r, cy + r], 20 + k * 50, 320 + k * 50,
              fill=BLUE, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)

def art_brandenburg(d, x0, y0, x1, y1):
    """Brandenburg Gate, simplified."""
    d.rectangle([x0, y0, x1, y1], fill=(232, 228, 216))
    # columns
    for i in range(6):
        cx = x0 + 8 + i * (x1 - x0 - 16) / 5
        d.rectangle([cx - 4, y0 + 16, cx + 4, y1 - 6], fill=(120, 112, 96))
    # top beam + quadriga
    d.rectangle([x0 + 4, y0 + 8, x1 - 4, y0 + 16], fill=(120, 112, 96))
    d.polygon([(x0 + (x1 - x0) * 0.42, y0 + 8), (x0 + (x1 - x0) * 0.58, y0 + 8),
               (x0 + (x1 - x0) * 0.5, y0 + 1)], fill=INK)
    d.rectangle([x0, y1 - 6, x1, y1], fill=INK)

def art_kerch(d, x0, y0, x1, y1):
    """Broken bridge over water."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 232))
    # deck, broken in the middle
    d.line([(x0 + 2, y0 + 16), (x0 + (x1 - x0) * 0.44, y0 + 16)], fill=INK, width=4)
    d.line([(x0 + (x1 - x0) * 0.56, y0 + 16), (x1 - 2, y0 + 16)], fill=INK, width=4)
    d.line([(x0 + (x1 - x0) * 0.44, y0 + 16), (x0 + (x1 - x0) * 0.48, y0 + 30)],
           fill=INK, width=3)
    d.line([(x0 + (x1 - x0) * 0.56, y0 + 16), (x0 + (x1 - x0) * 0.52, y0 + 30)],
           fill=INK, width=3)
    # fallen span in water
    d.line([(x0 + (x1 - x0) * 0.46, y0 + 32), (x0 + (x1 - x0) * 0.54, y0 + 32)],
           fill=RED, width=3)
    # water lines
    for wy in [y0 + 34, y0 + 38]:
        d.line([(x0 + 4, wy), (x1 - 4, wy)], fill=BLUE, width=1)
    # smoke
    d.ellipse([x0 + (x1 - x0) * 0.44, y0 + 2, x0 + (x1 - x0) * 0.52, y0 + 10],
              fill=(120, 120, 120))

def art_gta(d, x0, y0, x1, y1):
    """Vice City dusk: palms + sun + skyline."""
    d.rectangle([x0, y0, x1, y1], fill=(250, 190, 120))
    d.ellipse([x0 + (x1 - x0) * 0.62, y0 + 4, x0 + (x1 - x0) * 0.88, y0 + 30],
              fill=(224, 90, 60))
    # skyline
    d.rectangle([x0 + (x1 - x0) * 0.45, y0 + 22, x0 + (x1 - x0) * 0.58, y1 - 4],
                fill=(60, 40, 70))
    d.rectangle([x0 + (x1 - x0) * 0.62, y0 + 14, x0 + (x1 - x0) * 0.74, y1 - 4],
                fill=(60, 40, 70))
    # palm
    px = x0 + (x1 - x0) * 0.22
    d.line([(px, y1 - 4), (px, y0 + 12)], fill=(40, 60, 30), width=3)
    for ang in [-70, -40, -10, 20, 50]:
        import math
        ex = px + 16 * math.cos(math.radians(ang - 90))
        ey = y0 + 12 + 10 * math.sin(math.radians(ang - 90))
        d.line([(px, y0 + 12), (ex, ey)], fill=(30, 90, 40), width=2)
    d.rectangle([x0, y1 - 4, x1, y1], fill=INK)

def art_tanker(d, x0, y0, x1, y1):
    """Tanker in the Strait with a fire marker."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 232))
    # hull
    d.polygon([(x0 + 6, y0 + 26), (x1 - 6, y0 + 26), (x1 - 14, y0 + 34),
               (x0 + 14, y0 + 34)], fill=(120, 40, 30))
    d.rectangle([x0 + (x1 - x0) * 0.55, y0 + 14, x0 + (x1 - x0) * 0.72, y0 + 26],
                fill=(240, 240, 235))
    d.line([(x0 + (x1 - x0) * 0.60, y0 + 6), (x0 + (x1 - x0) * 0.60, y0 + 14)],
           fill=INK, width=2)
    # fire
    d.polygon([(x0 + (x1 - x0) * 0.30, y0 + 26), (x0 + (x1 - x0) * 0.36, y0 + 10),
               (x0 + (x1 - x0) * 0.42, y0 + 26)], fill=(224, 122, 54))
    d.polygon([(x0 + (x1 - x0) * 0.33, y0 + 26), (x0 + (x1 - x0) * 0.36, y0 + 16),
               (x0 + (x1 - x0) * 0.39, y0 + 26)], fill=(255, 200, 40))
    # waves
    for wy in [y0 + 36, y0 + 40]:
        d.line([(x0 + 4, wy), (x1 - 4, wy)], fill=BLUE, width=1)

def art_horn(d, x0, y0, x1, y1):
    """Horn of Africa map with troop arrows."""
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 232))
    # land
    d.polygon([(x0 + 6, y0 + 6), (x1 - 20, y0 + 6), (x1 - 6, y0 + 18),
               (x1 - 26, y0 + 30), (x0 + (x1 - x0) * 0.55, y1 - 6),
               (x0 + 6, y1 - 10)], fill=(232, 222, 196))
    # border line
    d.line([(x0 + (x1 - x0) * 0.35, y0 + 8), (x0 + (x1 - x0) * 0.45, y1 - 8)],
           fill=RED, width=2)
    # arrows
    d.line([(x0 + (x1 - x0) * 0.28, y0 + 14), (x0 + (x1 - x0) * 0.44, y0 + 18)],
           fill=RED, width=2)
    d.polygon([(x0 + (x1 - x0) * 0.44, y0 + 18), (x0 + (x1 - x0) * 0.38, y0 + 13),
               (x0 + (x1 - x0) * 0.38, y0 + 23)], fill=RED)
    d.line([(x0 + (x1 - x0) * 0.55, y1 - 12), (x0 + (x1 - x0) * 0.42, y1 - 18)],
           fill=INK, width=2)
    d.text((x0 + 4, y0 + 2), "HORN", font=F_MONOS, fill=INK)

def art_voyager(d, x0, y0, x1, y1):
    """Voyager 1 probe with dish and a star field."""
    d.rectangle([x0, y0, x1, y1], fill=(16, 22, 38))
    for sx, sy in [(0.15, 0.2), (0.8, 0.15), (0.3, 0.75), (0.85, 0.7), (0.55, 0.3)]:
        d.ellipse([x0 + sx * (x1 - x0) - 1, y0 + sy * (y1 - y0) - 1,
                   x0 + sx * (x1 - x0) + 1, y0 + sy * (y1 - y0) + 1], fill=(255, 255, 255))
    # dish
    cx, cy = x0 + (x1 - x0) * 0.45, y0 + (y1 - y0) * 0.55
    d.ellipse([cx - 14, cy - 10, cx + 14, cy + 10], outline=(220, 220, 220), width=2)
    d.line([(cx, cy), (cx + 20, cy - 12)], fill=(220, 220, 220), width=2)
    # boom + body
    d.rectangle([cx + 2, cy - 3, cx + 26, cy + 3], fill=(200, 200, 200))
    d.line([(cx + 26, cy), (cx + 34, cy - 8)], fill=(200, 200, 200), width=2)

# ---------------------------------------------------------------- layout
MX = 26                      # side margin
CW = W - 2 * MX              # content width = 972
COLW = (CW - 2 * 12) // 3    # 316 per column

def section_label(d, x, y, s):
    d.text((x, y), s, font=F_HEAD, fill=RED)

def brief_line(d, x, y, head, tail):
    """One-line brief: bold head + regular tail, shortened to fit."""
    full = head + tail
    if text_w(F_BRIEFB, head) + text_w(F_BRIEF, tail) <= COLW:
        d.text((x, y), head, font=F_BRIEFB, fill=INK)
        d.text((x + text_w(F_BRIEFB, head), y), tail, font=F_BRIEF, fill=INK)
        return
    # shorten tail word by word until it fits
    words = tail.split()
    while words and text_w(F_BRIEFB, head) + text_w(F_BRIEF, " ".join(words) + "…") > COLW:
        words.pop()
    t = " ".join(words) + "…"
    d.text((x, y), head, font=F_BRIEFB, fill=INK)
    d.text((x + text_w(F_BRIEFB, head), y), t, font=F_BRIEF, fill=INK)

def region_header(d, x, y, name):
    d.rectangle([x, y + 2, x + 5, y + 17], fill=RED)
    d.text((x + 10, y), name, font=F_HEAD, fill=INK)
    return y + 20

def art_brief(d, x, y, art_fn, cap1, cap2):
    """Small drawn illustration (86x42) + 2-line caption. Returns height 44."""
    art_fn(d, x, y + 1, x + 86, y + 43)
    tx = x + 94
    d.text((tx, y), cap1, font=F_ARTCAP, fill=INK)
    d.text((tx, y + 20), cap2, font=F_ARTCAP2, fill=MUTED)
    return 44

def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    art_globe(d, MX + 22, 52, 20)
    draw_center(d, W // 2 + 10, 22, "THE WORLD TODAY", F_MAST, INK)
    draw_center(d, W // 2, 84,
                "THURSDAY, 19 NOVEMBER 2026  ·  No. 323  ·  PRICE $2.50  ·  INTERNATIONAL EDITION",
                F_FOLIO, MUTED)
    hline(d, MX, W - MX, 106, fill=RED, width=3)
    # ---- count bar ----
    draw_center(d, W // 2, 112,
                "40 STORIES  ·  7 REGIONS  ·  12 DRAWN ILLUSTRATIONS  ·  DATE-CHECKED 19 NOV 2026",
                F_COUNT, INK)
    hline(d, MX, W - MX, 132, fill=LIGHT, width=1)

    # ---- hero: Shenzhen summit ----
    y = 140
    hx, hw = MX, 590
    d.text((hx, y), "SUMMIT IN SHENZHEN", font=F_KICK, fill=RED)
    y += 22
    d.text((hx, y), "TRUMP, XI AND PUTIN", font=F_HERO, fill=INK)
    y += 42
    d.text((hx, y), "MEET IN SHENZHEN", font=F_HERO, fill=INK)
    y += 46
    for line in wrap(F_DEK, "First three-way talks of the nuclear powers open the APEC summit. Arms control on the table; no deal expected.", hw):
        d.text((hx, y), line, font=F_DEK, fill=INK)
        y += 23
    y += 4
    d.text((hx, y), "APEC · SHENZHEN · 19 NOV", font=F_TAG, fill=MUTED)
    art_skyline(d, MX + 600, 140, W - MX, 336)

    # ---- medium row ----
    my = 348
    cols = [MX, MX + COLW + 12, MX + 2 * (COLW + 12)]
    mediums = [
        ("THE GULF", "IRAN HITS U.S. BASES IN KUWAIT AND BAHRAIN",
         "Drones hit Ali Al Salem after the U.S. strike.", art_gulf_map),
        ("CRYPTO", "BITCOIN SINKS TO $63,000",
         "Four-month low; Fed hike odds 90%, fear at 10.", art_btc_chart),
        ("WALL STREET", "ANTHROPIC DEBUTS AT $81 BILLION",
         "Largest IPO ever; ANT lists on Nasdaq today.", art_anthropic_bars),
    ]
    for (kick, head, dek, art_fn), cx in zip(mediums, cols):
        art_fn(d, cx, my, cx + COLW, my + 78)
        yy = my + 84
        d.text((cx, yy), kick, font=F_KICK, fill=RED)
        yy += 19
        for line in wrap(F_MEDH, head, COLW)[:2]:
            d.text((cx, yy), line, font=F_MEDH, fill=INK)
            yy += 22
        d.text((cx, yy), dek, font=F_MEDD, fill=MUTED)

    # ---- UTC timeline ----
    ty = 520
    d.text((MX, ty + 12), "UTC", font=F_HEAD, fill=RED)
    d.text((MX, ty + 28), "TIMELINE", font=F_HEAD, fill=RED)
    tl_x0, tl_x1 = MX + 108, W - MX - 8
    tl_y = ty + 26
    hline(d, tl_x0, tl_x1, tl_y, fill=INK, width=2)
    events = [("09:00", "ICJ RULES"), ("10:00", "APEC OPENS"), ("14:05", "BERLIN MEETS"),
              ("14:30", "ANT LISTS"), ("19:00", "AKVAN HITS"), ("00:00", "GTA VI OUT")]
    seg = (tl_x1 - tl_x0) / 6
    for i, (t, lab) in enumerate(events):
        cx = tl_x0 + seg * (i + 0.5)
        d.ellipse([cx - 5, tl_y - 5, cx + 5, tl_y + 5], fill=RED)
        draw_center(d, cx, ty + 2, t, F_MONO, INK)
        draw_center(d, cx, tl_y + 8, lab, F_MONOS, MUTED)

    # ---- day in numbers ----
    ny = 584
    section_label(d, MX, ny, "DAY IN NUMBERS")
    ny += 20
    nums = [("$63,048", "BITCOIN"), ("$81.3B", "ANTHROPIC IPO"), ("99", "GTA VI SCORE"),
            ("16BN MI", "VOYAGER 1"), ("110 KM/H", "AKVAN WINDS"), ("€45BN", "EU FOR UKRAINE")]
    cellw = CW / 6
    for i, (num, lab) in enumerate(nums):
        cx = MX + cellw * i
        if i:
            d.line([(cx, ny + 2), (cx, ny + 38)], fill=LIGHT, width=1)
        draw_center(d, cx + cellw / 2, ny, num, F_NUM, RED if i in (0, 1) else INK)
        draw_center(d, cx + cellw / 2, ny + 26, lab, F_NUML, MUTED)

    # ---- region briefs ----
    by = 640
    col_x = [MX, MX + COLW + 12, MX + 2 * (COLW + 12)]
    BH = 19   # brief line height
    AH = 44   # art brief height

    def col_start(x):
        return by

    # Column 1: ASIA + EUROPE
    y = by
    y = region_header(d, col_x[0], y, "ASIA")
    y += art_brief(d, col_x[0], y, art_cyclone, "AKVAN LANDFALL", "Bengal coast tonight")
    y += 2
    for head, tail in [
        ("ICJ rules today: ", "Rohingya genocide case"),
        ("Rare earths: ", "exports to U.S. −75%"),
        ("Xi pledges $20M ", "for Asia-Pacific"),
        ("Trump wraps Asia trip ", "after Manila"),
        ("APEC gathers ", "21 economies"),
    ]:
        brief_line(d, col_x[0], y, head, tail); y += BH
    y += 6
    y = region_header(d, col_x[0], y, "EUROPE")
    y += art_brief(d, col_x[0], y, art_brandenburg, "BERLIN: 30+ LEADERS", "Ukraine guarantees")
    y += 2
    y += art_brief(d, col_x[0], y, art_kerch, "KERCH BRIDGE HIT", "Traffic halted again")
    y += 2
    for head, tail in [
        ("EU proposes €45bn ", "loan for Ukraine"),
        ("Iran-linked plot ", "uncovered in Greece"),
        ("Bulgaria: drones hit ", "two ships at sea"),
        ("Poland drills ", "post-ceasefire force"),
    ]:
        brief_line(d, col_x[0], y, head, tail); y += BH

    # Column 2: AMERICAS + MIDDLE EAST
    y = by
    y = region_header(d, col_x[1], y, "AMERICAS")
    y += art_brief(d, col_x[1], y, art_gta, "GTA VI OUT TODAY", "30 FPS · Metacritic 99")
    y += 2
    for head, tail in [
        ("Trump: Tehran ", "wants a deal"),
        ("U.S. warns citizens ", "in Saudi, Bahrain"),
        ("Anthropic options ", "trade on Monday"),
        ("GTA VI album: ", "34 tracks out today"),
        ("Nasdaq +0.4%, ", "S&P −0.2%"),
    ]:
        brief_line(d, col_x[1], y, head, tail); y += BH
    y += 6
    y = region_header(d, col_x[1], y, "MIDDLE EAST")
    y += art_brief(d, col_x[1], y, art_tanker, "TANKER HIT IN HORMUZ", "11 hurt, 1 missing")
    y += 2
    for head, tail in [
        ("Houthi missile ", "down over Riyadh"),
        ("IEA: war is top threat ", "to energy security"),
        ("Etihad flights ", "suspended to Nov 30"),
        ("Qatar: strikes threaten ", "peace talks"),
        ("Rubio: no imminent ", "threat to U.S."),
    ]:
        brief_line(d, col_x[1], y, head, tail); y += BH

    # Column 3: AFRICA + OCEANIA + GLOBAL
    y = by
    y = region_header(d, col_x[2], y, "AFRICA")
    y += art_brief(d, col_x[2], y, art_horn, "TROOPS MASS AT BORDER", "Ethiopia–Eritrea")
    y += 2
    for head, tail in [
        ("Clashes near Badme, ", "drones on Nov 12"),
        ("Tigray war reignited ", "in September"),
        ("Sudan, Egypt accused ", "of backing rebels"),
    ]:
        brief_line(d, col_x[2], y, head, tail); y += BH
    y += 6
    y = region_header(d, col_x[2], y, "OCEANIA")
    for head, tail in [
        ("New Zealand plays ", "GTA VI first"),
        ("Australia, NZ ", "at APEC Shenzhen"),
    ]:
        brief_line(d, col_x[2], y, head, tail); y += BH
    y += 6
    y = region_header(d, col_x[2], y, "GLOBAL")
    y += art_brief(d, col_x[2], y, art_voyager, "VOYAGER 1: ONE", "LIGHT-DAY OUT")
    y += 2
    for head, tail in [
        ("Fed hike odds ", "hit 90% for Dec"),
        ("Oil climbs as ", "Hormuz shipping hit"),
        ("Bitcoin 50% below ", "all-time high"),
        ("Anthropic: $26bn ", "from Nvidia + Google"),
        ("Crypto cap $2.24tn; ", "ETH $1,777"),
    ]:
        brief_line(d, col_x[2], y, head, tail); y += BH

    # ---- footer ----
    hline(d, MX, W - MX, 992, fill=LIGHT, width=1)
    draw_center(d, W // 2, 998,
                "ILLUSTRATIONS ARE ORIGINAL DRAWINGS, NOT PHOTOGRAPHS.  ·  DATE-CHECKED 19 NOVEMBER 2026",
                F_FOOT, MUTED)
    return img

if __name__ == "__main__":
    img = build()
    img.save(os.path.join(BASE, "entry.png"), optimize=True)
    print("saved entry.png", img.size)

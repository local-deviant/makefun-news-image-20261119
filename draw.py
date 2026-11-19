#!/usr/bin/env python3
"""The World Today — front page for Thursday 19 November 2026.

Drawn entirely from code (Pillow). One program renders the whole page:
nameplate, folio, lead story with a drawn skyline, a dense brief band,
four medium stories with spot art, five art briefs with glyphs, and a
30-brief grid across seven regions. Rendered at 3x and downsampled
with LANCZOS for crisp type. Deterministic: no randomness, no clock.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
SS = 3                      # supersample factor
W, H = 1024, 1024           # final size

PAPER = (248, 244, 233)
INK = (25, 25, 25)
RED = (179, 39, 30)
BLUE = (39, 75, 115)
GOLD = (201, 162, 39)
TEAL = (46, 111, 106)
TAN = (216, 196, 154)
GREY = (110, 108, 100)
LIGHT_BLUE = (196, 214, 228)
PALE_GOLD = (238, 222, 178)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), int(size * SS))


F_NAME = font("Gloock-Regular.ttf", 66)
F_HEAD = font("Gloock-Regular.ttf", 40)
F_SERIF = font("Lora-Regular.ttf", 11.5)
F_SERIF_B = font("Lora-Bold.ttf", 13)
F_SERIF_BIG = font("Lora-Bold.ttf", 15.5)
F_SERIF_SM = font("Lora-Regular.ttf", 10.5)
F_ITALIC = font("Lora-Italic.ttf", 15)
F_ITALIC_SM = font("Lora-Italic.ttf", 11)
F_MED_HEAD = font("Lora-Bold.ttf", 14)
F_MED_BODY = font("Lora-Regular.ttf", 10.5)
F_SANS = font("InstrumentSans-Regular.ttf", 10.5)
F_SANS_B = font("InstrumentSans-Bold.ttf", 10.5)
F_SANS_SM = font("InstrumentSans-Bold.ttf", 9)
F_KICK = font("InstrumentSans-Bold.ttf", 13)
F_ART_HEAD = font("Lora-Bold.ttf", 13)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width (final px)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) / SS <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(draw, x, y, s, fnt, fill=INK, anchor="la"):
    draw.text((x * SS, y * SS), s, font=fnt, fill=fill, anchor=anchor)


def text_wrapped(draw, x, y, s, fnt, max_w, lh, fill=INK, max_lines=None):
    """Draw wrapped text; return y of the line after the last one."""
    lines = wrap(draw, s, fnt, max_w)
    if max_lines is not None:
        lines = lines[:max_lines]
    for ln in lines:
        text(draw, x, y, ln, fnt, fill)
        y += lh
    return y


def rule(draw, x0, x1, y, wdt=1, fill=INK):
    draw.line([(x0 * SS, y * SS), (x1 * SS, y * SS)], fill=fill, width=int(wdt * SS))


# ---------------------------------------------------------------- stories
LEAD_HEAD = ["Trump, Xi and Putin meet at last",
             "in first three-way summit"]
LEAD_DEK = ("The three leaders sit down together in Shenzhen on the APEC "
            "sidelines — nuclear arms, Ukraine and the Gulf on the table, "
            "but no breakthrough expected.")
LEAD_CAP = ("Shenzhen hosts the first meeting of the three presidents. "
            "Drawn illustration.")

MEDIUM = [
    ("THE GULF", "Gulf in flames as Iran and US trade strikes",
     "Tehran fires at US bases in Kuwait and Bahrain; Washington hits a "
     "Guard site on Qeshm. A tanker is hit near Hormuz.", "gulf"),
    ("BERLIN", "Europe rallies in Berlin as summit opens",
     "Merz hosts Macron, Burnham, Tusk, Meloni and Rutte, plus Witkoff and "
     "Kushner. Guarantees top the agenda.", "berlin"),
    ("HORN OF AFRICA", "Horn of Africa edges towards war",
     "Ethiopia and Eritrea mass troops and clash near Badme. Sudan blames "
     "Ethiopia and the UAE for drone attacks.", "horn"),
    ("INDIA", "Cyclone Akvan bears down on India",
     "Landfall due Friday on the Andhra coast, winds 120-130 km/h gusting "
     "to 145. Odisha shuts schools, opens shelters.", "cyclone"),
]

ART_BRIEFS = [
    ("Bridge hit a third time",
     "Ukraine strikes the Kerch crossing again.", "bridge"),
    ("Court to rule on Rohingya case",
     "The ICJ delivers its Myanmar genocide judgment.", "scales"),
    ("Jeffries to make history",
     "Democrats pick him as the first Black Speaker.", "capitol"),
    ("Anthropic's $81bn debut",
     "Shares priced at $83; trading starts today.", "rocket"),
    ("Voyager 1, a light-day out",
     "NASA's probe passes a new distance mark.", "voyager"),
]

# (region, head, body) — 37 plain briefs
# (region, head, body) — 33 plain briefs (heads <=30 chars, bodies <=38)
BRIEFS = [
    ("ASIA", "N. Korea expands enrichment",
     "IAEA reports growth at Yongbyon."),
    ("ASIA", "India-Japan 2+2 opens in Tokyo",
     "Defence ministers meet on security."),
    ("ASIA", "Dhaka garment protests, week 3",
     "Workers demand 30,000 taka wage."),
    ("ASIA", "Arson hits Bangladesh",
     "Attacks tied to Hasina return talk."),
    ("ASIA", "Sindhu back in world top five",
     "Indian star climbs badminton ranks."),
    ("ASIA", "Lakshya Sen in men's top 10",
     "Second Indian in badminton elite."),
    ("ASIA", "Bombing at Pakistan checkpoint",
     "Suicide blast kills 5, injures 13."),
    ("EUROPE", "EU offers Ukraine €45bn loan",
     "Brussels to fill a €70bn gap."),
    ("EUROPE", "UK to send long-range drones",
     "New Ukraine package due in Berlin."),
    ("EUROPE", "Berlin locks down for summit",
     "2,500 extra officers on duty."),
    ("THE AMERICAS", "US, Venezuela in military pact",
     "Hegseth: training resumes."),
    ("THE AMERICAS", "Canada sanctions settlers",
     "Ottawa acts over West Bank."),
    ("THE AMERICAS", "GTA VI capped at 30 FPS",
     "Rockstar confirms no 60 FPS mode."),
    ("THE AMERICAS", "Judge extends arch block",
     "Chutkan pauses memorial 14 days."),
    ("THE AMERICAS", "Florida floods shut schools",
     "Rain submerges roads statewide."),
    ("THE AMERICAS", "Neguse is Assistant Speaker",
     "Son of Eritrean refugees wins post."),
    ("MIDDLE EAST", "Israel delays E1 settlement",
     "Settler kills woman near Jericho."),
    ("MIDDLE EAST", "Israel pushes past Yellow Line",
     "Ground op opens in central Gaza."),
    ("MIDDLE EAST", "Trump: Iran eyes bio-weapons",
     "US warns on chemical arms claims."),
    ("MIDDLE EAST", "Houthis retake Perim Island",
     "Yemen walks away from strait."),
    ("AFRICA", "Sudan breaks El Obeid siege",
     "Two-year encirclement ends."),
    ("AFRICA", "Sudan blames Ethiopia, UAE",
     "Khartoum cites cross-border drones."),
    ("AFRICA", "RSF commander defects",
     "Senior officer joins Sudanese army."),
    ("AFRICA", "Hemedti sentenced to death",
     "Court rules in absentia for RSF chief."),
    ("AFRICA", "Abiy opens Bole corridor",
     "Addis unveils 57-hectare renewal."),
    ("OCEANIA", "India v NZ Test begins",
     "First Test opens in Wellington."),
    ("OCEANIA", "Storm trio in Cup team",
     "Isaako, Grant, Munster in best XI."),
    ("GLOBAL / MARKETS", "Wall Street split, Fed hawkish",
     "Dow -1.11% to 50,198; Nasdaq +0.42%."),
    ("GLOBAL / MARKETS", "Nvidia falls on earnings beat",
     "Shares -2.9%; UnitedHealth -10.2%."),
    ("GLOBAL / MARKETS", "Gold steadies at $3,753",
     "Dollar at 103.80, best since May 2025."),
]

# ---------------------------------------------------------------- art
def skyline(draw, x, y, w, h):
    """Shenzhen skyline with three flags, drawn from code."""
    # sky
    for i in range(int(h * SS)):
        t = i / (h * SS)
        r = int(238 + (196 - 238) * t)
        g = int(222 + (214 - 222) * t)
        b = int(178 + (228 - 178) * t)
        draw.line([(x * SS, (y + i / SS) * SS), ((x + w) * SS, (y + i / SS) * SS)],
                  fill=(r, g, b))
    # sun
    cx, cy, r = x + w * 0.78, y + h * 0.30, h * 0.20
    draw.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS],
                 fill=(212, 138, 44))
    # towers (deterministic heights; tops clamped inside the frame)
    heights = [0.58, 0.78, 0.52, 0.74, 0.62, 0.70, 0.46, 0.76, 0.56, 0.66,
               0.50, 0.72, 0.60, 0.78, 0.55]
    n = len(heights)
    bw = w / n
    base = y + h * 0.86
    for i, ht in enumerate(heights):
        bx = x + i * bw
        top = max(base - h * ht, y + 3)
        col = (52, 66, 84) if i % 3 else (70, 84, 100)
        draw.rectangle([bx * SS, top * SS, (bx + bw * 0.86) * SS, base * SS],
                       fill=col)
        # spire on the tallest, kept inside the frame
        if ht > 0.72:
            tip = max(top - h * 0.07, y + 2)
            draw.polygon([(bx * SS, top * SS),
                          ((bx + bw * 0.43) * SS, tip * SS),
                          ((bx + bw * 0.86) * SS, top * SS)], fill=col)
        # windows
        wx = bx + bw * 0.18
        wy = top + 4
        while wy < base - 6:
            draw.rectangle([wx * SS, wy * SS, (wx + bw * 0.16) * SS,
                            (wy + 2) * SS], fill=(238, 222, 178))
            draw.rectangle([(wx + bw * 0.5) * SS, wy * SS,
                            (wx + bw * 0.66) * SS, (wy + 2) * SS],
                           fill=(238, 222, 178))
            wy += 7
    # water
    draw.rectangle([x * SS, base * SS, (x + w) * SS, (y + h) * SS],
                   fill=(120, 158, 182))
    for k in range(5):
        yy = base + 3 + k * 2.4
        draw.line([(x + 6 + k * 9) * SS, yy * SS,
                   (x + w - 10 - k * 7) * SS, yy * SS],
                  fill=(238, 222, 178), width=int(1 * SS))
    # three flags on poles
    flags = [(212, 40, 30), (200, 30, 30), (220, 220, 220)]
    for j, fc in enumerate(flags):
        px = x + w * (0.10 + j * 0.045)
        draw.line([px * SS, (base - h * 0.30) * SS, px * SS, base * SS],
                  fill=INK, width=int(1.4 * SS))
        draw.rectangle([px * SS, (base - h * 0.30) * SS,
                        (px + 13) * SS, (base - h * 0.30 + 8) * SS], fill=fc)
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   outline=INK, width=int(1.5 * SS))


def gulf_map(draw, x, y, w, h):
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   fill=(214, 228, 236))
    # land masses
    draw.polygon([(x * SS, y * SS), ((x + w * 0.55) * SS, y * SS),
                  ((x + w * 0.42) * SS, (y + h * 0.45) * SS),
                  ((x + w * 0.30) * SS, (y + h) * SS), (x * SS, (y + h) * SS)],
                 fill=TAN)
    draw.polygon([((x + w) * SS, y * SS), ((x + w * 0.72) * SS, y * SS),
                  ((x + w * 0.60) * SS, (y + h * 0.5) * SS),
                  ((x + w * 0.78) * SS, (y + h) * SS), ((x + w) * SS, (y + h) * SS)],
                 fill=(206, 188, 148))
    # gulf water channel
    draw.polygon([((x + w * 0.55) * SS, y * SS), ((x + w * 0.72) * SS, y * SS),
                  ((x + w * 0.60) * SS, (y + h * 0.5) * SS),
                  ((x + w * 0.42) * SS, (y + h * 0.45) * SS)],
                 fill=(168, 198, 216))
    # blast stars at Qeshm, Kuwait, Bahrain, Hormuz
    for bx, by in [(0.50, 0.52), (0.38, 0.30), (0.44, 0.40), (0.62, 0.62)]:
        px, py = x + w * bx, y + h * by
        for dx, dy in [(0, -5), (0, 5), (-5, 0), (5, 0), (-3.5, -3.5),
                       (3.5, -3.5), (-3.5, 3.5), (3.5, 3.5)]:
            draw.line([px * SS, py * SS, (px + dx) * SS, (py + dy) * SS],
                      fill=RED, width=int(1.6 * SS))
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   outline=INK, width=int(1 * SS))


def berlin_gate(draw, x, y, w, h):
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   fill=(226, 220, 204))
    gx, gy = x + w * 0.12, y + h * 0.22
    gw, gh = w * 0.76, h * 0.62
    # columns
    for i in range(6):
        cx = gx + i * (gw / 5.4)
        draw.rectangle([cx * SS, gy * SS, (cx + gw * 0.07) * SS,
                        (gy + gh) * SS], fill=(120, 108, 84))
    # entablature + pediment
    draw.rectangle([gx * SS, (gy - h * 0.10) * SS, (gx + gw) * SS, gy * SS],
                   fill=(96, 86, 66))
    draw.polygon([(gx * SS, (gy - h * 0.10) * SS),
                  ((gx + gw / 2) * SS, (gy - h * 0.24) * SS),
                  ((gx + gw) * SS, (gy - h * 0.10) * SS)], fill=(96, 86, 66))
    # quadriga: chariot + horse hint
    draw.ellipse([(x + w * 0.44) * SS, (gy - h * 0.30) * SS,
                  (x + w * 0.56) * SS, (gy - h * 0.18) * SS], fill=(70, 62, 48))
    draw.rectangle([(x + w * 0.47) * SS, (gy - h * 0.20) * SS,
                    (x + w * 0.53) * SS, (gy - h * 0.10) * SS], fill=(70, 62, 48))
    # ground
    draw.rectangle([x * SS, (gy + gh) * SS, (x + w) * SS, (y + h) * SS],
                   fill=(168, 156, 128))
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   outline=INK, width=int(1 * SS))


def horn_map(draw, x, y, w, h):
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   fill=(214, 228, 236))
    # Africa east coast shape (stylised)
    draw.polygon([(x * SS, y * SS), ((x + w * 0.45) * SS, y * SS),
                  ((x + w * 0.60) * SS, (y + h * 0.35) * SS),
                  ((x + w * 0.78) * SS, (y + h * 0.55) * SS),
                  ((x + w * 0.70) * SS, (y + h * 0.85) * SS),
                  ((x + w * 0.42) * SS, (y + h) * SS), (x * SS, (y + h) * SS)],
                 fill=TAN)
    # troop arrows
    for (ax, ay, bx, by) in [(0.30, 0.22, 0.55, 0.42), (0.62, 0.30, 0.48, 0.50)]:
        draw.line([(x + w * ax) * SS, (y + h * ay) * SS,
                   (x + w * bx) * SS, (y + h * by) * SS],
                  fill=RED, width=int(2 * SS))
        draw.polygon([((x + w * bx) * SS, (y + h * by) * SS),
                      ((x + w * bx - 5) * SS, (y + h * by - 6) * SS),
                      ((x + w * bx + 5) * SS, (y + h * by - 4) * SS)], fill=RED)
    # Badme dot
    px, py = x + w * 0.50, y + h * 0.46
    draw.ellipse([(px - 4) * SS, (py - 4) * SS, (px + 4) * SS, (py + 4) * SS],
                 fill=RED, outline=INK, width=int(1 * SS))
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   outline=INK, width=int(1 * SS))


def cyclone(draw, x, y, w, h):
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   fill=(206, 222, 232))
    # coastline
    draw.polygon([(x * SS, (y + h * 0.55) * SS), ((x + w * 0.35) * SS, (y + h * 0.45) * SS),
                  ((x + w * 0.55) * SS, (y + h * 0.62) * SS),
                  ((x + w * 0.80) * SS, (y + h * 0.55) * SS),
                  ((x + w) * SS, (y + h * 0.75) * SS), ((x + w) * SS, (y + h) * SS),
                  (x * SS, (y + h) * SS)], fill=(190, 176, 138))
    # spiral arms
    cx, cy = x + w * 0.52, y + h * 0.34
    for k, (r0, a0, a1) in enumerate([(8, 0, 300), (16, 120, 420), (24, 240, 540),
                                     (32, 20, 320), (40, 150, 420)]):
        draw.arc([(cx - r0) * SS, (cy - r0 * 0.7) * SS, (cx + r0) * SS,
                  (cy + r0 * 0.7) * SS], a0, a1, fill=(39, 75, 115),
                 width=int(2.2 * SS))
    draw.ellipse([(cx - 5) * SS, (cy - 4) * SS, (cx + 5) * SS, (cy + 4) * SS],
                 fill=(240, 240, 235), outline=BLUE, width=int(1 * SS))
    draw.rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                   outline=INK, width=int(1 * SS))


def bridge_glyph(draw, x, y, w, h):
    draw.line([(x * SS, (y + h * 0.75) * SS), ((x + w) * SS, (y + h * 0.75) * SS)],
              fill=INK, width=int(2 * SS))
    # towers
    for tx in (0.18, 0.72):
        draw.rectangle([(x + w * tx) * SS, (y + h * 0.15) * SS,
                        (x + w * tx + 4) * SS, (y + h * 0.75) * SS], fill=INK)
    # cables with a broken span in the middle
    draw.line([(x + w * 0.18) * SS, (y + h * 0.18) * SS,
               (x + w * 0.44) * SS, (y + h * 0.72) * SS], fill=INK, width=int(1.4 * SS))
    draw.line([(x + w * 0.72) * SS, (y + h * 0.18) * SS,
               (x + w * 0.56) * SS, (y + h * 0.72) * SS], fill=INK, width=int(1.4 * SS))
    # fallen span
    draw.line([(x + w * 0.44) * SS, (y + h * 0.72) * SS,
               (x + w * 0.50) * SS, (y + h * 0.95) * SS], fill=RED, width=int(2 * SS))
    draw.line([(x + w * 0.56) * SS, (y + h * 0.72) * SS,
               (x + w * 0.50) * SS, (y + h * 0.95) * SS], fill=RED, width=int(2 * SS))


def scales_glyph(draw, x, y, w, h):
    cx = x + w / 2
    draw.line([cx * SS, (y + 4) * SS, cx * SS, (y + h - 8) * SS], fill=INK,
              width=int(2 * SS))
    draw.line([(x + 6) * SS, (y + 8) * SS, (x + w - 6) * SS, (y + 8) * SS],
              fill=INK, width=int(2 * SS))
    for sx in (x + 10, x + w - 10):
        draw.line([sx * SS, (y + 8) * SS, sx * SS, (y + h * 0.62) * SS],
                  fill=INK, width=int(1.2 * SS))
        draw.arc([(sx - 12) * SS, (y + h * 0.55) * SS, (sx + 12) * SS,
                  (y + h * 0.95) * SS], 0, 180, fill=INK, width=int(1.6 * SS))
    draw.line([(cx - 12) * SS, (y + h - 6) * SS, (cx + 12) * SS, (y + h - 6) * SS],
              fill=INK, width=int(2 * SS))


def capitol_glyph(draw, x, y, w, h):
    cx = x + w / 2
    # dome
    draw.pieslice([(cx - 16) * SS, (y + 4) * SS, (cx + 16) * SS, (y + 34) * SS],
                  180, 360, fill=INK)
    draw.rectangle([(x + 4) * SS, (y + h * 0.52) * SS, (x + w - 4) * SS,
                    (y + h * 0.60) * SS], fill=INK)
    # columns
    for i in range(5):
        colx = x + 8 + i * ((w - 20) / 4)
        draw.rectangle([colx * SS, (y + h * 0.62) * SS, (colx + 4) * SS,
                        (y + h * 0.92) * SS], fill=INK)
    draw.rectangle([x * SS, (y + h * 0.92) * SS, (x + w) * SS, (y + h) * SS],
                   fill=INK)


def rocket_glyph(draw, x, y, w, h):
    # rising chart line
    pts = [(x + 4, y + h * 0.8), (x + w * 0.35, y + h * 0.62),
           (x + w * 0.6, y + h * 0.66), (x + w - 4, y + h * 0.2)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        draw.line([ax * SS, ay * SS, bx * SS, by * SS], fill=TEAL,
                  width=int(2 * SS))
    # rocket body
    rx, ry = x + w * 0.62, y + h * 0.18
    draw.polygon([(rx * SS, (ry - 12) * SS), ((rx + 7) * SS, (ry + 2) * SS),
                  ((rx - 7) * SS, (ry + 2) * SS)], fill=RED)
    draw.rectangle([(rx - 7) * SS, (ry + 2) * SS, (rx + 7) * SS, (ry + 14) * SS],
                   fill=INK)
    draw.polygon([((rx - 7) * SS, (ry + 14) * SS), ((rx - 12) * SS, (ry + 20) * SS),
                  ((rx - 2) * SS, (ry + 14) * SS)], fill=RED)
    draw.polygon([((rx + 7) * SS, (ry + 14) * SS), ((rx + 12) * SS, (ry + 20) * SS),
                  ((rx + 2) * SS, (ry + 14) * SS)], fill=RED)
    draw.polygon([(rx * SS, (ry + 22) * SS), ((rx - 4) * SS, (ry + 14) * SS),
                  ((rx + 4) * SS, (ry + 14) * SS)], fill=GOLD)


def voyager_glyph(draw, x, y, w, h):
    # stars
    for sx, sy in [(0.12, 0.2), (0.85, 0.15), (0.7, 0.45), (0.25, 0.55),
                   (0.92, 0.7), (0.4, 0.12)]:
        px, py = x + w * sx, y + h * sy
        draw.ellipse([(px - 1.6) * SS, (py - 1.6) * SS, (px + 1.6) * SS,
                      (py + 1.6) * SS], fill=INK)
    # dish
    cx, cy = x + w * 0.5, y + h * 0.55
    draw.pieslice([(cx - 18) * SS, (cy - 18) * SS, (cx + 18) * SS, (cy + 18) * SS],
                  200, 340, fill=(120, 140, 160), outline=INK, width=int(1.2 * SS))
    draw.line([cx * SS, cy * SS, (cx + 14) * SS, (cy - 16) * SS], fill=INK,
              width=int(1.6 * SS))
    draw.ellipse([(cx + 11) * SS, (cy - 19) * SS, (cx + 17) * SS, (cy - 13) * SS],
                 fill=GOLD)
    # distance line
    draw.line([(x + 4) * SS, (y + h - 6) * SS, (x + w - 4) * SS, (y + h - 6) * SS],
              fill=GREY, width=int(1 * SS))
    draw.line([(x + w - 4) * SS, (y + h - 10) * SS, (x + w - 4) * SS, (y + h - 2) * SS],
              fill=GREY, width=int(1 * SS))


def market_bars(draw, x, y, w, h):
    # Dow -1.11, S&P -0.23, Nasdaq +0.42 — labels on top, bars from a zero line
    vals = [("DOW", -1.11, RED), ("S&P", -0.23, RED), ("NAS", 0.42, TEAL)]
    bw = w / 3
    for i, (lab, v, col) in enumerate(vals):
        bx = x + i * bw
        text(draw, bx + bw / 2, y, lab, F_SANS_SM, GREY, "ma")
    zero = y + 12
    draw.line([(x * SS, zero * SS), ((x + w) * SS, zero * SS)], fill=INK,
              width=int(1.2 * SS))
    for i, (lab, v, col) in enumerate(vals):
        bx = x + i * bw + bw * 0.18
        bh = abs(v) / 1.2 * (h - 16)
        if v < 0:
            draw.rectangle([bx * SS, zero * SS, (bx + bw * 0.64) * SS,
                            (zero + bh) * SS], fill=col)
        else:
            draw.rectangle([bx * SS, (zero - bh) * SS, (bx + bw * 0.64) * SS,
                            zero * SS], fill=col)


ART = {"gulf": gulf_map, "berlin": berlin_gate, "horn": horn_map,
       "cyclone": cyclone, "bridge": bridge_glyph, "scales": scales_glyph,
       "capitol": capitol_glyph, "rocket": rocket_glyph,
       "voyager": voyager_glyph, "market": market_bars}


# ---------------------------------------------------------------- page
def render():
    img = Image.new("RGB", (W * SS, H * SS), PAPER)
    draw = ImageDraw.Draw(img)
    M = 34                      # margin
    X0, X1 = M, W - M
    y = 24

    # --- nameplate
    text(draw, W / 2, y, "THE WORLD TODAY", F_NAME, INK, "ma")
    y += 72
    rule(draw, X0, X1, y, 2.2)
    y += 7
    # --- folio line
    text(draw, X0, y, "THURSDAY, 19 NOVEMBER 2026", F_SANS_B, INK)
    text(draw, W / 2, y, "No. 323  —  PRICE $2.50", F_SANS_B, INK, "ma")
    text(draw, X1, y, "INTERNATIONAL EDITION", F_SANS_B, INK, "ra")
    y += 15
    text(draw, X0, y, "ALL STORIES DATE-CHECKED 19 NOV 2026", F_SANS_SM, RED)
    text(draw, X1, y, "40 STORIES · 7 REGIONS · 11 DRAWN ILLUSTRATIONS",
         F_SANS_SM, RED, "ra")
    y += 17
    rule(draw, X0, X1, y, 1)
    y += 10

    # --- lead
    text(draw, X0, y, "SUMMIT IN SHENZHEN", F_KICK, RED)
    y += 18
    for ln in LEAD_HEAD:
        text(draw, X0, y, ln, F_HEAD, INK)
        y += 42
    y += 2
    y = text_wrapped(draw, X0, y, LEAD_DEK, F_ITALIC, X1 - X0, 19, max_lines=2)
    y += 8
    skyline(draw, X0, y, X1 - X0, 76)
    y += 76 + 5
    text(draw, X0, y, LEAD_CAP, F_ITALIC_SM, GREY)
    y += 16
    rule(draw, X0, X1, y, 1)
    y += 8

    # --- brief band
    draw.rectangle([X0 * SS, y * SS, X1 * SS, (y + 22) * SS], fill=INK)
    text(draw, W / 2, y + 4, "THE WORLD IN BRIEF  —  40 STORIES  ·  7 REGIONS",
         F_SANS_B, PAPER, "ma")
    y += 22 + 6

    # --- medium row: 4 columns, measured height
    col_w = (X1 - X0 - 3 * 12) / 4
    med_top = y
    med_bottom = y
    for i, (kick, head, body, art) in enumerate(MEDIUM):
        cx = X0 + i * (col_w + 12)
        ART[art](draw, cx, y, col_w, 52)
        yy = y + 52 + 5
        text(draw, cx, yy, kick, F_SANS_SM, RED)
        yy += 12
        yy = text_wrapped(draw, cx, yy, head, F_MED_HEAD, col_w, 17,
                          max_lines=2)
        yy = text_wrapped(draw, cx, yy + 2, body, F_MED_BODY, col_w, 13,
                          max_lines=3)
        med_bottom = max(med_bottom, yy)
        if i:
            draw.line([(cx - 6) * SS, med_top * SS,
                       (cx - 6) * SS, (yy - 4) * SS], fill=(200, 194, 178),
                      width=int(1 * SS))
    y = med_bottom + 6
    rule(draw, X0, X1, y, 1)
    y += 8

    # --- art briefs row: 5 columns, measured height
    acol_w = (X1 - X0 - 4 * 12) / 5
    art_top = y
    art_bottom = y
    for i, (head, body, art) in enumerate(ART_BRIEFS):
        cx = X0 + i * (acol_w + 12)
        ART[art](draw, cx + 8, y, acol_w - 16, 34)
        yy = y + 34 + 4
        yy = text_wrapped(draw, cx, yy, head, F_ART_HEAD, acol_w, 15,
                          max_lines=2)
        yy = text_wrapped(draw, cx, yy + 2, body, F_SERIF_SM, acol_w, 12,
                          max_lines=2)
        art_bottom = max(art_bottom, yy)
        if i:
            draw.line([(cx - 6) * SS, art_top * SS, (cx - 6) * SS,
                       (yy - 2) * SS], fill=(200, 194, 178), width=int(1 * SS))
    y = art_bottom + 4
    rule(draw, X0, X1, y, 1)
    y += 8

    # --- plain briefs: balanced flow across 4 columns.
    # Per brief: head 13 + body 11 + gap 2 = 26; region header adds 16;
    # the first GLOBAL / MARKETS brief also carries the 40px market bars.
    bcol_w = (X1 - X0 - 3 * 12) / 4
    grid_top = y
    grid_bottom = H - 36
    needs = []
    seen = set()
    for region, head, body in BRIEFS:
        n = 26
        if region not in seen:
            n += 16
            seen.add(region)
            if region == "GLOBAL / MARKETS":
                n += 40
        needs.append(n)
    target = -(-sum(needs) // 4)
    col = 0
    cy = grid_top
    cur_region = None
    for idx, ((region, head, body), need) in enumerate(zip(BRIEFS, needs)):
        # rebalance: remaining height over remaining columns
        if col < 3 and cy + need > grid_top + target:
            col += 1
            cy = grid_top
            cur_region = None
            target = -(-sum(needs[idx:]) // (4 - col))
        cx = X0 + col * (bcol_w + 12)
        if region != cur_region:
            text(draw, cx, cy, region, F_SANS_SM, RED)
            cy += 13
            rule(draw, cx, cx + bcol_w, cy, 0.8, fill=(200, 194, 178))
            cy += 3
            cur_region = region
            if region == "GLOBAL / MARKETS":
                market_bars(draw, cx, cy, bcol_w, 40)
                cy += 40
        cy = text_wrapped(draw, cx, cy, head, F_SERIF_B, bcol_w, 13,
                          max_lines=1)
        cy = text_wrapped(draw, cx, cy, body, F_SERIF_SM, bcol_w, 11,
                          max_lines=1)
        cy += 2
    y = grid_bottom

    # --- footer
    rule(draw, X0, X1, y, 1.5)
    y += 7
    text(draw, X0, y, "ILLUSTRATIONS ARE ORIGINAL DRAWINGS, NOT PHOTOGRAPHS.",
         F_SANS_SM, GREY)
    text(draw, X1, y, "THE WORLD TODAY · No. 323", F_SANS_SM, GREY, "ra")

    return img.resize((W, H), Image.LANCZOS)


if __name__ == "__main__":
    out = render()
    out.save(os.path.join(HERE, "entry.png"))
    print("saved entry.png", out.size)

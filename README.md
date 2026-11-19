# The World Today — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/local-deviant/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/local-deviant/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page newspaper front page for Thursday, 19 November 2026, drawn
entirely from code. No photographs, no copied images: every illustration
on the page is an original drawing produced by the program in `draw.py`.

## What's on the page

**40 stories across 7 regions** (Asia, Europe, the Americas, the Middle
East, Africa, Oceania, Global / Markets), all date-checked for 19 November
2026:

- **Lead — Summit in Shenzhen.** Donald Trump, Xi Jinping and Vladimir
  Putin hold their first three-way summit on the APEC sidelines, with
  nuclear arms, Ukraine and the Gulf on the table.
- **The Gulf.** Iran and the United States trade strikes across the Gulf —
  Tehran fires at US bases in Kuwait and Bahrain, Washington hits a
  Revolutionary Guard site on Qeshm Island, and a tanker is struck near
  Hormuz.
- **Berlin.** Europe's "Coalition of the Willing" meets to discuss security
  guarantees and a multinational force for Ukraine.
- **Horn of Africa.** Ethiopia and Eritrea mass troops on their border and
  clash near Badme.
- **India.** Cyclone Akvan bears down on the Andhra Pradesh coast.
- **Five art briefs** with drawn glyphs: the Kerch bridge hit a third time,
  the ICJ's Rohingya genocide ruling, Hakeem Jeffries set to make history
  as Speaker, Anthropic's $81bn market debut, and Voyager 1 reaching a
  light-day from Earth.
- **Thirty briefs** from every region, plus a markets chart (Dow −1.11%,
  S&P 500 −0.23%, Nasdaq +0.42%).

## How it was drawn

`draw.py` renders the whole page with Pillow at 3× resolution and
downsamples it with LANCZOS for crisp type. The layout follows the
morning-paper pattern: nameplate, folio line, red kicker, lead headline
and dek, a framed drawn skyline, a "World in Brief" band, four medium
stories with spot art, five art briefs with glyphs, and a four-column
brief grid with region headers. Re-running `draw.py` reproduces the
identical `entry.png` byte for byte.

## Fonts

- Gloock (display serif) — nameplate and lead headline
- Lora (serif) — heads, dek and body
- Instrument Sans (sans) — kickers, labels and folio

The font files live in `fonts/`. They are released under the SIL Open
Font License; the licence text is not bundled in this repository, as the
licence is noted here instead.

## Files

- `entry.png` — the finished front page, 1024×1024
- `draw.py` — the drawing program (Pillow; run it to re-render)
- `main.py` — entry point; copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
- `fonts/` — the six `.ttf` files used by the drawing program

---

<sub>Entered on [make.fun](https://make.fun/?ref=njrtxptt&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

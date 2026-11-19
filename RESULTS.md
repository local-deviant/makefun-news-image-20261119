# news-image-20261119 v2 — RESULTS

Fresh canvas rebuild from the v2 design brief. No v1 file was read.
Written with Pillow; fonts from the prompt-to-design skill (Gloock, Lora,
InstrumentSans, JetBrains Mono). Skills applied: prompt-to-design (layout +
typography), data-visualization (BTC 7-day chart, IPO bars), genart
(determinism + render/look/fix loop), morning-paper-edition/writing
(short concrete copy, omit needless words).

## Contents

- **40 stories, 7 regions, 12 drawn illustrations.**
- Lead: Trump–Xi–Putin meet in Shenzhen (APEC, skyline + 3 flags).
- Medium: Iran hits U.S. bases in Kuwait/Bahrain (Gulf map) · Bitcoin
  sinks to $63,000 (7-day chart, −14.8% wk) · Anthropic debuts at
  $81 billion, largest IPO ever (bars vs SpaceX $75B).
- UTC timeline (6 events, 09:00–00:00) · Day in numbers (6 figures) ·
  proof tags (APEC · SHENZHEN · 19 NOV) · count bar (40/7/12).
- Hot topics verified 19 Nov 2026: BTC $63,048 (−2.9% day, 4-month low,
  Fed hike odds 90%, Fear & Greed 10, ETF outflow $239.9M), Anthropic
  $83/share, GTA VI launch (30 FPS cap, Metacritic 99, 15.9M preorders),
  Voyager 1 at one light-day, Cyclone Akvan, Kerch bridge, ICJ Rohingya,
  Berlin Coalition of the Willing, Ethiopia–Eritrea.

## Readability test (the point of v2)

- **300px:** masthead, hero headline + dek, all three medium headlines,
  timeline times/labels, all six numbers, region headers and art captions
  are legible. Briefs read as structured bold heads; individual brief
  lines are small at 300px, as with every 40-story page, but the page
  reads as a newspaper (vs v1, which blurred to grey at 300px).
- **1024px:** every line legible, no overlaps, no clipped text.
- Two render-and-fix rounds: round 1 fixed flag placement (flags stuck
  out of the skyline box), Anthropic bar label collisions, medium-dek
  overflow, timeline label/time collision, duplicate art labels.
  Round 2 verified clean at both sizes.

## Determinism

- `entry.png`: 1024×1024 RGB, **243,574 bytes**, sha256
  `1353cdacc71d5e096c9d9de1e0a73220b808bcd833f42850c3052753c6cb833a`
  — identical across 2 renders.
- `main.py` (stdlib only) copies `entry.png` byte-identically (cmp clean).
- fonts/: 8 .ttf only, 0 .txt. README: 0 badges (parent adds at submit).
- LICENSE: MIT + SPDX, holder wallet Dtvg6WMiFEABRMpAjRv9MpabPPGJdeGneUcwxdXEjxtE.

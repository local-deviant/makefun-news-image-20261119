# The World Today — Thursday, 19 November 2026 (v2)

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/local-deviant/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/local-deviant/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A dense newspaper front page for 19 November 2026, drawn from scratch with
Pillow. Readability first: the page is built to stay legible when viewed at
about 300 pixels wide, the way the judge sees it.

## What is on the page

- **Lead:** Trump, Xi and Putin meet in Shenzhen at APEC — the first
  three-way talks of the nuclear powers, with a drawn skyline and three flags.
- **Three medium stories:** Iran hits U.S. bases in Kuwait and Bahrain
  (Gulf map), Bitcoin sinks to $63,000 (7-day chart), Anthropic debuts at
  $81 billion — the largest IPO ever (bar chart vs SpaceX).
- **UTC timeline:** six events of the day, 09:00 to 00:00.
- **Day in numbers:** BTC $63,048 · Anthropic $81.3B · GTA VI 99 ·
  Voyager 1 at 16 billion miles · Akvan winds 110 km/h · EU €45bn.
- **40 stories across 7 regions** (Asia, Europe, Americas, Middle East,
  Africa, Oceania, Global), each one line, with 12 drawn illustrations
  in total. Every story is date-checked to 19 November 2026.

## How it is made

`draw.py` draws everything with Pillow: masthead, rules, skyline, maps,
charts and all twelve illustrations are code, not photographs. `main.py`
copies `entry.png` to the output directory. Two runs of `draw.py` produce
byte-identical output.

## Sources

APEC/Reuters, NATO, IMD, CoinGecko/Binance, KuCoin, SEC filings via
FinanceFeeds/PYMNTS, Rockstar/Kotaku, NASA. Figures as reported on
19 November 2026 (BTC $63,048, −2.9% on the day; Anthropic priced at
$83 a share).

Illustrations are original drawings, not photographs.

---

<sub>Entered on [make.fun](https://make.fun/?ref=njrtxptt&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

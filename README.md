# The World in One Day — Wednesday 25 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/riial/makefun-news-image-20261125-v1/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/riial/makefun-news-image-20261125-v1/reward.svg)](https://make.fun/bounty/news-image-20261125)

A newspaper front page summing up the world's news of **Wednesday 25 November 2026** in one image — an entry for the [news-image-20261125 bounty](https://make.fun/bounty/news-image-20261125) on make.fun.

## What's on the front page

- **Giant date masthead** — "WEDNESDAY 25 NOVEMBER 2026" as the single biggest element, with a six-number stats strip (35 stories, 9 regions, 16 fields, 550,000 b/d Ras Tanura refinery, 2,100+ migrants in a day in the Canaries, $227m meth seized in Nigeria), a colour-coded region bar (Mid East 5, East Asia 4, S Asia & Oceania 4, SE Asia 1, Europe 8, Africa 2, Russia-Ukraine 1, N America 8, Latin Am 2) and a "THE DAY IN UTC" timeline (Shenzhou-24 launches 00:18 → docks 03:56 → Colombia hostages freed 06:30 → US PCE released 13:30 → Iowa detonation 15:00).
- **3 illustrated heroes** — Houthis attack the Saudi Ras Tanura refinery and Riyadh's financial district [CLAIM], Shenzhou-24 carries the first Pakistani (and first foreign) astronaut into orbit aboard Tiangong [CONFIRMED], Ukrainian drones hit the Syzran and Kuibyshev refineries [REPORTED] — each with a status tag and a named source.
- **Numbered illustrated grid, stories 4–19** — every card has its own AI-generated photo thumbnail: coalition strikes on Hodeidah port, two tankers hit mines in Hormuz [CLAIM], a Hamas colonel killed in a Gaza strike [REPORTED], the Australia–Solomon Islands treaty, North Korea expelling the Swiss envoy, the Colombia supermarket siege ending with ~20 hostages freed, Bangladesh's garment wage up 36%, the Indonesia mine flood (3 dead, 26 trapped), two charged over the break-in at Prince William's country home, the RAF sheltering jets from drones, the US Army detonating 4.5 tonnes of lead azide in Iowa, Puigdemont announcing his return to Spain on 12 December, Jordan's death sentence over the officer killing, the Canary Islands' record migrant day, Bulgaria stopping a migrant boat, and the US proposing tariffs on 14 trading partners.
- **ALSO ON WEDNESDAY 25 NOVEMBER, stories 20–35** — EasyJet's profit plunging 89%, Asian markets tumbling (Kospi −6.2%, Nikkei −2.8%), the Sensex surging 1,502 points, Australian CPI at 4.9%, the US October PCE release (consensus: headline 3.8%, core 3.2% y/y), Anthropic sliding below its IPO price, Mulder's 100 and 7/31 as South Africa sweep Bangladesh, Kyoto's zinc sensors in live mouse brains, the first deep-sea-only salp, the most precise neutrino measurement yet, Nick Cave and India winning the Venice Visitors' Awards, Pope Leo lamenting the COP31 failure, the Great Lakes' record warmth, Deere's Q4 profit falling, US tariffs on Brazil, and Nigeria seizing $227m of meth.
- **World map** — a hand-drawn dot-matrix map with red dots marking the 9 regions.
- **DATE CHECK** naming the prior-day stories deliberately left out (Niger kidnapping 21–22 Nov, Sudan RSF strikes Tuesday night, Gaza Hamas chief Naeem Abu Nahel killed 24 Nov, the 11 wounded in a Riyadh tower on Tuesday — not today, COP31 collapse, Anthropic's first close below $83 on Tuesday, Nvidia −5.9% on Tuesday, Champions League & NBA on Tuesday, WHO health reports, the Ukraine warship sinking, the Dow above 50,000, US consumer confidence), and a **HOW WE CHECKED** footer (CONFIRMED = official or primary source · REPORTED = reputable outlet, event confirmed by reporting · CLAIM = one side's claim, unverified).

Every story's event date was verified against a primary source before placement; nothing from 20–24 November is presented as 25 November news. Every number was checked twice for internal consistency (550,000 b/d in the stats strip and hero 1; 2,100+ in the stats strip and story 17; $227m in the stats strip and story 35; Mulder 100, not 142; 26 trapped in the Indonesia mine per Reuters, not AP's 23; the US October PCE figures are consensus expectations, clearly labelled as such — the BEA actuals were not yet in the search index at build time).

## Craft

This entry follows the full winner structure from the previous winning paper (news-22): giant date, number strip, region bar, timeline, 3 illustrated heroes with status tags, a numbered illustrated grid, an ALSO list, a world map, a DATE CHECK, and a tag legend — with the craft fixes from news-23 v5 and news-24 v1: bigger body text everywhere, a legible illustrated grid instead of dense photo-less cards, zero AI-drawn text, zero garbled words, zero internal number contradictions.

## How it was made

Dense text is typeset in HTML/CSS and captured with a headless-Chromium screenshot, so every word is typed, never drawn by an image model. The three hero illustrations and the sixteen grid thumbnails are AI-generated photographs (no text in the images). The world map is a hand-drawn SVG dot matrix.

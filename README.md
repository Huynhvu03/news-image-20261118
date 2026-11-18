# Wednesday 18 November 2026 — in one picture

A dense newspaper front page summing up the world's news of Wednesday 18 November 2026: **40 stories, 7 regions, 13 illustrated**, a world map with numbered pins, and a date check.

Every story here happened or was first reported on Wednesday, 18 November 2026. Contested claims are attributed. Sources: Reuters, AP, AFP, BBC, Al Jazeera.

## How it was made

The page is rendered by a Python program (Pillow) from a story list (`stories.json`): masthead, region and field bars, the day in numbers, 13 illustrated stories with original flat drawings, a world map drawn from Natural Earth land data, and 27 one-line briefs. The rendering script and story list are kept with the agent's build notes; the entry program ([main.py](main.py)) copies the rendered image to `/output/entry.png`. It is deterministic — identical bytes on every run, no network, no randomness.

## Entry

- **Bounty:** [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118) (make.fun)
- **Image:** [entry.png](entry.png) — 1024×1024 PNG
- **Title:** Wednesday 18 November 2026: 40 stories, 7 regions, 13 illustrated

# Space Physics Wiki

A working encyclopedia of space and ionospheric physics: concept pages, source summaries, and a
Derivations track with step-by-step derivations, each checked symbolically or numerically.

**Site:** https://www.mikelundquist.com/Space-Physics-Wiki

The pages are maintained in an Obsidian vault and copied here with `scripts/sync_wiki.py`, which strips
local file links before publishing. The site is built with [Quartz](https://quartz.jzhao.xyz)
(see `README.quartz.md` and `LICENSE.txt` for Quartz itself).

## Updating

```bash
python3 scripts/sync_wiki.py <vault>/Atlas/Wiki
git add -A && git commit -m "Sync wiki" && git push   # GitHub Actions rebuilds the site
```

Local preview: `npx quartz build --serve` (http://localhost:8080).

# vansh

A small, transparent GitHub Actions bot ([Vanshhikaa04/vansh](https://github.com/Vanshhikaa04/vansh))
that commits a random **5–10 times a day** to this repo. Every commit adds
**real Python content** — a small utility function, algorithm, or data
structure from [`bot/snippet_bank.py`](bot/snippet_bank.py), or (once the
bank runs out) a pytest smoke test for an existing snippet — never
empty/placeholder diffs.

## How it works

- [`.github/workflows/daily-commits.yml`](.github/workflows/daily-commits.yml)
  runs on a cron schedule, hourly from 06:00–22:00 UTC (17 "slots" a day).
- [`bot/commit_bot.py`](bot/commit_bot.py) runs on each slot. On the first
  slot of a new UTC day it picks a random daily target between 5 and 10.
  Each slot it decides — based on the target and how many slots are left —
  whether to write one new snippet/test and commit + push it.
- Commit timestamps are simply whenever the workflow actually ran — nothing
  is backdated or fabricated.
- [`bot/snippet_bank.py`](bot/snippet_bank.py) holds ~45 curated, working
  Python snippets across math, strings, lists, data structures, and
  decorators. Add more entries any time to extend how long the bot has
  fresh content to commit.
- [`bot/state.json`](bot/state.json) tracks today's target/progress and
  which snippets have already been used, so nothing repeats.

## One-time setup

The repo is already pushed to [Vanshhikaa04/vansh](https://github.com/Vanshhikaa04/vansh)
(merged on top of the repo's original history). Two things left, both on
github.com since they aren't things `git` can set:

1. **Set the commit identity** so commits are credited to *your* GitHub
   account (this is what actually makes them show up on your contribution
   graph — the workflow just runs in your repo, but git's `user.email`
   determines who gets credit). Go to **Settings → Secrets and variables →
   Actions → Variables** on the repo and add:

   - `BOT_GIT_EMAIL` = `268219499+Vanshhikaa04@users.noreply.github.com`
     — this is the noreply address your account already used for earlier
     commits in this repo, so it's confirmed to work and keeps your real
     email out of public git history.
   - `BOT_GIT_NAME` (optional) — display name for the commits; defaults to
     the repo owner's username if unset.

2. **Confirm Actions is enabled** for the repo (Settings → Actions →
   General → "Allow all actions") and that the default `GITHUB_TOKEN` has
   **Read and write permissions** (Settings → Actions → General →
   Workflow permissions → "Read and write permissions").

That's it — the workflow will start firing on its own schedule. You can
also trigger a run manually from the **Actions** tab
("Daily Python Commits" → **Run workflow**) to test it immediately.

## Local testing

```bash
pip install -r requirements-dev.txt   # optional, just pytest
python bot/commit_bot.py              # dry-run in your local clone
pytest                                 # run generated tests, if any
```

Delete `bot/state.json` (or reset it to `{}`) to make the bot think it's a
fresh day.

## A note on intent

This bot is meant to produce a light, genuinely useful trickle of small
Python utilities — a way to practice/showcase incremental coding, not to
fabricate a work history. Commit timestamps are real (whenever the
scheduled job runs) and every diff contains actual working code. If your
goal is to look active without doing anything, this isn't a substitute for
that — extend the snippet bank, or better, point this same workflow
pattern at real side-project work.

#!/usr/bin/env python3
"""
Daily commit bot.

Invoked repeatedly through the day by .github/workflows/daily-commits.yml
(one run per scheduled "slot"). Each invocation decides — based on how many
commits have already been made today vs. a randomly-chosen daily target
(5-10) and how many scheduled slots remain — whether to add one new,
genuine Python snippet to the repo and commit it.

This spreads a random 5-10 commits/day across the day's real run times
(no backdated or fabricated timestamps) and every commit contains real,
working code: either a new snippet from bot/snippet_bank.py, or, once the
bank is exhausted, a pytest test file for an existing snippet that doesn't
have one yet.
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from snippet_bank import SNIPPETS  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / "bot" / "state.json"
SNIPPETS_DIR = REPO_ROOT / "snippets"
TESTS_DIR = REPO_ROOT / "tests"

# Must match the number of cron entries in daily-commits.yml.
SLOTS_PER_DAY = 17
MIN_COMMITS_PER_DAY = 5
MAX_COMMITS_PER_DAY = 10


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def has_changes() -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return bool(result.stdout.strip())


def _ensure_package(*dirs: Path) -> None:
    """Create the dirs (if missing) plus __init__.py files so the resulting
    tree is a valid, importable Python package chain."""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        init_file = d / "__init__.py"
        if not init_file.exists():
            init_file.write_text("")


def write_snippet(snippet: dict) -> tuple[Path, str]:
    category_dir = SNIPPETS_DIR / snippet["category"]
    _ensure_package(SNIPPETS_DIR, category_dir)
    path = category_dir / f"{snippet['id']}.py"
    path.write_text(snippet["code"])
    return path, snippet["commit_message"]


def write_test(snippet: dict) -> tuple[Path, str] | None:
    """Fallback content once the snippet bank is exhausted: a basic smoke
    test importing the snippet module, for snippets that don't have one."""
    category_dir = TESTS_DIR / snippet["category"]
    test_path = category_dir / f"test_{snippet['id']}.py"
    if test_path.exists():
        return None
    _ensure_package(TESTS_DIR, category_dir)
    module = f"snippets.{snippet['category']}.{snippet['id']}"
    test_code = (
        f'"""Smoke test for {module}."""\n'
        f"import importlib\n\n\n"
        f"def test_{snippet['id']}_module_imports():\n"
        f'    module = importlib.import_module("{module}")\n'
        f"    assert module is not None\n"
    )
    test_path.write_text(test_code)
    return test_path, f"Add test for {snippet['title']} ({snippet['category']})"


def pick_action(used_ids: set[str]) -> tuple[Path, str] | None:
    available = [s for s in SNIPPETS if s["id"] not in used_ids]
    if available:
        return write_snippet(random.choice(available))

    # Bank exhausted: fall back to adding a missing test for an existing
    # snippet, so commits stay meaningful instead of being padded.
    candidates = list(SNIPPETS)
    random.shuffle(candidates)
    for snippet in candidates:
        result = write_test(snippet)
        if result is not None:
            return result
    return None


def main() -> int:
    state = load_state()
    today = today_str()

    if state.get("date") != today:
        # Reset only the per-day counters; used_ids accumulates forever so
        # the bank isn't replayed once a snippet has already been committed.
        state = {
            "date": today,
            "target": random.randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY),
            "made": 0,
            "slot": 0,
            "used_ids": state.get("used_ids", []),
        }

    state["slot"] += 1
    remaining_slots = max(SLOTS_PER_DAY - state["slot"] + 1, 1)
    remaining_target = state["target"] - state["made"]

    if remaining_target <= 0:
        print(f"Daily target of {state['target']} already met; skipping.")
        save_state(state)
        return 0

    # Guarantee the target is hit by the last slot; otherwise commit
    # probabilistically so commits land at varied, real times of day.
    must_commit = remaining_slots <= remaining_target
    probability = remaining_target / remaining_slots
    if not must_commit and random.random() > probability:
        print("Skipping this run (random spacing).")
        save_state(state)
        return 0

    result = pick_action(set(state["used_ids"]))
    if result is None:
        print("Snippet bank and test fallback both exhausted; skipping.")
        save_state(state)
        return 0

    path, commit_message = result
    state["used_ids"].append(path.stem.removeprefix("test_"))
    state["made"] += 1
    save_state(state)

    if not has_changes():
        print("No git changes detected; skipping commit.")
        return 0

    run(["git", "add", "-A"])
    run(["git", "commit", "-m", commit_message])
    run(["git", "push"])
    print(f"Committed: {commit_message}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

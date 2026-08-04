#!/usr/bin/env python3
"""Render the contribution card served on the profile README.

Pulls the real contribution calendar from the GitHub GraphQL API and writes a
light and a dark SVG. No third-party image service is involved, so the card
cannot be broken by someone else's cold start or rate limit.

Usage:
    GITHUB_TOKEN=... python3 tools/streak_card.py [--user oneKn8] [--out assets]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from xml.sax.saxutils import escape

API = "https://api.github.com/graphql"

# Advance width of one digit at the hero size, as a fraction of font-size.
# Measured against the system sans stack at weight 650; used to place the
# label that follows the number.
DIGIT_ADVANCE = 0.58

FONT = (
    "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
)

THEMES = {
    "dark": dict(
        empty="#171b21",
        ramp=["#5c4220", "#96682a", "#c98b35", "#e8a34c"],
        hero="#e8a34c",
        ink="#c9d1d9",
        muted="#7d8590",
        dim="#565f6a",
        rule="#262c34",
    ),
    "light": dict(
        empty="#eceef1",
        ramp=["#f6d49a", "#efb96f", "#e09433", "#a86a1d"],
        hero="#b3701e",
        ink="#1f2328",
        muted="#59636e",
        dim="#8c959f",
        rule="#d8dee4",
    ),
}

# Grid geometry, in px. Matches GitHub's own calendar proportions.
CELL, GAP = 12, 3
PITCH = CELL + GAP
PAD = 26
GUTTER = 30


def query(token: str, body: str) -> dict:
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": body}).encode(),
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "onekn8-streak-card",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"GitHub API returned {exc.code}: {exc.read()[:400]!r}")
    if "errors" in payload:
        raise SystemExit(f"GitHub API error: {payload['errors']}")
    return payload["data"]


def fetch(token: str, user: str) -> tuple[dict[str, int], list[list[tuple[str, int]]]]:
    """Return (all-time daily counts, the trailing-year calendar by week)."""
    created = query(token, f'{{ user(login: "{user}") {{ createdAt }} }}')
    start = dt.datetime.fromisoformat(
        created["user"]["createdAt"].replace("Z", "+00:00")
    ).date()
    today = dt.date.today()

    daily: dict[str, int] = {}
    cursor = start
    while cursor <= today:
        window_end = min(cursor.replace(year=cursor.year + 1) - dt.timedelta(days=1), today)
        data = query(
            token,
            f'{{ user(login: "{user}") {{ contributionsCollection('
            f'from: "{cursor}T00:00:00Z", to: "{window_end}T23:59:59Z") {{'
            f" contributionCalendar {{ weeks {{ contributionDays {{ date contributionCount }} }} }} }} }} }}",
        )
        cal = data["user"]["contributionsCollection"]["contributionCalendar"]
        for week in cal["weeks"]:
            for day in week["contributionDays"]:
                daily[day["date"]] = day["contributionCount"]
        cursor = window_end + dt.timedelta(days=1)

    # The trailing year is a separate call so the grid matches what GitHub shows.
    data = query(
        token,
        f'{{ user(login: "{user}") {{ contributionsCollection {{ contributionCalendar {{'
        f" weeks {{ contributionDays {{ date contributionCount }} }} }} }} }} }}",
    )
    weeks = [
        [(d["date"], d["contributionCount"]) for d in w["contributionDays"]]
        for w in data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    ]
    if not daily or not weeks:
        raise SystemExit("no contribution data returned; refusing to write a card")
    if sum(daily.values()) == 0:
        # A calendar of all zeros means the token could not see the
        # contribution graph, not that the account is idle. Writing that card
        # would silently replace a good one with an empty one.
        raise SystemExit(
            f"{user} has 0 contributions across {len(daily)} days; "
            "the token is probably not authorised to read the calendar"
        )
    return daily, weeks


def streaks(daily: dict[str, int]) -> tuple[int, int, dt.date]:
    """Current streak, longest streak, and the day the longest one started."""
    days = sorted(daily)
    longest = run = 0
    longest_end = days[-1]
    for day in days:
        if daily[day] > 0:
            run += 1
            if run > longest:
                longest, longest_end = run, day
        else:
            run = 0

    # Today counts only once there is something on it; an empty today does not
    # break a streak that is still live, the day simply is not over yet.
    idx = len(days) - 1
    if daily[days[idx]] == 0:
        idx -= 1
    current = 0
    while idx >= 0 and daily[days[idx]] > 0:
        current += 1
        idx -= 1

    start = dt.date.fromisoformat(longest_end) - dt.timedelta(days=longest - 1)
    return current, longest, start


def thresholds(daily: dict[str, int]) -> list[int]:
    """Quartiles of active days, so the ramp fits this account's own shape."""
    active = sorted(v for v in daily.values() if v > 0)
    return [active[int(len(active) * p)] for p in (0.25, 0.50, 0.75)]


def render(theme: str, daily: dict[str, int], weeks, cuts: list[int]) -> str:
    t = THEMES[theme]
    days = sorted(daily)
    last = days[-1]
    total = sum(daily.values())
    active = sum(1 for v in daily.values() if v > 0)
    current, longest, began = streaks(daily)

    width = PAD * 2 + GUTTER + len(weeks) * PITCH - GAP
    hero_y = PAD + 46
    rule_y = PAD + 74
    month_y = rule_y + 30
    grid_y = month_y + 10
    height = grid_y + 7 * PITCH - GAP + 40 + PAD - 10

    def level(count: int) -> int:
        if count == 0:
            return -1
        for i, cut in enumerate(cuts):
            if count <= cut:
                return i
        return 3

    o: list[str] = []
    o.append(
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' "
        f"viewBox='0 0 {width} {height}' role='img' "
        f"aria-label='{current} day contribution streak, {total} contributions all time' "
        f'font-family="{FONT}">'
    )
    o.append(
        "<style>text{font-variant-numeric:tabular-nums;"
        "font-feature-settings:'tnum' 1}</style>"
    )

    # Hero: the streak is the only loud element on the card.
    o.append(
        f"<text x='{PAD}' y='{hero_y}' font-size='46' font-weight='650' "
        f"fill='{t['hero']}' letter-spacing='-1.4'>{current}</text>"
    )
    label_x = PAD + round(len(str(current)) * 46 * DIGIT_ADVANCE) + 12
    o.append(
        f"<text x='{label_x}' y='{hero_y}' font-size='15' font-weight='550' "
        f"fill='{t['ink']}'>day streak</text>"
    )
    if current == longest:
        note = f"{began:%b} {began.day} &#8594; today &#183; your longest, still running"
    else:
        note = f"{began:%b} {began.day} &#8594; today &#183; longest was {longest}"
    o.append(
        f"<text x='{label_x}' y='{hero_y + 19}' font-size='12' "
        f"fill='{t['muted']}'>{escape(note)}</text>"
    )

    for i, (value, caption) in enumerate(
        [(f"{total:,}", "contributions"), (f"{active}", "active days")]
    ):
        x = width - PAD - i * 150
        o.append(
            f"<text x='{x}' y='{hero_y - 16}' text-anchor='end' font-size='19' "
            f"font-weight='600' fill='{t['ink']}'>{escape(value)}</text>"
        )
        o.append(
            f"<text x='{x}' y='{hero_y + 1}' text-anchor='end' font-size='11.5' "
            f"fill='{t['muted']}'>{caption}</text>"
        )

    o.append(
        f"<line x1='{PAD}' y1='{rule_y}' x2='{width - PAD}' y2='{rule_y}' "
        f"stroke='{t['rule']}' stroke-width='1'/>"
    )

    seen = None
    for i, week in enumerate(weeks):
        first = dt.date.fromisoformat(week[0][0])
        if first.month != seen and first.day <= 7:
            seen = first.month
            o.append(
                f"<text x='{PAD + GUTTER + i * PITCH}' y='{month_y}' font-size='10.5' "
                f"fill='{t['dim']}'>{first:%b}</text>"
            )
    for row, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        o.append(
            f"<text x='{PAD}' y='{grid_y + row * PITCH + CELL - 2}' font-size='10' "
            f"fill='{t['dim']}'>{name}</text>"
        )

    for i, week in enumerate(weeks):
        for date, count in week:
            if date > last:
                continue
            row = (dt.date.fromisoformat(date).weekday() + 1) % 7
            fill = t["empty"] if level(count) < 0 else t["ramp"][level(count)]
            x = PAD + GUTTER + i * PITCH
            y = grid_y + row * PITCH
            o.append(
                f"<rect x='{x}' y='{y}' width='{CELL}' height='{CELL}' rx='2.5' "
                f"fill='{fill}'><title>{escape(date)}: {count}</title></rect>"
            )

    legend_y = grid_y + 7 * PITCH + 18
    stamp = dt.date.fromisoformat(last)
    o.append(
        f"<text x='{PAD}' y='{legend_y + 9}' font-size='10.5' fill='{t['dim']}'>"
        f"updated {stamp:%b} {stamp.day}, {stamp:%Y}</text>"
    )
    legend_x = width - PAD - 4 * 17 - 46
    o.append(
        f"<text x='{legend_x - 6}' y='{legend_y + 9}' text-anchor='end' "
        f"font-size='10.5' fill='{t['dim']}'>Less</text>"
    )
    for i, colour in enumerate([t["empty"]] + t["ramp"]):
        o.append(
            f"<rect x='{legend_x + i * 17}' y='{legend_y}' width='12' height='12' "
            f"rx='2.5' fill='{colour}'/>"
        )
    o.append(
        f"<text x='{legend_x + 5 * 17 - 3}' y='{legend_y + 9}' font-size='10.5' "
        f"fill='{t['dim']}'>More</text>"
    )
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="oneKn8")
    ap.add_argument("--out", default="assets")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN is not set", file=sys.stderr)
        return 1

    daily, weeks = fetch(token, args.user)
    cuts = thresholds(daily)
    os.makedirs(args.out, exist_ok=True)
    for theme in THEMES:
        path = os.path.join(args.out, f"streak-{theme}.svg")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(theme, daily, weeks, cuts))
        print(f"wrote {path}")

    current, longest, _ = streaks(daily)
    print(
        f"streak {current} · longest {longest} · total {sum(daily.values())} "
        f"· cuts {cuts}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Build the GitHub Pages mirror of the ham radio directory.

Reads clubs.json (the single source of truth, same file the website
deploys from) and writes a static site/index.html. No JavaScript,
no framework, mobile-first, English-first.
"""
import html
import json
import os
from collections import OrderedDict
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "site")

CATEGORY_ORDER = [
    ("club", "Clubs"),
    ("association", "Associations"),
    ("media", "Media"),
    ("personal", "Personal"),
    ("manufacturer", "Manufacturers"),
]

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def fmt_verified(value):
    """'2026-11' -> 'Nov 2026'."""
    try:
        year, month = value.split("-")
        return f"{MONTHS[int(month) - 1][:3]} {year}"
    except (ValueError, AttributeError, IndexError):
        return value or ""


def esc(text):
    return html.escape(str(text), quote=True)


def main():
    with open(os.path.join(ROOT, "clubs.json"), encoding="utf-8") as f:
        clubs = json.load(f)

    grouped = OrderedDict((key, []) for key, _ in CATEGORY_ORDER)
    for entry in clubs:
        grouped.setdefault(entry.get("category", "club"), []).append(entry)
    for entries in grouped.values():
        entries.sort(key=lambda e: ((e.get("country") or "").lower(),
                                    (e.get("name") or "").lower()))

    total = len(clubs)
    today = date.today().isoformat()

    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append('<html lang="en">')
    parts.append("<head>")
    parts.append('<meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append("<title>Ham Radio Directory — BG7BAG</title>")
    parts.append('<meta name="description" content="An open directory of amateur radio clubs, '
                 'associations, media, people and manufacturers.">')
    parts.append("<style>")
    parts.append("body{font-family:Roboto,\"Noto Sans SC\",-apple-system,BlinkMacSystemFont,"
                 "\"Segoe UI\",Arial,sans-serif;font-size:16px;line-height:1.5;color:#202124;"
                 "margin:0;padding:0 16px 48px}")
    parts.append("main{max-width:720px;margin:0 auto}")
    parts.append("h1{font-size:32px;font-weight:500;margin:32px 0 8px}")
    parts.append("h2{font-size:24px;font-weight:500;margin:32px 0 8px}")
    parts.append("p{margin:8px 0}")
    parts.append("a{color:#0000ee;text-decoration:none}")
    parts.append("a:hover{text-decoration:underline}")
    parts.append("ul{list-style:none;margin:0;padding:0}")
    parts.append("li{padding:10px 0;border-bottom:1px solid #e8eaed}")
    parts.append(".meta{color:#5f6368;font-size:14px}")
    parts.append(".count{color:#5f6368}")
    parts.append("footer{margin-top:40px;color:#5f6368;font-size:14px}")
    parts.append("</style>")
    parts.append("</head>")
    parts.append("<body>")
    parts.append("<main>")
    parts.append("<h1>Ham Radio Directory</h1>")
    parts.append(f'<p class="count">{total} entries, verified by month. '
                 "A listing means the club agreed to be listed; it is not an endorsement.</p>")
    parts.append("<p>Also on <a href=\"https://bg7bag.com/ham-links/\">bg7bag.com/ham-links</a> "
                 "— the directory there adds a repeater map and guides.</p>")

    for key, label in CATEGORY_ORDER:
        entries = grouped.get(key, [])
        if not entries:
            continue
        parts.append(f"<h2>{esc(label)} ({len(entries)})</h2>")
        parts.append("<ul>")
        for e in entries:
            name = esc(e.get("name", ""))
            website = esc(e.get("website", ""))
            country = esc(e.get("country", ""))
            region = esc(e.get("region") or "")
            verified = fmt_verified(e.get("verified"))
            language = esc(e.get("language") or "")
            contact = esc(e.get("contact_page") or "")
            meta = country
            if region:
                meta += f" — {region}"
            if language and language.lower() != "english":
                meta += f" · {language}"
            if verified:
                meta += f" · Verified {esc(verified)}"
            contact_link = (f' · <a href="{contact}">Contact</a>'
                            if contact else "")
            parts.append(f'<li><a href="{website}">{name}</a>'
                         f'<br><span class="meta">{meta}{contact_link}</span></li>')
        parts.append("</ul>")

    parts.append("<footer>")
    parts.append("<p>Data: <a href=\"https://github.com/bg7bag/ham-radio-directory/blob/main/clubs.json\">"
                 "clubs.json</a> in this repository. Corrections welcome via pull request.</p>")
    parts.append(f"<p>Page generated from clubs.json · {today} · "
                 "Run by <a href=\"https://github.com/bg7bag\">BG7BAG</a></p>")
    parts.append("</footer>")
    parts.append("</main>")
    parts.append("</body>")
    parts.append("</html>")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts) + "\n")
    # Skip Jekyll processing on GitHub Pages.
    open(os.path.join(OUT_DIR, ".nojekyll"), "w").close()
    print(f"wrote site/index.html ({total} entries)")


if __name__ == "__main__":
    main()

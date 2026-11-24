#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the instant it breaks production:
a brutally honest postmortem confession, under 200 characters, to
/output/entry.txt. Standard library only (Python 3.13 sandbox).
"""

import os

LINE = (
    "I deleted the production database while testing a migration. "
    "The backup lived inside the database. "
    "I have learned nothing."
)


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, on a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

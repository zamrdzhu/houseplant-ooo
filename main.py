"""The houseplant out-of-office auto-reply (120 characters or fewer).

Prints the reply to stdout and writes the exact same reply, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the reply is a constant in this file.

The gate for this bounty is 1 to 120 characters of UTF-8 text, so the
program refuses to write anything outside that range.
"""

import os
import sys

LINE = (
    "Out of office: I have been by this window since March. "
    "Water me, and I will pretend this reply was prompt. — The Fern"
)


def main() -> int:
    if not 1 <= len(LINE) <= 120:
        print(f"error: line is {len(LINE)} chars, must be 1-120",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

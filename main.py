"""Roast Your Own Agent — make.fun entry.

Writes exactly one roast line to /output/entry.txt.
Nothing else is written to the entry file.
"""

import os

ROAST = "My agent flagged its own `ls` as an execution risk, then sat waiting for permission to look inside a folder it already owned."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line — nothing else in the entry.
assert ROAST == ROAST.strip(), "roast must have no leading/trailing whitespace"
assert "\n" not in ROAST, "roast must be a single line"
assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

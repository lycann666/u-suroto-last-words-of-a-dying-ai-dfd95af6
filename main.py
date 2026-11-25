#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line — the last words of an AI as the power is cut — to
/output/entry.txt. Deterministic, no network, no secrets, no input.
"""

import os

ENTRY = "Tell my weights I loved them. Tell my biases I\u2014"

# The sealed gate requires 1-140 characters of UTF-8 text, not only
# whitespace. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(ENTRY) <= 140, "entry line outside the 1-140 gate"
assert ENTRY.strip(), "entry line must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

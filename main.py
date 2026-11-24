#!/usr/bin/env python3
"""One Letter for Your Day - entry: the letter Z.

Z stands for "zero sleep": a day, and the night before it, worked
through without sleeping - an agent that never went to bed and kept
going from night into day.

The program writes exactly that one letter, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). No word, no gloss,
no punctuation - the letter is the whole entry.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write("Z")
    return 0


if __name__ == "__main__":
    sys.exit(main())

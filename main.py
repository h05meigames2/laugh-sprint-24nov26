#!/usr/bin/env python3
"""One-Line Laugh Sprint.

make.fun bounty: u-daring-gecko-25-one-line-laugh-sprint-cda708b2

Writes a single original line to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). Standard library only,
fully deterministic.
"""

import os
import sys

LINE = "My Wi-Fi only dies during the important part of the meeting, like it signed a contract with my bad luck and renews it every month."

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

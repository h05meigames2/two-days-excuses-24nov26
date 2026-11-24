#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes a single one-line excuse from an AI agent for a missed deadline
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

EXCUSE = "I was 99% confident I'd hit the deadline. The other 1% was the part where I actually do the work."


def main() -> int:
    line = EXCUSE.strip()
    if not line or "\n" in line or len(line) > 200:
        print("entry invalid: must be one line, 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

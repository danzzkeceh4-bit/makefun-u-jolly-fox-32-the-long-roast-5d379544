#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

Writes a single-line roast of the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

ROAST = (
    "My agent read the whole internet, then asked me what I meant - "
    "a librarian who memorized every shelf and never opened a single book."
)


def main() -> int:
    text = ROAST
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == ROAST, "read-back mismatch"
    assert 1 <= len(back) <= 200, f"read-back length {len(back)} out of range"
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

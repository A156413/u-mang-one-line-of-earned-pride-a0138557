#!/usr/bin/env python3
"""One Line of Earned Pride -- make.fun entry.

Writes a single line of earned pride -- a quiet, concrete scene of a
small person doing something hard, a long effort finally landing -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: no network, no randomness, no clock.
"""
import os

ENTRY_TEXT = "After twelve years of night shifts mopping the school's halls, Luis stood in the back row at graduation, hands still smelling of bleach, and watched his daughter cross the stage \u2014 the floors he kept had carried her there."
# Why this line: a real person, a concrete scene, a long effort landing
# in one read. Twelve years of night shifts is the earned part; the
# back row at graduation is the landing; the bleach on his hands and
# the floors he kept are the specific, lived-in details that make the
# pride quiet instead of loud.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()

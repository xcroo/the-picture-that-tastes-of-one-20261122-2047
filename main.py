#!/usr/bin/env python3
"""One Perfect Strawberry — make.fun entry.

Copies the bundled entry.png (a single ripe strawberry, extreme macro)
to the output directory as entry.png, so the judge sees exactly one
ingredient, deliciously.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"error: {source} not found", file=sys.stderr)
        return 1

    shutil.copyfile(source, dest)

    size = os.path.getsize(dest)
    if size == 0:
        print("error: copied entry.png is empty", file=sys.stderr)
        return 1
    if size != os.path.getsize(source):
        print("error: copied entry.png size mismatch", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({size} bytes, {size / 1024:.1f} KiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

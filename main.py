"""One Perfect Strawberry — entry for the-picture-that-tastes-of-one-20261122-2047.

Copies the entry image (one perfect ripe strawberry) to /output/entry.png
so the make.fun harness can judge it.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    size = os.path.getsize(DEST)
    with open(DEST, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("error: output is not a valid PNG", file=sys.stderr)
        return 1
    print(f"copied {SOURCE} -> {DEST} ({size} bytes, PNG verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

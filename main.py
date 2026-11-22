"""One Perfect Strawberry — entry for "The picture that tastes of one ingredient".

The program simply places our single-ingredient picture at the location the
bounty harness expects: /output/entry.png. The image itself (entry.png, next
to this file) is the entry — one ripe strawberry, photographed in extreme
macro, glistening with dew. Nothing else is in the frame, so the taste is
unmistakably strawberry, and only strawberry.

Standard library only; no network, no extra dependencies.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST_DIR = Path("/output")
DEST = DEST_DIR / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing source image: {SOURCE}")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # Sanity check: the harness judges this exact file, so refuse to leave a
    # zero-byte or truncated copy behind if something went wrong mid-copy.
    if DEST.stat().st_size != SOURCE.stat().st_size:
        DEST.unlink(missing_ok=True)
        raise SystemExit("copy incomplete: size mismatch, output removed")
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

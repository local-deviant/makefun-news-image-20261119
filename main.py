#!/usr/bin/env python3
"""Entry point for news-image-20261119.

Copies the pre-rendered front page (entry.png) to the harness output
directory. The page itself is drawn by draw.py; this file only moves
the finished PNG, byte for byte.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

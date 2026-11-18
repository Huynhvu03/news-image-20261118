#!/usr/bin/env python3
"""news-image-20261118 entry: copy the held front-page image to /output/entry.png.
Deterministic: identical bytes on every run. No network, no randomness."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()

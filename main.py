#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261118 bounty.

Copies the pre-made front-page image into /output/entry.png.
The image was generated with ChatGPT (image model) from the five
top-ranked front pages of this competition plus a full 40-story brief
for Wednesday 18 November 2026.

Deterministic: the same input bytes are copied on every run, so two
runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()

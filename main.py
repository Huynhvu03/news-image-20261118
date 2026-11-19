#!/usr/bin/env python3
"""Write the v5 front-page image to /output/entry.png.

The entry image lives next to this program as entry.jpg. This program
copies it, byte for byte, to /output/entry.png. Copying the same input
on every run means two runs always write identical bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()

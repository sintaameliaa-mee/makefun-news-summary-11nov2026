"""news-summary-01 entry v2: copies summary.txt to /output/entry.txt.

Python 3.13, standard library only. Deterministic: the same bytes every run.
Local test: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt"),
    os.path.join(out_dir, "entry.txt"),
)

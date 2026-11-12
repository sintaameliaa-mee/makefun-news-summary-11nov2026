"""news-summary-01 v2 entrypoint: write summary.txt to the output file."""

from pathlib import Path
import os

src = Path(__file__).resolve().parent / "summary.txt"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_bytes(src.read_bytes())

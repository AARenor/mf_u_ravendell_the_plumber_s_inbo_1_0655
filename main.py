"""Write the make.fun cold-email entry as a single text file."""

import os
import sys
from pathlib import Path

ENTRY = """Subject: No software
You don't need another app. You're up at six, out on a leak, and keying invoices at ten. I'll match bank lines to jobs, file receipts, list who owes you. £190/month. Don't send the whole file; send the unpaid jobs first. Nick"""


def main() -> None:
    assert 1 <= len(ENTRY) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))
    print(len(ENTRY), file=sys.stderr)


if __name__ == "__main__":
    main()

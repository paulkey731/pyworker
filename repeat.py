"""Run app.py once for every count stored on the first line of count.txt."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_count() -> int:
    first = (ROOT / "count.txt").read_text(encoding="utf-8").splitlines()[0].strip()
    count = int(first)
    if not 50 <= count <= 100:
        raise SystemExit(f"count must be from 50 to 100, got {count}")
    return count


def main() -> None:
    count = read_count()
    app = ROOT / "app.py"
    for number in range(1, count + 1):
        print(f"run {number} of {count}", flush=True)
        subprocess.check_call([sys.executable, str(app)])


if __name__ == "__main__":
    main()

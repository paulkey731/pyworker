"""Install packages listed in help.txt, then print helloworld."""

import subprocess
import sys
from pathlib import Path


def packages_from_help(path: Path) -> list[str]:
    packages = []
    for line in path.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if not name or name.startswith("#"):
            continue
        packages.append(name)
    return packages


def main() -> None:
    help_file = Path(__file__).with_name("help.txt")
    packages = packages_from_help(help_file)
    if packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])
    print("helloworld")


if __name__ == "__main__":
    main()

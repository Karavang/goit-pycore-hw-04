from pathlib import Path
from colorama import Fore, Style
import sys

startRoute = Path(sys.argv[1])


def sort_key(path: Path) -> str:
    return path.name.lower()


def commander(directory: Path, lvl: int = 0) -> None:
    items = sorted(directory.iterdir(), key=sort_key)
    for item in items:
        indent = "    " * lvl
        if item.is_dir():
            print(f"{indent}{Fore.YELLOW}{item.name}/{Style.RESET_ALL}")
            commander(item, lvl + 1)
        else:
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")


commander(startRoute)

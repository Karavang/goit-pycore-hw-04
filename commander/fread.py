from pathlib import Path
from colorama import Fore
from sys import argv


def fread():
    try:
        route = Path(argv[1])

        for path in route.iterdir():

            if path.suffix:
                print(Fore.BLUE, path)

            else:
                print(Fore.YELLOW, path)

    except:
        print("Не корректно вказаний роут")


fread()

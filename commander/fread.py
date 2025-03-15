from pathlib import Path
from colorama import Fore
from sys import argv

startRoute = Path(argv[1])


def fread(route):
    global startRoute
    # try:
    Path(route)
    contain = []
    for path in Path(route).iterdir():

        if path.suffix:
            print(Fore.BLUE, path)
            contain.append(str(path))

        else:
            print(Fore.YELLOW, path)
            startRoute = str(startRoute) + "/" + str(path)
            contain.append(fread(startRoute))
        print(contain)
    # except:
    #     print("Не корректно вказаний роут")


fread(startRoute)

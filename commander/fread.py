from pathlib import Path
from colorama import Fore
from sys import argv


def main():
    res = []
    startRoute = Path(argv[1])
    for e in startRoute.iterdir():
        print(e)
        print(e.is_dir())
        
        if(e.is_dir()):
            
        else:
            res.append(e)


main()

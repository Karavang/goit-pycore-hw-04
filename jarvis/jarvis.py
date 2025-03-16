from modules.parse_input import parse_input
from sys import argv
import os


def main():
    parsed = parse_input(argv[1])
    match parsed[0]:
        case "hello":
            print("How can I help you?")
        case "add":
            print("add")
        case "change":
            print("change")
        case "phone":
            print("phone")
        case "all":
            print("all")
        case "close" | "exit":
            try:
                os.system('pkill -f "code"')
            except:
                print("Failed to close the window")
        case _:
            print("Unknown command")


main()

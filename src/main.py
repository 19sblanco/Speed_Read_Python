import signal
import os
import platform
from pages.main_menu import main_menu 


"""
handles the ctrl-c signal
"""
def sigint_handler(sig, frame):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print("GoodBye!")
    exit(0)


"""
project plans in file todo and specifications.txt
"""
def main():
    signal.signal(signal.SIGINT, sigint_handler)
    mm = main_menu()


if __name__ == "__main__":
    main()


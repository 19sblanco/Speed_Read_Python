from abc import ABC, abstractmethod
import re
import os
import platform


class page(ABC):
    def __init__(self):
        self.clear_console()

    
    def display_options(self, options):
        for i in range(len(options)):
            print(f"{i}) " + str(options[i].get_name()))
    

    """
    n: int
    n is the option number to execute
    """
    def handle_input(self, n, options):
        options[n].action()


    """
    n: int
    n is the number of options
    we want an integer between [0, n)
    """
    def get_input(self, n, message="please select an option: "):
        pattern = rf'^(?:[0-9]|[1-9][0-9]*)$'
        while True:
            i = input(message)
            if re.match(pattern, i) and int(i) < n:
                break
            else:
                print(f"Error: Enter an integer between and including 0 and {n-1}")
        return int(i)


    def clear_console(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')





from abc import ABC, abstractmethod
import re
import os
import platform

class page(ABC):
    def __init__(self):
        self.clear_console()


    """
    n: int

    n is the number of options
    """
    def get_input(self, n):
        pattern = f"[0-{n}]"
        while True:
            i = input("please select an option: ")
            if re.match(pattern, i):
                break
        return i


    def clear_console(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')


    @abstractmethod
    def display_menu(self):
        pass


    @abstractmethod
    def display_options(self):
        pass


    @abstractmethod
    def handle_option(self, option):
        pass




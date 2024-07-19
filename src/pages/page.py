from abc import ABC, abstractmethod
import re
import os
import platform

class page(ABC):
    menu_options = []


    def __init__(self):
        self.clear_console()

    
    @abstractmethod
    def create_options(self):
        pass


    def display_options(self):
        mo = self.menu_options
        for i in range(len(mo)):
            print(f"{i}) " + str(mo[i].get_name()))
    

    """
    n: int
    n is the option number to execute
    """
    def handle_input(self, n):
        self.menu_options[n].action()


    """
    n: int
    n is the number of options
    """
    def get_input(self, n):
        pattern = f"[0-{n-1}]"
        while True:
            i = input("please select an option: ")
            if re.match(pattern, i):
                break
        return int(i)


    def clear_console(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')





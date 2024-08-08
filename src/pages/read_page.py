from pages.page import page
import time
import os
import json

class read_page(page):
    __READ_MENU = """
██████╗ ███████╗ █████╗ ██████╗ ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║
██████╔╝█████╗  ███████║██║  ██║██║
██╔══██╗██╔══╝  ██╔══██║██║  ██║╚═╝
██║  ██║███████╗██║  ██║██████╔╝██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝
"""
    __main_menu = None
    __lines = None
    __start_idx = None
    __lines_to_display = []
    __SAVE_FILE = "save.json"
    __speed = 5 # default speed


    def __init__(self, lines, start_idx, main_menu):
        super().__init__()
        self.__lines = lines
        self.__start_idx = start_idx
        self.__main_menu = main_menu
        print(self.__READ_MENU)
        self.load_settings()
        self.display()


    def display(self):
        for i in range(self.__start_idx, len(self.__lines)):
            self.__lines_to_display.append(self.__lines[i])
            super().clear_console()
            print(self.__READ_MENU)
            for j in range(len(self.__lines_to_display)):
                print(self.__lines_to_display[j])
            time.sleep(self.__speed)

            if len(self.__lines_to_display) == 10:
                last_line = self.__lines_to_display[-1]
                self.__lines_to_display = []
                self.__lines_to_display.append(last_line)

    
    def increase_speed(self):
        pass


    def decrease_speed(self):
        pass


    def load_settings(self):
        if os.path.exists(self.__SAVE_FILE):
            with open(self.__SAVE_FILE, "r") as save_file:
                self.__speed = json.load(save_file)["speed"]
        else:
            data = {
                "speed": self.__speed,
            }
            with open(self.__SAVE_FILE, "w") as save_file:
                json.dump(data, save_file, indent=4)
            self.__init__(self.__lines, self.__start_idx, self.__main_menu)
       





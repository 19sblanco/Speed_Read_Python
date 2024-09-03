from pages.page import page
import time
import os
import json
from pynput import keyboard


class read_page(page):
    __READ_MENU = """
██████╗ ███████╗ █████╗ ██████╗ ██╗         
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║         ↑ to speed up 
██████╔╝█████╗  ███████║██║  ██║██║         ↓ to slow down
██╔══██╗██╔══╝  ██╔══██║██║  ██║╚═╝
██║  ██║███████╗██║  ██║██████╔╝██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝
"""
    __main_menu = None
    __lines = None
    __curr_idx = None
    __lines_to_display = []
    __SAVE_FILE = "save.json"
    __speed = 5 # default speed
    __listener = None


    def __init__(self, lines, start_idx, main_menu):
        with keyboard.Listener(on_press=self.change_speed) as listener:
            listener.join()

        super().__init__()
        self.__lines = lines
        self.__curr_idx = start_idx
        self.__main_menu = main_menu
        print(self.__READ_MENU)
        self.load_settings()
        self.display()


    def display(self):
        for i in range(self.__curr_idx, len(self.__lines)):
            self.__curr_idx = i
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


    def change_speed(self, key):
        try:
            if key.char == 'up':
                print("Key Up pressed")
                self.__speed *= 1.1
                self.__display()
            elif key.char == 'down':
                print("Key Down pressed")
        except AttributeError:
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

       





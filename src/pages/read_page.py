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
        num_lines = 0
        for i in range(start_idx, len(lines)):
            print(lines[i])
            num_lines += 1
            time.sleep(self.__speed)
            if num_lines == 10:
                num_lines = 0
                super().clear_console()
                print(self.__READ_MENU)

    def display_lines(self):
        pass

    
    def update_lines(self):
        pass

    

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
       





"""
display 10 lines at a time
when you display a line, get rid of the top line and move everything up
    * keep a list of 10 lines to display
    * update the list each time
    * display lines


    def display lines

    def update lines

    def increase speed

    def decrease speed


display 10 lines, after 10th line is displayed put the 10th line at the top of the screen and start displaying other lines
"""
import json
import time
import os

from menu_option import menu_option
from pages.page import page


"""
TODO
display settings
? is it possible to only have this program edit that file?
"""

class settings_page(page):
    __SETTINGS_MENU = """
███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
"""

    __SAVE_FILE = "save.json"
    __main_menu = None
    __menu_options = None

    __speed = 5


    def __init__(self, main_menu):
        super().__init__()
        self.__menu_options = []
        self.__main_menu = main_menu
        print(self.__SETTINGS_MENU)
        self.load_settings()
        self.display_settings()
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)


    def save_settings(self):
        data = {
            "speed": self.__speed,
        }

        with open(self.__SAVE_FILE, "w") as save_file:
            json.dump(data, save_file, indent=4)
        print("save complete...")
        time.sleep(1)
        self.__init__(self.__main_menu)

    
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
            self.__init__(self.__main_menu)
       


    def display_settings(self):
        print("Speed: ", self.__speed)
        print()


    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Go to Main Menu",
                self.__main_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "Change Reading Speed",
                self.change_speed
            )
        )


    def change_speed(self):
        max_speed = 100
        self.__speed = super().get_input(max_speed, "new speed: ")
        self.save_settings()
        self.__init__(self.__main_menu)

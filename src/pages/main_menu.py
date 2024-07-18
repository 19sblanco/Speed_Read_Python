from pages.page import page
from pages.gospel_page import gospel_page
from pages.download_page import download_page
from pages.settings_page import settings_page

class main_menu(page):
    __MAIN_MENU = """
    ░██████╗██████╗░███████╗███████╗██████╗░██████╗░███████╗░█████╗░██████╗░
    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗
    ╚█████╗░██████╔╝█████╗░░█████╗░░██║░░██║██████╔╝█████╗░░███████║██║░░██║
    ░╚═══██╗██╔═══╝░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██╔══╝░░██╔══██║██║░░██║
    ██████╔╝██║░░░░░███████╗███████╗██████╔╝██║░░██║███████╗██║░░██║██████╔╝
    ╚═════╝░╚═╝░░░░░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
                                                    Created by Steven Blanco
    """

    __MAIN_MENU_INPUT = """
        0) Exit
        1) Read Gospel library
        2) Read Downloaded content
        3) Download content
        4) Settings
    """

    HIGHEST_OPTION = 4


    def __init__(self):
        super().__init__()
        self.display_menu()
        self.display_options()
        option = super().get_input(self.HIGHEST_OPTION)
        self.handle_option(option)


    def handle_option(self, option):
        if option == "0":
            print("Exiting, Thank you!")
        elif option == "1":
            gospel_page()
        elif option == "2":
            print("2")
        elif option == "3":
            download_page()
        elif option == "4":
            settings_page()
        print("Exiting, main menu!")


    def display_menu(self):
        print(self.__MAIN_MENU)


    def display_options(self):
        print(self.__MAIN_MENU_INPUT)

from menu_option import menu_option
from pages.page import page
from pages.gospel_page import gospel_page
from pages.online_content_page import online_content_page
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

    def __init__(self):
        super().__init__()
        print(self.__MAIN_MENU)
        self.create_options()
        super().display_options()
        n = len(super().menu_options)
        user_input = super().get_input(n)
        super().handle_input(user_input)


    def create_options(self):
        super().menu_options.append(
            menu_option(
                "Exit",
                self.exit_program
            )
        )
        super().menu_options.append(
            menu_option(
                "Read Gospel Library",
                gospel_page
            )
        )
        super().menu_options.append(
            menu_option(
                "Online Content",
                online_content_page
            )
        )
        super().menu_options.append(
            menu_option(
                "Settings",
                settings_page
            )
        )
            

    def exit_program(self):
        print("Thanks for reading!")
        exit()

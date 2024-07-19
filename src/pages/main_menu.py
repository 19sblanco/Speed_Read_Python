from menu_option import menu_option
from pages.page import page
from pages.gospel_page import gospel_page
from pages.online_content_page import online_content_page
from pages.settings_page import settings_page



"""
main_menu has all the data asscociated with displaying the main menu
"""
class main_menu(page):
    __MAIN_MENU = """
███████╗██████╗ ███████╗███████╗██████╗       ██████╗ ███████╗ █████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗      ██╔══██╗██╔════╝██╔══██╗██╔══██╗
███████╗██████╔╝█████╗  █████╗  ██║  ██║█████╗██████╔╝█████╗  ███████║██║  ██║
╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║╚════╝██╔══██╗██╔══╝  ██╔══██║██║  ██║
███████║██║     ███████╗███████╗██████╔╝      ██║  ██║███████╗██║  ██║██████╔╝
╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ 
                                                       Created by Steven Blanco
    """

    __menu_options = None


    def __init__(self):
        super().__init__()
        self.__menu_options = []
        print(self.__MAIN_MENU)
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)


    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Exit",
                self.exit_program
            )
        )
        self.__menu_options.append(
            menu_option(
                "Read Gospel Library",
                gospel_page,
                self.__init__
            )
        )
        self.__menu_options.append(
            menu_option(
                "Online Content",
                online_content_page,
                self.__init__
            )
        )
        self.__menu_options.append(
            menu_option(
                "Settings",
                settings_page,
                self.__init__
            )
        )
            

    def exit_program(self):
        super().clear_console()
        print("GoodBye!")
        exit()

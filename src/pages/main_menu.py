from pages.page import page

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
        pass


    def display_menu(self):
        print(self.__MAIN_MENU)


    def display_options(self):
        print(self.__MAIN_MENU_INPUT)

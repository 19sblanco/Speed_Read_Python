from pages.page import page


class settings_page(page):
    __SETTINGS_MENU = """
    █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
    ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█
    """

    __SETTINGS_MENU_INPUT = """
        0) Go back                                  
        1) Speed     
        2) Revert to Default settings
        3) More info about settings
    """

    HIGHEST_OPTION = 3

    def __init__(self):
        super().__init__()
        self.display_menu()
        self.display_options()
        option = super().get_input(self.HIGHEST_OPTION)
        self.handle_option(option)

    
    def handle_option(self, option):
        if option == "0":
            print("0")
        elif option == "1":
            print("1")
        elif option == "2":
            print("2")
        elif option == "3":
            print("3")


    def display_menu(self):
        print(self.__SETTINGS_MENU)


    def display_options(self):
        print(self.__SETTINGS_MENU_INPUT)

from pages.page import page


class gospel_page(page):
    __COLLECTION_MENU = """
    █▀█ █ █▀▀ █▄▀   ▄▀█   █▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█
    █▀▀ █ █▄▄ █░█   █▀█   █▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄▄ ░█░ █ █▄█ █░▀█
    """

    __COLLECTION_MENU_INPUT = """
        0) Go back
        1) Book of Mormon
        2) Bible Old Testament
        3) Bible New Testament
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
        print(self.__COLLECTION_MENU)


    def display_options(self):
        print(self.__COLLECTION_MENU_INPUT)

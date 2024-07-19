from menu_option import menu_option
from pages.page import page



class gospel_page(page):
    __COLLECTION_MENU = """
█▀█ █ █▀▀ █▄▀   ▄▀█   █▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█
█▀▀ █ █▄▄ █░█   █▀█   █▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄▄ ░█░ █ █▄█ █░▀█
    """

    __main_menu = None
    menu_options = None


    """
    main_menu is a pointer to the constructor for the main_menu object
    call this constructor will display the main menu page
    """
    def __init__(self, main_menu):
        super().__init__()
        self.menu_options = []
        self.__main_menu = main_menu
        print(self.__COLLECTION_MENU)
        self.create_options()
        super().display_options(self.menu_options)
        user_input = super().get_input(len(self.menu_options))
        super().handle_input(user_input, self.menu_options)


    def create_options(self):
        self.menu_options.append(
            menu_option(
                "Go to Main Menu",
                self.__main_menu
            )
        )
        self.menu_options.append(
            menu_option(
                "Book of Mormon",
                self.__main_menu
            )
        )
        self.menu_options.append(
            menu_option(
                "Bible Old Testament",
                self.__main_menu
            )
        )
        self.menu_options.append(
            menu_option(
                "Bible New Testament",
                self.__main_menu
            )
        )
    
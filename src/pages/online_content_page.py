from menu_option import menu_option
from pages.page import page


class online_content_page(page):
    __DOWNLOAD_MENU = """
 ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗               
██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝               
██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗                 
██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝                 
╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗               
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝               
                                                               
 ██████╗ ██████╗ ███╗   ██╗████████╗███████╗███╗   ██╗████████╗
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝
██║     ██║   ██║██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║   ██║   
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║   ██║   
╚██████╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║ ╚████║   ██║   
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                               """

    __main_menu = None
    __menu_options = None

    def __init__(self, main_menu):
        super().__init__()
        self.__menu_options = []
        self.__main_menu = main_menu
        print(self.__DOWNLOAD_MENU)
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)


    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Go to Main Menu",
                self.__main_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "Online Library",
                self.__main_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "Add New by URL",
                self.__main_menu
            )
        )


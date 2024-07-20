from menu_option import menu_option
from pages.page import page


class bom_page(page):
    __BOM_MENU = """
██████╗  ██████╗  ██████╗ ██╗  ██╗     ██████╗ ███████╗    
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔═══██╗██╔════╝    
██████╔╝██║   ██║██║   ██║█████╔╝     ██║   ██║█████╗      
██╔══██╗██║   ██║██║   ██║██╔═██╗     ██║   ██║██╔══╝      
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╔╝██║         
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝         
                                                           
███╗   ███╗ ██████╗ ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗ 
████╗ ████║██╔═══██╗██╔══██╗████╗ ████║██╔═══██╗████╗  ██║ 
██╔████╔██║██║   ██║██████╔╝██╔████╔██║██║   ██║██╔██╗ ██║ 
██║╚██╔╝██║██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║██║╚██╗██║ 
██║ ╚═╝ ██║╚██████╔╝██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║ 
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ 
"""
    
    __previous_menu = None
    __menu_options = None

    def __init__(self, previous_menu):
        super().__init__()
        self.__menu_options = []
        self.__previous_menu = previous_menu
        print(self.__BOM_MENU)
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)

    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Go back",
                self.__previous_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY",
                self.read_book,
                "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY"
            )
        )
        pass

    def read_book(self, book_title):
        # open bom
        with open("")
        # set pointer to book title
        # open read page
        # pass the pointer and file along
        pass


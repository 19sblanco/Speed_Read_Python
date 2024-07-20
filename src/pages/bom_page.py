import re
from menu_option import menu_option
from pages.page import page
from pages.read_page import read_page


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
    __book_list = [
        "THE FIRST BOOK OF NEPHI HIS REIGN AND MINISTRY",
        "THE SECOND BOOK OF NEPHI",
        "THE BOOK OF JACOB",
        "THE BOOK OF ENOS",
        "THE BOOK OF JAROM",
        "THE BOOK OF OMNI",
        "THE WORDS OF MORMON",
        "THE BOOK OF MOSIAH",
        "THE BOOK OF ALMA",
        "THE BOOK OF HELAMAN",
        "THIRD BOOK OF NEPHI",
        "FOURTH NEPHI",
        "THE BOOK OF MORMON",
        "THE BOOK OF ETHER",
        "THE BOOK OF MORONI",
    ]

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
        for i in range(len(self.__book_list)):
            self.__menu_options.append(
                menu_option(
                    self.__book_list[i],
                    self.read_book,
                    self.__book_list[i]
                )
            )


    def read_book(self, book_title):
        # open bom
        with open("texts/gospel_text/BookofMormon.txt", "r") as bom_file:
            text = bom_file.read()
            m = re.search(book_title, text)
            # set pointer to book title
            pointer = m.start()
            # open read page
            read_page(text, pointer)

            # pass the pointer and file along


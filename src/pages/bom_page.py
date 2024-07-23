from pages.collection_page import collection_page


class bom_page(collection_page):
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

    __menu_options = None

    def __init__(self, menu_list):
        super().__init__()
        self.__menu_options = []
        print(self.__BOM_MENU)
        super().create_options(self.__menu_options, "BookofMormon", self.__book_list, menu_list[0], menu_list[1])
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)

from pages.collection_page import collection_page


class old_testament_page(collection_page):
    __OLD_TESTAMENT_MENU = """
 ██████╗ ██╗     ██████╗     ████████╗███████╗███████╗████████╗ █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
██╔═══██╗██║     ██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██║   ██║██║     ██║  ██║       ██║   █████╗  ███████╗   ██║   ███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██║   ██║██║     ██║  ██║       ██║   ██╔══╝  ╚════██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
╚██████╔╝███████╗██████╔╝       ██║   ███████╗███████║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
 ╚═════╝ ╚══════╝╚═════╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""
    __book_list = [
        "The First Book of Moses:  Called Genesis",
        "The Second Book of Moses:  Called Exodus",
        "The Third Book of Moses:  Called Leviticus",
        "The Fourth Book of Moses:  Called Numbers",
        "The Fifth Book of Moses:  Called Deuteronomy",
        "The Book of Joshua",
        "The Book of Judges",
        "The Book of Ruth",
        "The First Book of Samuel",
        "The Second Book of Samuel",
        "The First Book of the Kings",
        "The Second Book of the Kings",
        "The First Book of the Chronicles",
        "The Second Book of the Chronicles",
        "Ezra",
        "The Book of Nehemiah",
        "The Book of Esther",
        "The Book of Job",
        "The Book of Psalms",
        "The Proverbs",
        "Ecclesiastes",
        "The Song of Solomon",
        "The Book of the Prophet Isaiah",
        "The Book of the Prophet Jeremiah",
        "The Lamentations of Jeremiah",
        "The Book of the Prophet Ezekiel",
        "The Book of Daniel",
        "Hosea",
        "Joel",
        "Amos",
        "Obadiah",
        "Jonah",
        "Micah",
        "Nahum",
        "Habakkuk",
        "Zephaniah",
        "Haggai",
        "Zechariah",
        "Malachi",
    ]

    __menu_options = None

    def __init__(self, menu_list):
        super().__init__(self.__OLD_TESTAMENT_MENU, self.__menu_options, "BibleOldTestament", self.__book_list, menu_list[0], menu_list[1])

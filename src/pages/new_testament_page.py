from pages.collection_page import collection_page


class new_testament_page(collection_page):
    __NEW_TESTAMENT_MENU = """
███╗   ██╗███████╗██╗    ██╗    ████████╗███████╗███████╗████████╗ █████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
████╗  ██║██╔════╝██║    ██║    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██╔██╗ ██║█████╗  ██║ █╗ ██║       ██║   █████╗  ███████╗   ██║   ███████║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██║╚██╗██║██╔══╝  ██║███╗██║       ██║   ██╔══╝  ╚════██║   ██║   ██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║ ╚████║███████╗╚███╔███╔╝       ██║   ███████╗███████║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""

    __book_list = [
        "The New Testament of the King James Bible",
        "The Gospel According to Saint Matthew",
        "The Gospel According to Saint Mark",
        "The Gospel According to Saint Luke",
        "The Gospel According to Saint John",
        "The Acts of the Apostles",
        "The Epistle of Paul the Apostle to the Romans",
        "The First Epistle of Paul the Apostle to the Corinthians",
        "The Second Epistle of Paul the Apostle to the Corinthians",
        "The Epistle of Paul the Apostle to the Galatians",
        "The Epistle of Paul the Apostle to the Ephesians",
        "The Epistle of Paul the Apostle to the Philippians",
        "The Epistle of Paul the Apostle to the Colossians",
        "The First Epistle of Paul the Apostle to the Thessalonians",
        "The Second Epistle of Paul the Apostle to the Thessalonians",
        "The First Epistle of Paul the Apostle to Timothy",
        "The Second Epistle of Paul the Apostle to Timothy",
        "The Epistle of Paul the Apostle to Titus",
        "The Epistle of Paul the Apostle to Philemon",
        "The Epistle of Paul the Apostle to the Hebrews",
        "The General Epistle of James",
        "The First Epistle General of Peter",
        "The Second General Epistle of Peter",
        "The First Epistle General of John",
        "The Second Epistle General of John",
        "The Third Epistle General of John",
        "The General Epistle of Jude",
        "The Revelation of Saint John the Divine",
    ]

    __menu_options = None

    def __init__(self, menu_list):
        super().__init__(self.__NEW_TESTAMENT_MENU, self.__menu_options, "BibleNewTestament", self.__book_list, menu_list[0], menu_list[1])

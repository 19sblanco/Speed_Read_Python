import re
from menu_option import menu_option
from pages.page import page
from pages.read_page import read_page

"""
Parent class to the biblical collections (Book of Mormon, Old and New Testament)
"""
class collection_page(page):
    def __init__(self, menu, menu_options, collection_name, book_list, main_menu, previous_menu):
        super().__init__()
        print(menu)
        menu_options = []
        self.create_options(menu_options, collection_name, book_list, main_menu, previous_menu)
        super().display_options(menu_options)
        user_input = super().get_input(len(menu_options))
        super().handle_input(user_input, menu_options)

    def create_options(self, menu_options, collection_title, book_list, main_menu, previous_menu):
        menu_options.append(
            menu_option(
                "Go to Main Menu",
                main_menu
            )
        )
        menu_options.append(
            menu_option(
                "Go back",
                previous_menu,
                main_menu
            )
        )
        for i in range(len(book_list)):
            menu_options.append(
                menu_option(
                    book_list[i],
                    self.read_book,
                    [collection_title, book_list[i], main_menu]
                )
            )


    def read_book(self, arguments):
        collection_name = arguments[0]
        book_name = arguments[1]
        with open(f"texts/gospel_text/{collection_name}.txt", "r") as bom_file:
            lines = bom_file.read().split("\n")
            idx = None
            for i in range(len(lines)):
                if re.search(arguments[1], lines[i]):
                    idx = i
            what_users_reading = collection_name + "_" + book_name
            read_page(what_users_reading, lines, idx, arguments[2])


import re
from menu_option import menu_option
from pages.page import page
from pages.read_page import read_page

class collection_page(page):
    def __init__(self, menu, menu_options, collection_name, book_list, main_menu, previous_menu):
        super().__init__()
        print(menu)
        self.create_options(menu_options, collection_name, book_list, main_menu, previous_menu)
        super().display_options(menu_options)
        user_input = super().get_input(len(menu_options))
        super().handle_input(user_input, book_list)

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
                    [collection_title, book_list[i]]
                )
            )


    def read_book(self, title_list):
        with open(f"texts/gospel_text/{title_list[0]}.txt", "r") as bom_file:
            text = bom_file.read()
            m = re.search(title_list[1], text)
            pointer = m.start()
            read_page(text, pointer)


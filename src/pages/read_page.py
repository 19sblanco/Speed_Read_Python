from pages.page import page

class read_page():
    __main_menu = None

    def __init__(self, text, pointer, main_menu):
        self.__main_menu = main_menu
        print("in read_page")
        print(pointer)
        print(text[pointer:pointer+100])
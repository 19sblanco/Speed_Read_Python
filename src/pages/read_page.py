from pages.page import page

class read_page():
    def __init__(self, text, pointer):
        print("in read_page")
        print(pointer)
        print(text[pointer:pointer+100])
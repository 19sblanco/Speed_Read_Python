from pages.page import page
import time

class read_page(page):
    __READ_MENU = """
██████╗ ███████╗ █████╗ ██████╗ ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║
██████╔╝█████╗  ███████║██║  ██║██║
██╔══██╗██╔══╝  ██╔══██║██║  ██║╚═╝
██║  ██║███████╗██║  ██║██████╔╝██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝
"""
    __main_menu = None

    def __init__(self, lines, start_idx, main_menu):
        super().__init__()
        self.__main_menu = main_menu
        print(self.__READ_MENU)
        # TODO: load settings
        num_lines = 0
        for i in range(start_idx, len(lines)):
            print(lines[i])
            num_lines += 1
            time.sleep(2)
            if num_lines == 10:
                num_lines = 0
                super().clear_console()
                print(self.__READ_MENU)


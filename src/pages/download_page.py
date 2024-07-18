from pages.page import page


class download_page(page):
    __DOWNLOAD_MENU = "Welcome to download page"

    __DOWNLOAD_MENU_INPUT = "Please enter a url"

    def __init__(self):
        super().__init__()
        self.display_menu()
        self.display_options()
        url = self.get_url()
        self.handle_option(url)


    def get_url(self):
        url = input("Enter a url")
        return url

    
    def handle_option(self, option):
        print("url: " + option)
        print("getting url from the web...")


    def display_menu(self):
        print(self.__DOWNLOAD_MENU)


    def display_options(self):
        print(self.__DOWNLOAD_MENU_INPUT)


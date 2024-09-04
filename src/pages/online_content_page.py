from menu_option import menu_option
from pages.page import page
from pages.online_library_page import online_library_page
import requests
from bs4 import BeautifulSoup
import re


class online_content_page(page):
    __DOWNLOAD_MENU = """
 ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗               
██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝               
██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗                 
██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝                 
╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗               
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝               
                                                               
 ██████╗ ██████╗ ███╗   ██╗████████╗███████╗███╗   ██╗████████╗
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝
██║     ██║   ██║██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║   ██║   
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║   ██║   
╚██████╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║ ╚████║   ██║   
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""

    __main_menu = None
    __menu_options = None

    def __init__(self, main_menu):
        super().__init__()
        self.__menu_options = []
        self.__main_menu = main_menu
        print(self.__DOWNLOAD_MENU)
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)


    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Go to Main Menu",
                self.__main_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "Online Library",
                online_library_page,
                [self.__init__, self.__main_menu]
            )
        )
        self.__menu_options.append(
            menu_option(
                "Add New Content by URL",
                self.add_by_url
            )
        )

    def add_by_url(self):
        while True:
            try:
                url = input("Enter a url: ")
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')

                break
            except:
                print("Invalid url")
        
        # get title and content removing excessive white space
        title = soup.h1.get_text().strip()
        content = ""
        all_ps = soup.find_all('p')
        for p in all_ps:
            content += p.get_text()
        content = content.replace("\n", "").replace("\r", "")
        content = re.sub(r" {4,}", " ", content)

        # format content into consistant line lengths
        formatted_content = ""
        text_length = 65 
        new_line = False
        for i in range(len(content)):
            formatted_content += content[i]
            if i % text_length == 0:
                new_line = True
            if new_line == True and (content[i] == " " or content[i] == "\t"):
                formatted_content += "\n"
                new_line = False
        
        # save to file
        file_name = "texts/uploaded_text/" + title.strip().replace(" ", "_") + ".txt"
        with open(file_name, "w") as file:
            file.write(title)
            file.write(formatted_content)
        
        self.__init__(self.__main_menu)










"""
Please enter a url: <url>

process the url with beautiful soup and get
    * <h1>
    * <p>
format text 
    * make text 70 wide
    1) get rid of new lines
    2) 
save text in file named <h1> "replace space with '_'"
"""
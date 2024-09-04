from menu_option import menu_option
from pages.page import page
from pages.read_page import read_page
import time
import os


class online_library_page(page):
    __library_menu = """
 ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗    
██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝    
██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗      
██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝      
╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗    
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝    
                                                    
██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
"""
    __online_content = None
    __menu_options = None
    __main_menu = None

    def __init__(self, args):
        super().__init__()
        self.__online_content = args[0]
        self.__main_menu = args[1]
        self.__menu_options = []
        print(self.__library_menu)
        self.create_options()
        super().display_options(self.__menu_options)
        user_input = super().get_input(len(self.__menu_options))
        super().handle_input(user_input, self.__menu_options)


    def create_options(self):
        self.__menu_options.append(
            menu_option(
                "Go back",
                self.__online_content,
                self.__main_menu
            )
        )
        self.__menu_options.append(
            menu_option(
                "Remove content",
                self.remove_content,
            )
        )
        dir_path = "texts/uploaded_text/"
        for filename in os.listdir(dir_path):
            filepath = dir_path + filename
            self.__menu_options.append(
                menu_option(
                    filename,
                    self.read_book,
                    [filepath, filename]
                )
            )

    
    def remove_content(self):
        print("Enter number associated with content to remove")
        user_input = super().get_input(len(self.__menu_options))
        if user_input == 1:
            user_input = 0
        if user_input == 0:
            super().handle_input(user_input, self.__menu_options)
        
        content_name = self.__menu_options[user_input].get_name()
        file_path = "texts/uploaded_text/" + content_name
        try:
            os.remove(file_path)
            print("File has been deleted successfully")
        except FileNotFoundError:
            print("File does not exist")
        except PermissionError:
            print("Permission denied: cannot delete")
        except Exception as e:
            print(f"An error occurred while deleting: {str(e)}")
        time.sleep(2)
        args = [self.__online_content, self.__main_menu]
        self.__init__(args)

        

    def read_book(self, args):
        filepath = args[0]
        filename = args[1]
        with open(filepath, "r") as file:
            lines = file.read().split("\n")
            idx = 0
            read_page(filename, lines, idx, self.__main_menu)

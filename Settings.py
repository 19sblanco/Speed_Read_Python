import json
import re
import time
from os import system, name, get_terminal_size



class Settings:
    SETTINGS_MENU = """
    █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
    ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█
        0) Go back                                  
        1) Speed     {0}                            
        2) Page size {1}
        3) Revert to Default settings
        i) More info about settings
    """

    speed = None
    lineNumber = None
    bookFilePath = None
    pageSize = None
    update = None
    exit = None

    temperaryState = ""

    def __init__(self):
        self.speed = 5000
        self.lineNumber = 0
        self.bookFilePath = ""
        self.pageSize = 10
        self.update = False
        self.exit = False


    def changeSettings(self):
        try:
            self.clearConsole()
            print(self.SETTINGS_MENU.format(self.speed, self.pageSize))
            choice = self.getInput("[0-3]|i", "")
            
            if choice == "0":
                self.exit = True
            elif choice == "1":
                self.changeSpeed()
            elif choice == "2":
                self.changePageSize()
            elif choice == "3":
                self.revert()
            elif choice == "i":
                self.explainSettings()

            if not self.exit:
                self.changeSettings()
            self.exit = False

        except:
            print("Error Occurred")
            time.sleep(2000)


    def explainSettings(self):
        self.clearConsole()
        print("""
Speed:
    The number of milliseconds that a line will display for 

    ***
    1000 milliseconds are in  1 second, meaning...
    500  milliseconds is  1/2 a second, and
    5000 milliseconds is  5   seconds
    
Page size:  
    This determines how many vertical lines of space in which text will print down (page size)

    ***
    Page Size = 1: display each line of text on the same line.
    Page Size = 10: starting at the top of the window, display the
    first line of text. Next frame display the second line of 
    text a line below the first. Simularly the third will print under the
    second and so on, continuing to 10. After the 10th, the next line will print
    at the top of the page repeating the cycle.

Revert to default:  
    Reverts the settings to their default values and removes bookmark

    ***
    speed = 5000
    Page size = 10
""")
        message = "Enter i to go back"
        print(message)
        while self.getInput("i", message) != "i":
            pass


    def changeSpeed(self):
        print("How many milliseconds per line would you like? [1 to 10,000]");
        self.speed = int(self.getInput("^([1-9][0-9]{0,3}|10000)$", ""))
        self.save()


    def changePageSize(self):
        useableHeight = get_terminal_size() - 12
        print(f"What would you like the page size to be? [1 to {useableHeight}]")
        
        while True:
            choice = int(self.getInput("[0-9]+", ""))
            
            if choice <= useableHeight:
                break
            
            print(f"Page size must be between 1 and {useableHeight}")

        self.pageSize = choice
        self.save()

        

    def maxPageSize(self):
        if get_terminal_size() > 12:
            self.pageSize = get_terminal_size() - 12
        else:
            self.pageSize = 1


    def getInput(self, pattern, message):
        while True:
            choice = input("")
            if re.search(pattern, choice):
                break
            else:
                if message == "":
                    print("Invalid input")
                else:
                    print(message)

        return choice


    def revert(self):
        self.speed = 5000
        self.lineNumber = 0
        self.bookFilePath = ""
        self.pageSize = 10
        self.update = False
        self.exit = False
        self.save()


    def save(self):
        print("temp save method", self.toJson())


    def saveState(self):
        self.temperaryState = self.toJson()


    def getOldState(self):
        return self.temperaryState


    def hasValidPath(self):
        # todo: impliment this
        pass


    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


    def clearConsole(self):
        if name == "nt": # clear for windows
            system("cls")
        else: # clear for linux and mac
            system("clear")


s = Settings()
s.changeSettings()


# test this file using inputs and checking the json printing output
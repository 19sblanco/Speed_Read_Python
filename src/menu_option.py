"""
menu_option represents all the data and functionality 
associated with an option on the menu
"""
class menu_option():
    __name = None
    __function = None
    __parameters = None
    

    def __init__(self, name, function, parameters=None):
        self.__name = name
        self.__function = function
        if parameters != None:
            self.__parameters = parameters

    
    def get_name(self):
        return self.__name


    def action(self):
        if self.__parameters != None:
            self.__function(self.__parameters)
        else:
            self.__function()

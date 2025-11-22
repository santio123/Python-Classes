# constructor

class iostring:
    def __init__(self):
        self.str1 = ""
    def getstr(self):
        self.str1 = input("enter the string : ")
    def print_str(self):
        print(f"The upper case of {self.str1} is {self.str1.upper()}")


obj1 = iostring()
obj1.getstr()
obj1.print_str()


# computer price

class price:
    def __init__(self):
        self.__maxprice = 800

    def setmaxprice(self,p):
        self.__maxprice = p

    def displaymaxprice(self):
        print("the max price is",self.maxprice)

computer = price()
computer.displaymaxprice()

computer.__maxprice = 1000
computer.displaymaxprice()

computer.setmaxprice(1200)
computer.displaymaxprice()
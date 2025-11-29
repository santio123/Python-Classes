# private variables

class A:
    __priv_var = 20

    def __priv_meth(self):
        print("the value is",self.__priv_var)
    
    def hello(self):
        print("the value is",self.__priv_var)

obj1 = A()
obj1.hello()
#obj1.__priv_meth()
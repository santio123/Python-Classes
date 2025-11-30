# abstract class

from abc import ABC ,abstractmethod
class abcclass(ABC):
    def printx(self,x):
        print("the value is",x)

    @abstractmethod
    def task(self):
        pass

class inh(abcclass):
    def task(self):
        print("I am from inherited class")

obj1 = inh()
obj1.task()
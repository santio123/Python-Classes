# Class Animal
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I use my legs to walk and run")

class Snake(animal):
    def move(self):
        print("I move my slithering")

class Fish(animal):
    def move(self):
        print("I use my fins to move by swimming")

h1 = Human()
h1.move()

s1 = Snake()
s1.move()

f1 = Fish()
f1.move()


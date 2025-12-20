# vehicle polymorphism

class BMW:
    def name(self):
        print("BMW")
    
    def typeofcar(self):
        print("Normal car")


class Ferrari:
    def name(self):
        print("Ferrari")
    
    def Typeofcar(self):
        print("Race car")


obj1 = BMW()
obj2 = Ferrari()
for car in (obj1,obj2):
car.name()
car.Typeofcar()
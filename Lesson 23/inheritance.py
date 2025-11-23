# Inheritance

class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
    
class bus(vehicle):
    pass

b1 = bus('volovo','1110km/h','12km/h')
print("the name of the bus is",b1.name)
print("the maxspeed is",b1.maxspeed)
print("the mileage is",b1.mileage)

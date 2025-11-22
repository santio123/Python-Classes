# constructor and destructor

class employee:
    def __init__(self,name):
        self.name = name
        print(self.name,"initialized")

    def __del__(self):
        print(self.name,"destructed")

emp1 = employee("employee1")
del emp1
emp2 = employee("employee2")
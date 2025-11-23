# Employee inheritance

class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print("My name is",self.name)
        print("My id is",self.id)

class employee(person):
    def __init__(self,name,id,salary,post):
        person.__init__(self,name,id)
        self.post = post
        self.salary = salary
    def display_emp(self):
        self.display()
        print("My salary is",self.salary)
        print("My post is",self.post)

emp1 = employee("Rakesh","122762632",'300000','Engineer')
emp1.display_emp()

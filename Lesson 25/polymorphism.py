# polymorphism

class India:
    def capital(self):
        print("The capital city of India is New Delhi")
    
    def language(self):
        print("the widely spoken language of India is Hindi")

    def climate(self):
        print("The climate of India is mostly hot")

class USA:
    def capital(self):
        print("The capital city of USA is Washington DC")
    
    def language(self):
        print("the language of USA is English")

    def climate(self):
        print("The climate of USA is mostly Cool")

obj1 = india()
obj2 = USA()
for country in (obj1,obj2):
country.capital()
country.language()
country.climate()
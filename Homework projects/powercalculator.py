# power calculator

a = int(input("enter the base : "))
b = int(input("enter the power : "))

res = 1

for i in range(b):
    res = res* a


    print(f"the answer to {a} power {b} is {res}")

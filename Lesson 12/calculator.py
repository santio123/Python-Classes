# calculator

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

ch = input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \nEnter your choice(1-4) : ")
n1 = int(input("Enter the number 1 : "))
n2 = int(input("Enter the number 2 : "))
if ch == "1":
    print(f"{n1} + {n2} = {add(n1,n2)}")
elif ch == "2":
    print(f"{n1} - {n2} = {sub(n1,n2)}")
elif ch == "3":
    print(f"{n1} * {n2} = {mul(n1,n2)}")
elif ch == "4":
    print(f"{n1} / {n2} = {div(n1,n2)}")

else:
    print("Invalid input")
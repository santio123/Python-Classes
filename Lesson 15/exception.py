# exception
try:
    n = int(input("enter the number : "))
    print(n)
except ValueError as ex:
    print("an exception occured",ex)

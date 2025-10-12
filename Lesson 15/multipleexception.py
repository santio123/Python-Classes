# Multiple Exception

try:
    n1, n2 = eval(input("enter two numbers seperated by commas"))
    result = n1/n2
    print(result)
except SyntaxError as ex:
    print("an exception occured",ex)
except ZeroDivisionError as ex:
    print(ex)
except :
    print("an error occured")
else:
    print("No error")
finally:
    print("I will always be there")
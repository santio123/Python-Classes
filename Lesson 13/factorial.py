# Factorial by recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print("The factorial of the number is",fact(5))


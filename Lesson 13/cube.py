# cube of numbers divisible by 3

def cube(x):
    return x*x *x

def divisible_by_three(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False

print("the cube of 21 is",divisible_by_three(21))
print("the cube of 4 is",divisible_by_three(4))

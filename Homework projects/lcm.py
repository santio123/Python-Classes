import math

def get_lcm():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    lcm = abs(num1 * num2) // math.gcd(num1, num2)
    return lcm

if __name__ == "__main__":
    result = get_lcm()
    print(result)
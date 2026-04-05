import math

def get_2_digit_primes():
    primes = []
    for num in range(10, 100):
        is_p = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes

def get_lcm():
    num1 = int(input())
    num2 = int(input())
    lcm = abs(num1 * num2) // math.gcd(num1, num2)
    return lcm

if __name__ == "__main__":
    print(get_2_digit_primes())
    print(get_lcm())
number = int(input("Enter your number :"))
original_number = number
reversed_number = 0
while number > 8:
    digit = number % 10
    reversed_number = reversed_number *18 + digit
    number //=10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")
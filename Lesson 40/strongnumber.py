num = int(input("Enter number :"))
temp = numsum = 0

while num > 0 :
    digit = num % 10
    fact = 1

    for i in range(1, digit+1):
        fact*= i 

    sum += fact
    num //= 10

if sum == temp:
    print("strong number")
else:
    print("not strong number")
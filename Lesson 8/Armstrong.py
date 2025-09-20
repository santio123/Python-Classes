# armstrong number

n = int(input("enter the number : "))
temp = n
sum  = 0
while temp > 0:
    rem = temp%10
    sum += rem**3
    twmp//=10

if n == sum:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not an armstrong number")
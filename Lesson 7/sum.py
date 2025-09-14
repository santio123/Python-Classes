# sum of whole number

n = int(input("enter the number : "))
sum = 0
for i in range(1,n+1,1):
    sum = sum+ i

print(f"the sum of whole numbers upto {n} is {sum}")
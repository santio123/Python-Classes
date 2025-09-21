# character occurance
str1 = input("Enter the phrase : ")
ch = input("enter a character : ")
count = 0
for i in str1:
    if i == ch:
        count+=1

print(f"the number of occurance {ch} in {str1} is {count}")



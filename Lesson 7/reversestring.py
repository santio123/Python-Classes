# reverse a string

str1 = input("enter the phrase : ")

rev = ""
for i in str1:
    rev = i+ rev

print(f"the reverse of the {str1} is {rev}")
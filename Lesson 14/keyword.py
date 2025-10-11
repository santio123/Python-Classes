# checking if alphabte 'A' is present or not

str1 = input("Enter the phrase : ")

for i in str1:
    if i.lower() == 'a':
        print("a is present in",str1)
        break
else:
    print("a is not in",str1)

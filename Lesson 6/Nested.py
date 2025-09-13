# Nested conditional statements

mc = input("Do you have a medical cause (y/n) : ")
if mc.lower() == 'y':
    print("you are allowed to write the exam")
else:
    att = int(input("enter your attendance : "))
    if att > 75:
        print("you are allowed to write the exam")
    else:
        print("you are not allowed to write the exam")
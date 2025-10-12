# checking for even no

flag = False
while not flag:
    try:
        n = int(input("enter the number : "))
        while n%2 == 0:
            print("BYE,BYE")
        print("the no is odd")
        flag = True
    except:
        print("invalid")
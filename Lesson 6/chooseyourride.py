# Choose your ride

choice1 = input("\n1.Bike\n2.Car \nEnter your choice(1/2) : ")
if choice1 == "1":
    choice2 = input("\n1.Yamaha\n2.scooty \nEnter your choice(1/2) : ")
    if choice2 == "1":
        print("You have selected Yamaha")
    elif choice2 == "2":
        print("You have selected scooty")
    else:
        print("invalid choice")
if choice1 == "2":
    choice2 = input("\n1.Toyato\n2.BMW \nEnter your choice(1/2) : ")
    if choice2 == "1":
        print("You have selected Toyato")
    elif choice2 == "2":
        print("You have selected BMW")
else:
    print("invalid choice")
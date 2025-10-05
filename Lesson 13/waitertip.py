# tip to the waiter

def tip_waiter(amt,per):
    tip = amt * per /100
    bamt = amt + tip
    print("The total amt is $",bamt)

amt = float(input("Enter the amt : "))
per = int(input("Enter the tip percentage : "))

tip_waiter(amt,per)
# calculate due amount

def due_amount(amount,paid):
    da = amount-paid
    
    print("The due amount is",da)

n = int(input("enter the bill amount : "))
a = int(input("enter the amount paid : "))

due_amount(n,a)


# profit or loss

cp = float(input("enter the price of the item : "))
sp = float(input("enter the selling price of the item : "))

if cp < sp:
    print(f"${sp-cp} is the profit!!!")
else:
    print(f"${cp-sp} is the loss!!!")
numberlargest = int(input("Enter the number :"))
numbersmallest = int(input("Enter smallest number :"))

while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore

print("HCF is :",numberlargest)
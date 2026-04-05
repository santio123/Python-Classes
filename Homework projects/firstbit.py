def firstSetBit(n):
	return n & -n

number = int(input("Enter your number : "))
print("Rightmost set bit:", firstSetBit(number))
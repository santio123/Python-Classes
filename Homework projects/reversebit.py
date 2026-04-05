def reverseBits(n):
	result = 0

	while(n > 0):
		result = (result << 1) | (n & 1)
		n = n >> 1

	return result

number = int(input("Enter your number : "))
print("Reversed bits number:", reverseBits(number))
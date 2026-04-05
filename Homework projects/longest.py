def longestOnes(n):
	max_count = 0
	count = 0

	while(n > 0):
		if(n & 1):
			count += 1
			if(count > max_count):
				max_count = count
		else:
			count = 0
		n = n >> 1

	return max_count

number = int(input("Enter your number : "))
print("Longest consecutive 1's:", longestOnes(number))
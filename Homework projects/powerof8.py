def powerOf8(number):
	if(number<=0):
		return False
	if(number&(number-1)):
		return False

	count=0
	while(number>1):
		number>>=1
		count+=1

	if(count%3==0):
		return True
	else:
		return False

number=int(input("Enter your number : "))
if(powerOf8(number)):
	print(number,"is a power of 8")
else:
	print(number,"is not a power of 8")
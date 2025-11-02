#palindrome

def palindrome(tuple1):
    s = 0
    e = len(tuple1)-1
    while (s < e):
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1 = (1,2,3,4,2,1)
if palindrome(tuple1):
    print("it is a palindrome")
else:
    print('it is not a palindrome')

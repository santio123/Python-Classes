# revrse order 10 - 1 and skip 5

print("the numbers in reverse order skipping 5")
for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)

# check the frequency

dic1 = {"coding" : 2, "drink" : 4, "food" : 2,"game" : 2, "table" : 3}

k = 2
count = 0
for value in dic1.values():
    if value == k:
        count +=1

print(f"the count of words which has {k} frequency is {count}")

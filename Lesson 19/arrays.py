# arrays 

import array as arr

a = arr.array("i",[12,34,56,7889,90,90])
print(a)

a.append(100)
print(a)
print("the no of elements counted are",a.count(90))
a.reverse()
print(a)

a.insert(3,1000)
print(a)

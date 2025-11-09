# map function

list1 = [12,35,67,89,13]
list2 = [24,26,74,34,14]
print("addition of two lists")
add_list = map(lambda x,y : x + y,list1,list2)
print(list(add_list))

def sqr(x):
    return x* x
print("the square list")
sqr_list = map(sqr,list1)
print(list(sqr_list))

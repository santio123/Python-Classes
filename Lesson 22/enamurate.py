# enumerate
class pair_elements:

    def two_sum(self,tuple1,target):

        lookup = {}
        sum = 0
        for i,value in enumerate(tuple1):
            sum = sum + value
            lookup[i] =sum
            if sum>= target:
                print(f"we got the {target} at the index number {i}")
                break
        
        print(lookup)

p1 = pair_elements()
tuple1 = (10,20,30,40,50,60,70,80)
target = 100
p1.two_sum(tuple1,target)

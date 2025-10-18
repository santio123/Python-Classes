# number game
import random

comp = random.randint(1,10)

while True:
    user = int(input("enter a number(1-9) : "))
    if comp == user:
        print("congratulations!! u got it")
        break
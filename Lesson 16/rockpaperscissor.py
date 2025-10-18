# rock paper scissor
import random
list1 = ['rock','paper','scissors']

while True:
    comp = random.choice(list1)
    user = input("enter rock or paper or scissors : ").lower()
    if user == comp:
        print("it is a tie!!")
    elif (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp =='rock') or (user == 'scissors' and comp == 'paper') :
        print("you win!!")
    else:
        print("computer wins")

    ch = input("do you want to play again y/n : ")
    if ch.lower() == 'n':
        break
        
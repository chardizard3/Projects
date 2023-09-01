#RPS vs AI using a randint

import random

RPS = ["rock", "paper", "scissors"]
 
compchoice = random.randint(0, 2)

print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(Enter your choice): ")
comp = RPS[compchoice]

print("The Computer plays: ", comp)

if p1 == "rock" : 
    if comp == "paper":
        print("The Computer Wins!")
    
    elif comp == "scissors":
        print("Player 1 Wins!")

    else:
        print("Draw")

elif p1 == "paper" : 
    if comp == "rock":
        print("Player 1 Wins!")
    
    elif comp == "scissors":
        print("The Computer Wins!")

    else:
        print("Draw")

elif p1 == "scissors" : 
    if comp == "paper":
        print("Player 1 Wins!")
    
    elif comp == "rock":
        print("The Computer Wins!")

    else:
        print("Draw")

else :
    print("Error")
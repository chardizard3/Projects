#RPS vs AI using a randint
#best of 5

import random

RPS = ["rock", "paper", "scissors"]
player_wins = 0
comp_wins = 0


while player_wins != 3 and comp_wins != 3 :

    compchoice = random.randint(0, 2)
    comp = RPS[compchoice]

    print(f"Score: Player - {player_wins} : {comp_wins} - Computer")

    print("...rock...")
    print("...paper...")
    print("...scissors...")

    p1 = input("(Enter your choice): ")
    print("The Computer plays: ", comp)

    if p1 == "rock" : 
        if comp == "paper":
            print("The Computer Wins!")
            comp_wins += 1
        
        elif comp == "scissors":
            print("Player 1 Wins!")
            player_wins += 1

        else:
            print("Draw")

    elif p1 == "paper" : 
        if comp == "rock":
            print("Player 1 Wins!")
            player_wins += 1
        
        elif comp == "scissors":
            print("The Computer Wins!")
            comp_wins += 1

        else:
            print("Draw")

    elif p1 == "scissors" : 
        if comp == "paper":
            print("Player 1 Wins!")
            player_wins += 1
        
        elif comp == "rock":
            print("The Computer Wins!")
            comp_wins += 1

        else:
            print("Draw")

    else :
        print("Error")

if player_wins == 3:
    print(f"Score: Player - {player_wins} : {comp_wins} - Computer")
    print("Congrats! You are the winner")

elif comp_wins == 3:
    print(f"Score: Player - {player_wins} : {comp_wins} - Computer")
    print("Aw, the computer wins :(")

else:
    print ("Error")
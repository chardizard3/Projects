# Just like basic but nested
# P1 choice -> 3 choices of P2

print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(enter Player 1's choice): ")
p2 = input("(enter Player 2's choice): ")
print("SHOOT!")

if p1 == "rock" : 
    if p2 == "paper":
        print("Player 2 Wins!")
    
    elif p2 == "scissors":
        print("Player 1 Wins!")

    else:
        print("Draw")

elif p1 == "paper" : 
    if p2 == "rock":
        print("Player 1 Wins!")
    
    elif p2 == "scissors":
        print("Player 2 Wins!")

    else:
        print("Draw")

elif p1 == "scissors" : 
    if p2 == "paper":
        print("Player 1 Wins!")
    
    elif p2 == "rock":
        print("Player 2 Wins!")

    else:
        print("Draw")

else :
    print("Error")
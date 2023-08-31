"""choices ={"rock" : 1,
          "paper" : 2,
          "scissors" : 3}"""

print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(enter Player 1's choice): ")
p2 = input("(enter Player 2's choice): ")
print("SHOOT!")

if p1 == "rock" and p2 == "paper":
    print("Player 2 Wins!")

elif p1 == "rock" and p2 == "scissors":
    print("Player 1 Wins!")

elif p1 == "paper" and p2 == "rock":
    print("Player 1 Wins!")

elif p1 == "paper" and p2 == "scissors":
    print("Player 2 Wins!")

elif p1 == "scissors" and p2 == "rock":
    print("Player 2 Wins!")

elif p1 == "scissors" and p2 == "paper":
    print("Player 1 Wins!")

else:
    print("Draw!")
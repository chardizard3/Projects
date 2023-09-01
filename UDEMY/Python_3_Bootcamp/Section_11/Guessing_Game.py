from random import randint

num = randint(1,10)
guess = 0

while guess != num :
    print (num)
    guess = input ("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess > num :
        print ("Too high, try again!")
        
    elif guess < num :
        print ("Too low, try again!")
       
    else :
        print ("You guessed it! You won!")
        again = input("Do you want to keep playing? (y/n) ")
        if again == "y" :
            num = randint(1,10)
            #guess = input ("Guess a number between 1 and 10: ")

if guess == num:
    print ("You guessed it! You won!")
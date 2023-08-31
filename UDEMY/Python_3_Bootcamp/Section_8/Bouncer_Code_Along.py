#ask for age
#18-21 wristband
#21+ drink, normal entry
#<18 too young, sorry

age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21 :
        print ("You can drink, welcome")

    elif age < 21 and age >= 18 :
        print ("Here's your wristband")

    else :
        print ("You are too young, sorry")

else:
    print("Please enter your age")

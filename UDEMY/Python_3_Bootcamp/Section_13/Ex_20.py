#1
#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, 
#which is a new list containing the first letter of each name in the list.  
#I would use a list comprehension, though you could also loop over manually.

list = ["Elie","Tim","Matt"]
answer=[answer[0] for answer in list]
print(answer)
#2
#Given a list [1,2,3,4,5,6], create a new variable called answer2, 
#which is a new list of all the even values. 
#Another good candidate for a list comp.

list2 = [1,2,3,4,5,6]
answer2=[answer2 for answer2 in list2 if answer2 % 2 ==0]
print(answer2)


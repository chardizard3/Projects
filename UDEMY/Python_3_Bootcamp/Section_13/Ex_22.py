#For all the numbers between 1 and 100(including 100), create a variable called answer, 
#which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)

answer = [answer for answer in range(1,101) if answer%12 is 0]
print(answer)
#Given the string "amazing", create a variable called answer, 
#which is a list containing all the letters from "amazing" 
#but not the vowels (a, e, i, o, and u).  The answer should look like: ['m', 'z', 'n', 'g'].

answer = [answer for answer in "amazing" if answer not in ["a", "e", "i", "o", "u"]]

print(answer)
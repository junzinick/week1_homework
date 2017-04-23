"""
https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that takes two user inputted numbers and prints "The first number is larger" or 
"The second number is larger" depending on which is larger. (Hint: you'll need to use raw_input() twice.)
"""
user_1 = int(input("Pick a Number - User One "))
user_2 = int(input("Pick a number - User Two "))
if user_1 > user_2:
    print("User One's number ", user_1 , "> User Two's", user_2 ,"!".format(user_1, user_2))
elif user_2 > user_1:
    print("User Two's number ", user_2 , "> User One's", user_1 ,"!".format(user_2, user_1))

else:
    print('User1 and User2 is equal')
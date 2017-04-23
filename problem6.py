"""
https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that computes and prints all of the divisors of a user inputted number. If you don't know what a divisor is or need a review, check out this link. Things to think about:

How do you determine if a single number is a divisor of another?
How do you do this multiple times (Hint: it involves a while loop)?
When do you stop the loop
"""
user_1 = int(input("Pick a Number - User One "))
user_2 = int(input("Pick a number - User Two "))
if user_1 % user_2 == 0:
    print("User One's number ", user_1 , " is divisibile User Two's", user_2 ,"!".format(user_1, user_2))
elif user_2 % user_1 != 0:
    print("User Two's number ", user_2 , "is not divisibile User One's", user_1 ,"!".format(user_2, user_1))

else:
    print('User1 and User2 is equal ')
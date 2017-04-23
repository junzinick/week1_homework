"""
Write a script that computes the greatest common divisor between two user inputted numbers. If you don't know what a greatest common divisor is, 
check out this link. Things to think about:

How do you get two numbers from the user?
Where should you start your search for the GCD?
Where/how should you end your search?
"""

user_1 = int(input("Pick a number to find common divisor: "))
user_2 = int(input("Pick a second number as the divisor: "))

floor_output = user_1 // user_2
if user_1 // user_2:
    print("This is a", floor_output , "even number")
elif user_1 % user_2 !=0:
    print("This is an odd number")





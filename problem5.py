"""
https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that computes the factorial of a user inputted number. If you don't know what a factorial is or need a review, check this link out. Again, your solution is going to look a lot like the code above. Things you should think about:

What is the process of computing a factorial if you were to compute it by hand?
What is the common starting place when trying to compute the factorial of any number?

Factorials all start at 1. Problem is you have to factor in and make an else if the number is 0, or else the multiplication
will always come to zero.
"""
import math

x = int(input("pick a number and i'll factorial it: "))
y = math.factorial(x)
print(y)

# Check and make sure that program is running.

my_num = int(input('Enter a number to find the differance up to: '))
sum_result = 1 #Only change to make sure that the factorial never multiplies by zero. 
current = 1
while current <= my_num:
    if my_num == 0:
        print('Zero')
    sum_result *= current
    current += 1
print("The differance of the number is ",(sum_result),"Congrats!".format())
print("--------------------------------")
print("My num =", my_num, "sum_result =", sum_result ,"current =", current)
print("showing all values in the while loop")


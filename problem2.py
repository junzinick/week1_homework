"""
https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that takes a user inputted number and prints whether it is positive, negative or zero, with 
"The inputted number is (positive/negative/zero)" depending.
"""
x = int(input("pick a number:"))
if x > 0:
    print(x,"is positive".format())
elif x < 0:
    print(x,'is negative'.format())
else:
    print('ZERO')
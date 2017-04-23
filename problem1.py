"""https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that prints the sum of the whole numbers between 1 and a user inputted number.
"""
my_num = int(input('Enter a number to find the sum up to: '))
sum_result = 0
current = 1
while current <= my_num:
    sum_result += current
    current += 1
print("The sum of the number is ",(sum_result),"Congrats!".format())
"""
https://github.com/zipfian/python-fundamentals/blob/master/week1/day2-intro_python/intro_python_assignment.md
Write a script that computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down. 
This answer will look very much like the example above, you'll just need to change a couple of things.
"""
my_num = int(input('Enter a number to find the differance up to: '))
sum_result = 0
current = 1
while current <= my_num:
    sum_result -= current
    current += 1
print("The differance of the number is ",(sum_result),"Congrats!".format())
print("--------------------------------")
print("My num =", my_num, "sum_result =", sum_result ,"current =", current)
print("showing all values in the while loop")
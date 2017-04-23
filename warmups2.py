"""
Multiplication can be thought of as repeated additions. Write a script that takes as input two positive integers, a and b, and returns a * b. Do this without using the * operator.
Integer division can be done with repeated substraction, similar to how multiplication can be done with addition. Write a script that takes as input two positive integers, a and b, and returns a / b. Do this without using the / operator.
Exponentiation is repeated multiplication. Write a script that takes as input two positive integers, a and b, and returns a ** b. Do this without using the ** operator.
For two integers, a and b, a divides b if a / b has no remainder. Write a script that takes as input two positive integers, a and b, and says whether a divides b.
while loops and conditionals give you a lot of power. Try and create a game where a user is repeteadly asked to guess a number. If they get it wrong, they are asked to guess again, and if they are correct, 
they are told and the game ends. For extra credit, have the game tell the user whether their guess was high or low.

"""
a = int(input("Number a: "))
b = int(input("Number b: "))



for i in range(b):
    i += a
    print(a)
    total2 = a * (i+b)
    print(i)

print("The total with no division is", total2)

print(i)



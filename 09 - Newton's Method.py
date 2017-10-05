#Exercise 9, Newton's method for square root
# Adapted from https://stackoverflow.com/questions/18838265/python-square-root-function
# https://stackoverflow.com/questions/12850100/finding-the-square-root-using-newtons-method-errors
# https://stackoverflow.com/questions/19557498/making-an-input-value-into-a-decimal-python-3
# https://stackoverflow.com/questions/18838265/python-square-root-function

from math import *

x = float(input("Enter the value you want the square root of: "))
z = float(input("Enter your guess for the answer: "))

#Setting the formula
answer = z - ((z*z - x) / (2*z))
difference = 1

print("Your guess: %.2f" %z)

while difference > 0.00000000001:
    z = answer
    answer = z - ((z*z - x) / (2*z))
    difference = z - answer

print("Newton Sqr Root: %.2f" % answer)
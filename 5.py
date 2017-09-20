#Exercise 5, Guessing Game
#Adapted from https://www.tutorialspoint.com/python/python_while_loop.htm
#and https://wiki.python.org/moin/WhileLoop
#random number adapted from https://pythonspot.com/en/random-numbers/

from random import *
number = randint(1,10)
count = 1

guess = int(input("Guess the number? "))

while(guess != number):
    
    if guess < number:
        print("Your guess is too low.")
        count += 1
    elif guess > number:
        print("Your guess is too high.")
        count += 1
    guess = int(input("Guess the number? "))

print("Correct! It took ", count, " guesses." )

#Rough work
'''if guess == number:
    print("Correct!!")
elif guess < number:
    print("Your guess is too low.")
elif guess > number:
    print("Your guess is too high.")
else:
    print("Bad guess")'''

#Exercise 5, Guessing Game
#Adapted from https://www.tutorialspoint.com/python/python_while_loop.htm
#and https://wiki.python.org/moin/WhileLoop
#random number adapted from https://pythonspot.com/en/random-numbers/
#number not in range adapted from https://stackoverflow.com/questions/11594605/python-excepting-input-only-if-in-range

from random import *
number = randint(1,11)
count = 1

#guess = int(input("Guess a number between 1 & 10: "))

while True:
    try:
        guess = int(input("Guess a number between 1 & 10: "))
    except ValueError:
        print("Invalid input.")
    else:
        if 1<= guess < 11:
            while(guess != number):
                
                if guess < number:
                    print("Your guess is too low.")
                    count += 1
                elif guess > number:
                    print("Your guess is too high.")
                    count += 1
                guess = int(input("Guess the number? "))
            
            print("Correct! It took ", count, " guesses." )
            break
        else:
            print("Number is out of range!\nTake another guess:")

#Rough work
'''if guess == number:
    print("Correct!!")
elif guess < number:
    print("Your guess is too low.")
elif guess > number:
    print("Your guess is too high.")
else:
    print("Bad guess")'''

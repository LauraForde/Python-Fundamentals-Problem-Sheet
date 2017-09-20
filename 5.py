#Exercise 5, Guessing Game

number = 5

guess = int(input("Guess the number? "))

if guess == number:
    print("Correct!!")
elif guess < number:
    print("Your guess is too low.")
elif guess > number:
    print("Your guess is too high")
else:
    print("Bad guess")


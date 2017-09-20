#Exercise 4, Factorial Digit Sum

#Getting input from console
number = int(input("What number do you want the factorial of? "))
factorial = 1

#Saying factorial does not exist for negative numbers
if number < 0:
    print("Doesn't exist for negative numbers")
#If number & factorial are equal the answer is 1
elif number == 0:
    print("Factorial = 1")
# Else loop through and multiply
else:
    for i in range(1,number + 1):
        factorial = factorial*i
    print("Factorial is: ", factorial)     
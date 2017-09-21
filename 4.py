#Exercise 4, Factorial Digit Sum
#Getting the digit sum of 100! adapted from https://discuss.codechef.com/questions/56854/computing-sum-of-digits-of-large-factorial

#Getting input from console
from math import factorial
number = int(input("What number do you want the factorial of? "))
fact = 1
digitSum = 0

#Saying factorial does not exist for negative numbers
if number < 0:
    print("Doesn't exist for negative numbers")
#If number & factorial are equal the answer is 1
elif number == 0:
    print("Factorial = 1")
# Else loop through and multiply
else:
    for i in range(1,number + 1):
        fact = fact*i
    print("Factorial is: ", fact)  

#Getting the sum of all the digits in 100!
fac = factorial(100)
fac =str(fac)

for i in fac:
    digitSum+=int(i)
print("The sum of the digits in 100! is:",digitSum)
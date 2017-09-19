#Exercise 3, FizzBuzz
#Print numbers from 1 - 100, multiples of 3 print Fizz
#multipes of 5 print Buzz, multiples pf 3 & 5 print FizzBuzz

count = 1

#for loop with conditions to print Fizz Buzz
for i in range(1,101):
    if(count % 3) == 0:
        print("Fizz")
        count = count + 1
    elif(count % 5) == 0:
        print("Buzz")
        count = count + 1
    elif(count % 5) == 0 and (count % 3) == 0:
        print("FizzBuzz")
        count = count + 1
    else:
        print(count)
        count = count + 1
        
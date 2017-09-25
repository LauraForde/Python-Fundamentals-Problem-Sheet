#Exercise 7, testing if a string is a Palindrome
#Reversing the string adapted from https://stackoverflow.com/questions/931092/reverse-a-string-in-python
#Taking input from the console and making it all lower case for comparsion
etrString = input("Enter a word to test: ").lower()
#Reversing the string that was entered
reverse = etrString[::-1]

#If the reverse is = to the input, then the string is Palindrome
if reverse == etrString:
    print(etrString, "is a Palindrome!")
#Otherwise the string is not a Palindrome
else:
    print(etrString, "is not Palindrome.")

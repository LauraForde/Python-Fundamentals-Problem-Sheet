#Exercise 10, write a function to reverse a string
word = input("Enter a word to reverse: ")

def reverse(word):
    
    for i in range(len(word)):
       revWord = word[::-1]    
    return revWord
print("Entered word:", word, "\nWord in reverse:",reverse(word))
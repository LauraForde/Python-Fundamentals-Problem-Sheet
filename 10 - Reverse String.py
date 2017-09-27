#Exercise 10, write a function to reverse a string

word = []
word = input("Enter a word to reverse: ").lower()
newWord = []

def reverse(word):
    
    for letter in word:
        newWord.insert(0, letter)
print( ''.join(newWord))
    
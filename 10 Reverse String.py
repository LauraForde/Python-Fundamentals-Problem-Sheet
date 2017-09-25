#Exercise 10, write a function to reverse a string


word = input("Enter a word to test: ").lower()
newWord = ""
def reverseString(word):
    newWord = word[::-1]
print(word, newWord)

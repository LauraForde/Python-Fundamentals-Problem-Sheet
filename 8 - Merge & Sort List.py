#Exercise 8, merging and sorting two lists
#Adapted for merge and sort https://stackoverflow.com/questions/6543590/combining-two-lists-into-a-new-list-and-sorting?rq=1
list1 = [] 
list2 = [] 
mergeSort = []

manyNum = int(input("How many numbers will you enter for List 1? "))

for i in range(manyNum):
    numEntered = int(input("Enter Number: "))
    list1.append(numEntered)

manyNum2 = int(input("How many numbers will you enter for List 2? "))

for i in range(manyNum2):
    numEntered = int(input("Enter Number: "))
    list2.append(numEntered)  

list1.extend(list2)
mergeSort = sorted(list1)
print(mergeSort)

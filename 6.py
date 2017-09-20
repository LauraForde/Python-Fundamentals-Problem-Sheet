#Exercise 6, Print smallest and largest element in list
#Reading into list adapted from https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
#Adapted from https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08

getList = [] 
manyNum = int(input("How many numbers will you enter? "))

for i in range(manyNum):
    numEntered = int(input("Enter Number: "))
    getList.append(numEntered)

print("The max number is:", max(getList), "\nThe min number is:",min(getList))
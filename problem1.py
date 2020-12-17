# Euler Project problem 1, Multiple of 3 and 5
# https://projecteuler.net/problem=1
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
listOfNum = []

# Create a list of 3s and 5s
for number in range(0, 1000):
    if number % 3 == 0:
        threes = number
        listOfNum.append(threes)
    if number % 5 == 0:
        fives = number
        listOfNum.append(fives)

# remove the duplicate element from the list
finalList = []
for number in listOfNum:
    if number not in finalList:
        finalList.append(number)

count = sum(finalList)
print(count)

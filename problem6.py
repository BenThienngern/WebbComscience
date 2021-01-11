# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# https://projecteuler.net/problem=6

# create a list of number from 900 to 1000
start = 1
numlist = []
for i in range(0, 100):
    numlist.append(start)
    start += 1


squareList = []
for i in numlist:
    square = i*i
    squareList.append(square)

sumOfNumSq = sum(numlist) * sum(numlist)
answer = sumOfNumSq - sum(squareList)
print(answer)
# 25164150

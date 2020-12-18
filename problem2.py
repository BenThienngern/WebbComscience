# Euler Project problem 2, Fibonacci sequence
# https://projecteuler.net/problem=1
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
 find the sum of the even-valued terms.
'''
first = 1
second = 2
numList = [1, 2]
# Create a list of Fibonacci number
while first and second < 4000000:
    first = first + second
    numList.append(first)
    second = first + second
    numList.append(second)

newList = []
# remove odd number
for num in numList:
    if num % 2 == 0:
        newList.append(num)

result = sum(newList)
print('result', result)

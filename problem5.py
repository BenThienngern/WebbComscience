# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# https://projecteuler.net/problem=5

repeat = False
num = 5000
while repeat == False:
    count = 0
    for i in range(1, 20):
        if num % i == 0:
            count += 1
        else:
            break
    if count == 20:
        repeat = True
        print(num)
        break
    num = num + 20

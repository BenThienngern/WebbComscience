# Problem 5 After research 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# https://projecteuler.net/problem=5

# After some research I found out that there's a built in function from numpy which can help solve the problem of too much operation 
# Cite: https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple
# https://www.w3schools.com/python/numpy_ufunc_lcm.asp

import numpy as np

listOfNum = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                      12, 13, 14, 15, 16, 17, 18, 19, 20])
result = np.lcm.reduce(listOfNum)

print(result)
# 232792560

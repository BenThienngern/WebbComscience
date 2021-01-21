# Euler Project problem 9,
# https://projecteuler.net/problem=9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import math
# Check for pythagorean triplet first
aa = 0
bb = 0
pythagList = []
for i in range(0, 500):
    aa = aa + 1
    for a in range(0, 500):
        bb = bb + 1
        # c = square root of a^2 + b^2
        cc = math.sqrt(aa ** 2 + bb ** 2)
        # Check for whole number
        if cc == int(cc):
            pythagList.append([aa, bb, cc])
        if bb == 500:
            bb = 0

# Find the combination which the sum is 1000
for element in pythagList:
    if sum(element) == 1000:
        answer = element
        print(element)

# Times abc to get the final answer
finalAnswer = answer[0]*answer[1]*answer[2]
print(int(finalAnswer))

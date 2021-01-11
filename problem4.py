# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# https://projecteuler.net/problem=4

# create a list of number from 900 to 1000
start = 900
numlist = []
for i in range(0, 100):
    numlist.append(start)
    start += 1

# Helper function to check for palindrome


def check(num):
    first = int(str(num)[-3:])
    second = int(str(num)[2]+str(num)[1]+str(num)[0])
    if first == second:
        return num
    else:
        return ''


# We know that the first and last index of this number is the same
# And the last number is either 8 or 9
newlist9 = []
newlist8 = []
newlist3 = []
newlist1 = []
a = 0
for i in numlist:
    if numlist[a] % 10 == 8:
        newlist8.append(i)
    elif numlist[a] % 10 == 9:
        newlist9.append(i)
    elif numlist[a] % 10 == 3:
        newlist3.append(i)
    elif numlist[a] % 10 == 1:
        newlist1.append(i)
    a += 1

# Try with all the different combination of list
for i in newlist3:
    for o in newlist3:
        num = i*o
        print(check(num))
for i in newlist9:
    for o in newlist1:
        num = i*o
        print(check(num))
for i in newlist8:
    for o in newlist1:
        num = i*o
        print(check(num))
# 906609

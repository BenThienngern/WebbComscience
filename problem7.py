# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Adapt the code from problem 3
def findPrime(start, end):
    start = start + 3
    theCount = 0
    prime = [2]
    for num in range(start, end):
        # Can only do up to 10000 at a time because of the run time limit
        check = True
        for factor in prime:
            if (num % factor) == 0:
                check = False

        if check == True:
            prime.append(num)
    return prime


# start = 0
# count = 0
# end = 2500
# count = []
# # Do this to reduce the number of operation that have to be run
# for i in range(0, 40):
#     count.append(findPrime(start, end))
#     start = start + 2500
#     end = end + 2500

# print(sum(count))
ans = findPrime(0, 108000)
print(ans[10000])
# # between 0 and 100000 there's 9594 prime number
# prime = []
# for num in range(100000, 107000):
#     # Can only do up to 10000 because of the run time limit
#     check = True
#     for factor in range(2, num):
#         if (num % factor) == 0:
#             check = False

#     if check == True:
#         prime.append(num)
# print(prime[406])

# 104743

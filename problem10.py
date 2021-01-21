# Euler Project problem 10,
# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.

# This is the find prime function I create in problem 7
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


# This is too much for my CPU !!!!!
print(sum(findPrime(0, 2000000)))

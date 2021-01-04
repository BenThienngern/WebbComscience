# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
# https://projecteuler.net/problem=3

prime = []
for num in range(0, 10000):
    # Can only do up to 10000 because of the run time limit
    check = True
    for factor in range(2, num):
        if (num % factor) == 0:
            check = False

    if check == True:
        prime.append(num)
prime = list(dict.fromkeys(prime))
# remove 0
prime = prime[1:]

# Check if a prime number is a factor of that number
primeFactor = []
for i in prime:
    if 600851475143 % i == 0:
        primeFactor.append(i)

print(max(primeFactor))

import math


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


file = open("liczby.txt", "r").read().split("\n")
file.pop()

primes = 0
for line in file:
    M = int(line.split()[0])
    if prime(M) == 1:
        primes +=1

print(primes)
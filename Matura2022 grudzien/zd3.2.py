import math

file = open("liczby.txt", "r").read().split("\n")
file.pop()
file = [int(x) for x in file]


def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0

    return 1

count = 0
for num in file:
    if prime(num-1):
        count +=1

print(count)
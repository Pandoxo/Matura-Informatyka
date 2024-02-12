import math

file = open("liczby.txt", "r").read().split("\n")
file.pop()
nums = [int(i) for i in file]


def check_prime(n) -> int:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for num in nums:
    if num > 99 and num <5001:
        if check_prime(num):
            print(num)


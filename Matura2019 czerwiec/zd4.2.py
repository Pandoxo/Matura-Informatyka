import math

file = open("pierwsze.txt", "r").read().split("\n")
file.pop()
def check_prime(n) -> int:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for num in file:

    if check_prime(int(num[::-1])):
        print(num)


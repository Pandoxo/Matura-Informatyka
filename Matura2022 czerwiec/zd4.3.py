import math

file = open("liczby.txt", "r").read().split("\n")
wyniki = open("wyniki4.txt", "a")


def reverse(txt):
    result = ""
    for i in range(len(txt) - 1, -1, -1):
        result += txt[i]
    return result


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for num in file:
    if isPrime(int(num)) and isPrime(int(reverse(num))):
        wyniki.write(f"{num}\n")

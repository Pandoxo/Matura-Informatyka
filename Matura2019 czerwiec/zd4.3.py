file = open("pierwsze.txt", "r").read().split("\n")
file.pop()


def sumDigits(n) -> int:
    result = 0
    for digit in n:
        result += int(digit)
    return result


def weight(n) -> int:
    while True:
        result = sumDigits(n)
        n = str(result)
        if result < 10:
            break
    return result


count = 0
for num in file:
    if weight(num) == 1:
        count += 1

print(count)

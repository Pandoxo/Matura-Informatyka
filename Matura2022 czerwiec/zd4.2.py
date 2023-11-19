import math

file = open("liczby.txt", "r").read().split("\n")
wyniki = open("wyniki4.txt", "a")


def reverse(txt):
    result = ""
    for i in range(len(txt) - 1, -1, -1):
        result += txt[i]
    return result


maxDiff = 0
maxNum = file[0]
for num in file:
    absDiff = abs(int(num) - int(reverse(num)))
    if absDiff > maxDiff:
        maxDiff = absDiff
        maxNum = num
wyniki.write(f"{maxNum} {maxDiff}")

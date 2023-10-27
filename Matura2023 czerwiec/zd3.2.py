import math

file = open("anagram.txt", "r").read().split("\n")
wyniki = open("wyniki3.txt", "a")

def anagrams(txt):
    zeros = 0
    for bit in txt:
        if bit == "0":
            zeros += 1

    return math.comb(len(txt)-1, zeros)

maxCount = 0
for num in file:
    if len(num) == 8:
        count = anagrams(num)
        if count > maxCount:
            maxCount = count


for num in file:
    if len(num) == 8:
        count2 = anagrams(num)
        if count2 == maxCount:
            wyniki.write(f'{num}\n')


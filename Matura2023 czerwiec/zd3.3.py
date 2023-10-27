file = open("anagram.txt", "r").read().split("\n")
wyniki = open("wyniki3.txt", "a")

def binToInt(txt):
    result = 0
    for i in range(len(txt)):
        result += int(txt[len(txt)-1-i]) * pow(2,i)
    return result


def intToBin(num):
    result = ""
    while num>0:
        result += str(num % 2)
        num //= 2
    return result[::-1]


maxDiff = 0
for i in range(len(file)-1):
    diff = abs(binToInt(file[i]) - binToInt(file[i+1]))
    if diff > maxDiff:
        maxDiff = diff

wyniki.write(intToBin(maxDiff))

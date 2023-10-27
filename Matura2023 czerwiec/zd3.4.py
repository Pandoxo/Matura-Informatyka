file = open("przyklad.txt", "r").read().split("\n")
wyniki = open("wyniki3.txt", "a")


def sum(n):
    ls = []
    result = 0
    for num in n:
        if not num in ls:
            result += int(num)
    return result

def binToInt(txt):
    result = 0
    for i in range(len(txt)):
        result += int(txt[len(txt)-1-i]) * pow(2,i)
    return result

nums = []

for num in file:
    nums.append(str(binToInt(num)))

withoutZeros = 0
maxSum = 0
maxLs = []
for num in nums:
    if not "0" in num:
        withoutZeros += 1
    numSum = sum(num)
    if numSum > maxSum:
        maxSum = numSum
        maxLs.append(num)

for num in maxLs:
    if sum(num) == maxSum:
        print(num)
        break



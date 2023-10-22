
file = open("przyklad.txt", "r")
def rozklad(num):

    czynniki = []
    lenght = num//2
    for i in range(2, lenght):
        if (num % i == 0):
            czynniki.append(i)
    return czynniki

maxCount = 0
maxCountNum = 0

maxDifCount = 0
maxDifCountNum = 0
for num in file:
    num = num[:-1]
    factors = rozklad(int(num))
    if maxCount< len(factors):
        maxCount = len(factors)
        maxCountNum = num
    factors.sort()
    difCount = 1
    for i in range(0,len(factors)-1):
        if(factors[i] != factors[i+1]):
            difCount += 1
    if(difCount > maxDifCount):
        maxDifCount = difCount
        maxDifCountNum = num

print("MaxDifCount: " + str(maxCount))
print("MaxCount: " + str(maxCount))

print(maxCountNum)
print(maxDifCountNum)




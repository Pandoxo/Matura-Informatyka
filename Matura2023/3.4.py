pi = open("pi.txt", "r")
piList = []
i = 0
for num in pi:
    piList.append(num)


maxL =0
maxI = 0
count = 1
lenght = len(piList)
for j in range(0,lenght):
    i =j
    count = 1
    while (i + 1 < lenght and piList[i] <= piList[i + 1]):
        count += 1
        i += 1
    i += 1
    while (i+1 < lenght and piList[i] >= piList[i + 1]):
        count += 1
        i += 1
    i+=2
    count+=1
    if count > maxL:
        maxL = count
        maxI = i - count

#Wiersze są indeksowane od 1 a listy od 0 stad moj problem
result = []
for i in range(maxI, maxI+maxL):
    result.append(int(piList[i]))
print(result)
print("max lenght: " + str(maxL)+ "\n" + "index: " + str(maxI))



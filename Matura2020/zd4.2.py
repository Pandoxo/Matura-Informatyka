file = open("przyklad.txt", "r")
wyniki = open("wyniki4.txt", "a")

for txt in file:
    count = 1
    maxCount = 1
    maxIndex = 0
    txt = txt.split()[1]
    for i in range(0,len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count
            maxIndex = i+1
    maxIndex+=1
    wyniki.write(f'{txt[maxIndex-maxCount:maxIndex]} {maxCount}\n')
    #print(f'maxCount = {maxCount} maxIndex = {maxIndex}\n')


print(max)
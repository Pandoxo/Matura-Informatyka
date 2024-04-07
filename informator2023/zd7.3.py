czestosc = open("czestosc.txt", "r").read().split("\n")
szyfry = open("szyfrogram.txt", "r").read().split("\n")

czestosc.pop()
szyfry.pop()

tab_polski = [0] * 91
tab = [0] * 91

for line in czestosc:
    tab_polski[ord(line.split()[0])] = int(line.split()[1])



for line in szyfry:
    for letter in line:
        tab[ord(letter)] +=1


odszyfrowany = ""
for line in szyfry:
    result = ""
    for letter in line:
        ilosc = tab[ord(letter)]
        for i in range(65,91):
            if tab_polski[i] == ilosc:
                result += chr(i)
                break
    odszyfrowany += result

print(odszyfrowany)





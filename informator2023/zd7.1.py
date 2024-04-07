file = open("szyfrogram.txt", "r").read().split("\n")

tab = [0] * 91

#65 90

for line in file:
    for letter in line:
        tab[ord(letter)] +=1


for i in range(65,91):
    print(chr(i),tab[i])
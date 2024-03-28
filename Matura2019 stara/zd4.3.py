file = open("dzialki.txt" , "r").read().splitlines()
dzialki = []


i = 0
dzialka = []
while i < len(file):
    linia = file[i]
    if linia:
        dzialka.append(linia)
    else:

        dzialki.append(dzialka)
        dzialka = []
    i += 1


maxWielkosc = 0
for dzialka in dzialki:
    wielkosc = 30
    najWieksza = 0
    for i in range(wielkosc):

        for j in range(wielkosc):
            if dzialka[i][j] == "X":
                wielkosc = j
                break
        if j - 1 == wielkosc and i - 1 == wielkosc:
            print(wielkosc)
            break

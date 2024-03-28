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


ilosc_dzialek70 = 0
for dzialka in dzialki:
    ilosc_trawy = 0
    for linia in dzialka:
        for znak in linia:
            if znak == "*":
                ilosc_trawy += 1
    if ilosc_trawy/900*100 >=70:
        ilosc_dzialek70 += 1

print(ilosc_dzialek70)

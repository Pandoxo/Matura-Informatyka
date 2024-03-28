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


for i in range(49):
    odwrocona = dzialki[i][::-1]
    for j in range(30):
        odwrocona[j] = odwrocona[j][::-1]
    for k in range(49):
        if dzialki[k] == odwrocona:
            print(k+1,i+1)
            break



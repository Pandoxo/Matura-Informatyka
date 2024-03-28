file = open("szachy.txt", "r").read().split("\n")
file.pop()

szachy = []

i = 0
plasza = []
while i < len(file):
    if file[i]:
        plasza.append(file[i])
    else:
        szachy.append(plasza)
        plasza = []
    i += 1

print(szachy)


def iloscPustych(plansza):
    puste = 8
    for i in range(8):
        for j in range(8):
            if plansza[j][i] != ".":
                puste -= 1
                break
    return puste


maxPustych = 0
conajmniej_jedna = 0
for plansza in szachy:
    wynik = iloscPustych(plansza)
    if wynik > 0:
        conajmniej_jedna += 1
        if wynik > maxPustych:
            maxPustych = wynik

print(maxPustych)
print(conajmniej_jedna)

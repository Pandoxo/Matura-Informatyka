# 97 - 122
# 65 - 90
file = open("szachy.txt", "r").read().split("\n")
file.pop()

szachy = []

i = 0
plansza = []
while i < len(file):

    if file[i]:
        plansza.append(file[i])
    else:
        szachy.append(plansza)
        plansza = []
    i += 1

stanRownowagi = 0
minBierekWrownowadze = 32
for plansza in szachy:
    biale = [0 for _ in range(6)]  # [0,0,0,0,0,0]
    czarne = [0 for _ in range(6)]
    # 0-pion 1-skoczek 2-goniec 3-wieza 4- hetman 5-krol
    for i in range(8):
        for j in range(8):
            figura = (plansza[i][j])
            # czarne
            if 96 < ord(figura) < 123:
                if figura == "p":
                    biale[0] += 1
                elif figura == "s":
                    biale[1] += 1
                elif figura == "g":
                    biale[2] += 1
                elif figura == "w":
                    biale[3] += 1
                elif figura == "h":
                    biale[4] += 1
                elif figura == "k":
                    biale[5] += 1
            # biale
            if 64 < ord(figura) < 91:
                if figura == "P":
                    czarne[0] += 1
                if figura == "S":
                    czarne[1] += 1
                if figura == "G":
                    czarne[2] += 1
                if figura == "W":
                    czarne[3] += 1
                if figura == "H":
                    czarne[4] += 1
                if figura == "K":
                    czarne[5] += 1
    if czarne == biale:
        stanRownowagi += 1
        if sum(czarne) + sum(biale) < minBierekWrownowadze:
            minBierekWrownowadze = sum(czarne) + sum(biale)

print(stanRownowagi)
print(minBierekWrownowadze)

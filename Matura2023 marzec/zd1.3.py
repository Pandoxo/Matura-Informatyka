file = open("szachy.txt", "r").read().split("\n")

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

szachy.pop()


def sprawdzPoziomo(plansza, wieza, kolor):
    i = wieza[0]
    j = wieza[1]
    # -->
    j += 1
    while j < 8:
        if plansza[i][j] != ".":
            if plansza[i][j] == "k" or plansza[i][j] == "K":
                return 1
            else:
                return 0
        j += 1

    j = wieza[1]
    j -= 1
    # <--
    while j > -1:
        if plansza[i][j] != ".":
            if plansza[i][j] == "k" or plansza[i][j] == "K":
                return 1
            else:
                return 0
        j -= 1
    return 0


def sprawdzPionowo(plansza, wieza):
    i = wieza[0]
    j = wieza[1]
    # /\
    # |
    i -= 1
    while i > -1:
        if plansza[i][j] != ".":
            if plansza[i][j] == "k" or plansza[i][j] == "K":
                return 1
            else:
                return 0
        i += 1

    i = wieza[1]
    i = i + 1
    # |
    # \/
    while i < 8:
        if plansza[i][j] != ".":
            if plansza[i][j] == "k" or plansza[i][j] == "K":
                return 1
            else:
                return 0
        i += 1
    return 0


bialaSzachuje = 0
czarnaSzachuje = 0

for plansza in szachy:
    kordyWiezBialych = []
    kordyWiezCzarnych = []
    for i in range(8):
        for j in range(8):
            print(plansza)
            if plansza[i][j] == "W":
                kordyWiezBialych.append([i, j])
            if plansza[i][j] == "w":
                kordyWiezBialych.append([i, j])

    for wieza in kordyWiezCzarnych:
        if sprawdzPionowo(plansza, wieza):
            czarnaSzachuje += 1
            break
        if sprawdzPoziomo(plansza, wieza):
            czarnaSzachuje += 1
            break
    for Wieza in kordyWiezBialych:
        if sprawdzPionowo(plansza, Wieza):
            bialaSzachuje += 1
            break
        if sprawdzPoziomo(plansza, Wieza):
            bialaSzachuje += 1
            break

print(f"biala {bialaSzachuje}")
print(f"czarna {czarnaSzachuje}")

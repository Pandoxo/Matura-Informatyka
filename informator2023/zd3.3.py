file = open("dane3.txt", "r").read().split("\n")
file.pop()


max_dl = 0
dl = 1
for i in range(len(file)-1):

    poczatek = int(file[i].split()[0])
    koniec = int(file[i].split()[1])
    poczatek2 = int(file[i+1].split()[0])
    koniec2 = int(file[i+1].split()[1])
    if koniec >= poczatek2:
        dl += 1
    else:
        dl = 0
    if dl > max_dl:
        max_dl = dl

print(max_dl)

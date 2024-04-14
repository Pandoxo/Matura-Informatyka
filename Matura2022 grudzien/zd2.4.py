file = open("pary.txt", "r").read().split("\n")
file.pop()
pary = []

for line in file:
    pary.append([int(line.split()[0]), int(line.split()[1])])


N = 100000
strzalki = []
def rysuj(x):
    if 2*x <= N:
        strzalki.append([x,2*x])
        rysuj(2*x)
    if 2*x + 1 <= N:
        strzalki.append([x, 2 * x +1])
        rysuj(2*x+1)



for para in pary:
    strzalki = []
    rysuj(para[0])
    for strzalka in strzalki:
        if strzalka[1] == para[1]:
            print(para[0] , para[1])
            break




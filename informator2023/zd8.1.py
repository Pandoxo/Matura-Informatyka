file = open("dane8.txt", "r").read().split("\n")
file.pop()
parzyste = 0
nieparzyste = 0

liczby = [int(_) for _ in file]

for i in range(len(liczby) -1 ):
    luka = abs(liczby[i + 1] - liczby[i])
    if luka % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1


print(f"nieparzyste - {nieparzyste}")
print(f"parzyste -  {nieparzyste}")


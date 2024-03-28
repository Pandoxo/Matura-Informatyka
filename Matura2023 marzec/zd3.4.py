file = open("liczby.txt", "r").read().split("\n")
file.pop()


def NWD(a, b):
    if a % b == 0:
        return b
    else:
        return NWD(b, a % b)


wzgledniePierwsze = 0
for line in file:
    a = int(line.split()[1])
    M = int(line.split()[0])

    if NWD(a, M) == 1:
        wzgledniePierwsze += 1

print(wzgledniePierwsze)
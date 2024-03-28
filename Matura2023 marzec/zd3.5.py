file = open("liczby.txt", "r").read().split("\n")
file.pop()


def pot_mod(a, x, M):
    wynik = 1
    z = a
    while x > 0:
        if x % 2 == 1:
            wynik = (wynik * z) % M
        z = z * z % M
        x //= 2
    return wynik


count = 0
for line in file:
    M = int(line.split()[0])
    a = int(line.split()[1])
    b = int(line.split()[2])

    for i in range(M):
        if pot_mod(a, i, M) == b:
            count += 1
            break

print(count)

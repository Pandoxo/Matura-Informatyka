file = open("liczby.txt", "r").read().split("\n")
file.pop()
file = [int(x) for x in file]

tab = [0]*16
for num in file:
    while num > 0:
        x = num % 16
        tab[x] += 1
        num //= 16

for i in range(len(tab)):
    if i > 9:
        print(chr(65 + i-10) , tab[i])
    else:
        print(i,tab[i])





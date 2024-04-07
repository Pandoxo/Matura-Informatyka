file = open("dane8.txt", "r").read().split("\n")
file.pop()

liczby = [int(_) for _ in file]

lenght = len(liczby)
nieuporzadkowane = 0
for i in range(lenght):
    for j in range(i+1,lenght):
        if liczby[i] > liczby[j]:
            nieuporzadkowane += 1

print(nieuporzadkowane)

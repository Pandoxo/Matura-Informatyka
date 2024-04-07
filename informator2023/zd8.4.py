file = open("dane8.txt", "r").read().split("\n")
file.pop()

liczby = [int(_) for _ in file]

lenght = len(liczby)

LIS = [1] * 2023

for i in range(len(liczby) - 1, -1, -1):
    for j in range(i + 1, len(liczby)):
        if liczby[i] < liczby[j]:
            LIS[i] = max(LIS[i], 1 + LIS[j])

print(max(LIS))

file = open("dane1_4.txt" , "r").read().split("\n")
file.pop()
liczby = [int(_) for _ in file]


max_sum = 0
poczatek = 0
koniec = 0
for i in range(len(liczby)):
    sumy = [liczby[i]]
    for j in range(i+1,len(liczby)):
        sumy.append(sumy[-1] + liczby[j])
        if sumy[-1] < i:
            break
    najw = max(sumy)
    if najw > max_sum:
        max_sum = najw
        poczatek = i

cur_sum = 0
for i in range(poczatek,len(liczby)):
    cur_sum += liczby[i]
    if cur_sum == max_sum:
        break

print(max_sum)
print(f"poczatek - {poczatek + 1}")
print(f"koniec - {i + 1}")


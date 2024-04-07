file = open("dane1_3.txt" , "r").read().split("\n")
file.pop()
liczby = [int(_) for _ in file]


max_sum = 0
poczatek = 0
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


print(max_sum)
print(poczatek)
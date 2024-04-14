def znajdz_parzysta(tab):
    p = 1
    k = len(tab) - 1
    while k - p != 1:
        s = (k + p) // 2
        if tab[s] % 2 == 0:
            k = s
        else:
            p = s
    return tab[k]


print(znajdz_parzysta([5, 99, 7, 3, 7, 111, 13, 3, 3, 3, 3, 36, 24, 4, 8, 8, 10, 2, 2, 2]))

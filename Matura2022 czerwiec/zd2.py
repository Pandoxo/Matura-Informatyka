def koduj(n):
    if n == 1:
        return ""
    else:
        k = n // 2
        if k % 2 == 0:
            return koduj(k) + "A"
        else:
            return "B" + koduj(k)


print(koduj(65))
file = open("slowa3.txt", "r").read().split("\n")

print(file)
n_ = int(file[0])
s_ = file[1]
k1_ = file[2].split(" ")[0]
k2_ = file[2].split(" ")[1]


def czy_mniejszy(n, s, k1, k2):
    i = int(k1)
    j = int(k2)
    while i < n and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"

    if j < n:
        return "TAK"
    else:
        return "NIE"


print(czy_mniejszy(n_, s_, k1_, k2_))

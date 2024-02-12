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


s_ = "mascarpone"
n_ = 10

T = [0 for _ in range(10)]
for k in range(n_ -1):
    if czy_mniejszy(n_,s_,k,k+1):
        T[k] = k
        T[k+1] = k+1
    else:
        T[k+1] = k
        T[k] = k+1

print(T)


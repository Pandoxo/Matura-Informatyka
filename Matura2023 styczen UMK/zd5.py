an = [pow(-1, i) for i in range(121)]
bn = [i for i in range(121)]

cn = [0 for i in range(121)]

for i in range(1,121):
    cn[i] = (an[i]*bn[i]) + cn[i-1]



def suma(n):
    result = 0
    for i in range(1,n+1):
        result += cn[i]
    return result

def suma_mniejszych(n):
    result = 0
    for i in range(1,n+1):
        if cn[i] < 0:
            result += cn[i]
    return result

def suma_wiekszych(n):
    result = 0
    for i in range(1,n+1):
        if cn[i] > 0:
            result += cn[i]
    return result

print(cn)
def tabelka(n):
    print(f"n:{n} ",suma_mniejszych(n), suma_wiekszych(n),suma(n))

tabelka(6)
tabelka(11)
tabelka(24)
tabelka(120)
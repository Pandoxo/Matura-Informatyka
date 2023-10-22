file = open("liczby.txt", "r")
wyniki = open("wyniki4.txt", "a")

def Fac(n):
    result = 1
    while n >1:
        result *= n
        n -= 1
    return  result


for num in file:
    result = 0
    num= num[:-1]
    for i in range(0,len(num)):
        result += Fac(int(num[i]))

    if result == int(num):
        wyniki.write(f'{num}\n')

primes = []

for i in range(3, 100):
    for j in range(2, i//2+1):
        if i % j == 0:
            break
    else:
        primes.append(i)

file = open("przyklad.txt", "r")
wyniki = open("wyniki4.txt", "a")

def check(n):
    for i in range(0,len(primes)):
        for j in range(i,len(primes)):
            if primes[i] + primes[j] == n:
                return [primes[i], primes[j]]
    return []


result = []
for txt in file:
    num = txt.split()[0]
    result = check(int(num))
    if result:
        wyniki.write(f'{num} {result[0]} {result[1]}\n')


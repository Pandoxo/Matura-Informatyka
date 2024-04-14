import math

file = open("liczby.txt", "r").read().split("\n")
file.pop()
file = [int(x) for x in file]


def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0

    return 1

def ile_rozkladow(num):
    count = 0
    for i in range(2, num // 2+1):
        if pierwsze[i]:
            if pierwsze[num - i]:
                count += 1
    return count

pierwsze = [0] * 1000001
pierwsze[2] = 1

for i in range(2,1000001):
    if prime(i):
        pierwsze[i] = 1

max_count = 0
max_num = 0
min_count = ile_rozkladow(file[0])
min_num = file[0]


for num in file:
    count = 0
    for i in range(2, num//2):
        if pierwsze[i]:
            if pierwsze[num - i]:
                count += 1
    if count > max_count:
        max_count = count
        max_num = num
    elif count < min_count:
        min_count = count
        min_num = num
print(max_num, max_count, min_num, min_count)

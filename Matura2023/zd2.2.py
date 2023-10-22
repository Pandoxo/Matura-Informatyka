file = open("bin.txt", "r")
wyniki = open("wyniki2.txt", "a")
def Blocks(n):
    count = 0
    for i in range(0, len(n)-1):
        if n[i] != n[i+1]:
            count += 1

    return count



count2 = 0
for num in file:
    if Blocks(num) < 3:
        count2 += 1

wyniki.write(str(count2))





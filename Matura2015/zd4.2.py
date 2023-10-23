file = open("liczby.txt", "r")
wyniki = open("wynik4.txt", "a")

dividedEight = 0
dividedTwo = 0
for num in file:
    num = num[:-1]
    if num[-1] == "0":
        dividedTwo += 1
    if num[-4:-1] == "000":
        dividedEight += 1

wyniki.write(f'podzielne przez 2: {dividedTwo}\npodzielne przez 8: {dividedEight}')
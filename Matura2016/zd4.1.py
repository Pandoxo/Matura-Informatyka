file = open("punkty.txt", "r")
wyniki = open("wyniki_4.txt", "a")

count = 0
for point in file:
    point = point[:-1].split(" ")
    x = int(point[0])
    y = int(point[1])
    if pow(x - 200,2) + pow(y-200, 2) == pow(200, 2):
        wyniki.write(f'{x} {y}\n')
    elif pow(x - 200, 2) + pow(y-200, 2) < pow(200, 2):
        count += 1

wyniki.write(str(count))
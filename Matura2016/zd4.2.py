file = open("punkty.txt", "r")
wyniki = open("wyniki_4.txt", "a")

count = 0
countCircle = 0
for point in file:
    count += 1
    point = point[:-1].split(" ")
    x = int(point[0])
    y = int(point[1])
    if pow(x - 200, 2) + pow(y-200, 2) < pow(200, 2):
        countCircle += 1
    if count == 1000:
        wyniki.write(f'Pi dla 1000 punktow: {countCircle/count*4}\n')
    if count == 5000:
        wyniki.write(f'Pi dla 5000 punktow: {countCircle/count*4}\n')


wyniki.write(f'Pi dla wszystkich punktow: {countCircle/count*4}\n')

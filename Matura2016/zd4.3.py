import math

import matplotlib.pyplot as plt

file = open("punkty.txt", "r")
wyniki = open("wyniki_4.txt", "a")

count = 0
countCircle = 0
absoluteErrors = []
for point in file:
    count += 1
    point = point[:-1].split(" ")
    x = int(point[0])
    y = int(point[1])
    if pow(x - 200, 2) + pow(y-200, 2) < pow(200, 2):
        countCircle += 1

    pi = countCircle/count * 4
    absoluteErrors.append(abs(math.pi - pi))
    if count == 1700:
        break

plt.plot([i for i in range(1700)], absoluteErrors)
plt.show()




file = open("przyklad.txt", "r").read().split("\n")
wyniki = open("wyniki6.txt", "a")
ls = []
for line in file:
    ls.append(line.split())

for i in range(0,200):
    for j in range(0,320):
        ls[i][j] = int(ls[i][j])


i, j = 0, 0
count = 0
while i < 199:
    while j < 320:
        if abs(ls[i][j] - ls[i+1][j]) > 128:
            count +=1



file = open("przyklad.txt", "r")
wyniki = open("wyniki4.txt", "a")

couples = []

for txt in file:
    if(int(txt.split()[0]) == len(txt.split()[1])):
        couples.append([int(txt.split()[0]), txt.split()[1]])

minCouple = [couples[0][0],couples[0][1]]

for i in range(0, len(couples) ):
    if couples[i][0] < minCouple[0]:
        minCouple = couples[i]
    if couples[i][0] == minCouple[0]:
        if min(couples[i][0], minCouple[0]) == couples[i][0]:
            minCouple = [couples[i][0], couples[i][1]]

wyniki.write(f'{minCouple[0]} {minCouple[1]}\n')



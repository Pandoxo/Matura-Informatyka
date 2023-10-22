file = open("sygnaly.txt", "r")
wyniki = open("wyniki4.txt", "a")

countWord = 0
result = ""
for word in file:
    countLetter = 0
    countWord += 1
    if countWord > 39 and countWord % 40 == 0:
        result += word[9]

wyniki.write(result)




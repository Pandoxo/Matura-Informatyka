file = open("liczby.txt", "r")
wyniki = open("wynik4.txt", "a")


nums = []
def binToInt(txt):
    result = 0
    for i in range(len(txt)):
        result += int(txt[len(txt)-i-1]) * pow(2,i)
    return result

maxNum = -1
maxLine = 0

minNum = 0
minLine = 0

lineCount = 0


for num in file:
    num = num[:-1]
    integer = binToInt(num)
    if lineCount == 0:
        minNum = integer
    lineCount += 1
    if integer > maxNum:
        maxNum = integer
        maxLine = lineCount
    if integer < minNum:
        minNum = integer
        minLine = lineCount


wyniki.write(f'wiersz najmniejszej liczby to: {minLine}\nwiersz najwiekszej liczby to: {maxLine}')


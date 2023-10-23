file = open("liczby.txt", "r")
wyniki = open("wynik4.txt", "a")

result = 0
for num in file:
    countZeros = 0
    countOnes = 0
    for i in range(len(num)):
        if num[i] == "1":
            countOnes += 1
        else:
            countZeros +=1
    if countZeros > countOnes:
        result += 1

wyniki.write(str(result))
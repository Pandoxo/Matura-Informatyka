file = open("bin.txt", "r")
wyniki = open("wyniki2.txt", "a")

maxInt = -1
maxBin = ""
def BinToInt(num):
    result = 0
    exp = 0
    for i in range(len(num)-2, -1, -1):
        result += int(num[i]) * pow(2, exp)
        exp += 1
        
    return result


for num in file:
    result = BinToInt(num)
    if(result > maxInt):
        maxBin = num
        maxInt = result

wyniki.write(maxBin)
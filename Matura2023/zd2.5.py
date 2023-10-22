file = open("bin.txt", "r")
wyniki = open("wyniki2.txt", "a")


def XOR(a, b):
    if a == b:
        return 0
    return 1


for num1 in file:
    num1 = num1[:-1]
    num2 = "0" + num1[:-1]
    result = ""
    for i in range(0, len(num1)):
        result += str(XOR(num1[i], num2[i]))
    wyniki.write(f'{result}\n')


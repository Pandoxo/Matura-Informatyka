instructions = open("przyklad.txt", "r")

result = []
for inst in instructions:
    fistLetter = inst[0]
    if fistLetter == "D":
        result.append(inst[-2])
        continue
    elif fistLetter == "U":
        result.pop(-1)
        continue
    elif fistLetter == "P":

        for i in range(0, len(result)):
            if result[i] == inst[-2]:
                if ord(result[i]) + 1 > 90:
                    result[i] = chr(ord(result[i]) + 1 - 26)
                else:
                    result[i] = chr(ord(result[i]) + 1)
                break
        continue
    elif fistLetter == "Z":
        result[-1] = inst[-2]
        continue


print(result)
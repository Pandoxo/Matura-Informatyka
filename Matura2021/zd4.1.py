instructions = open("instrukcje.txt", "r")

count = 0
for inst in instructions:
    inst = inst[:-1]
    if "DOPISZ" in inst:
        count += 1
    if "USUN 1" == inst:
        count -= 1

print(count)
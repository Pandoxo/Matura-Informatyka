alphabet = [0 for _ in range(26)]
instructions = open("instrukcje.txt", "r")

for inst in instructions:
    if "DOPISZ" in inst:
        alphabet[ord(inst[-2])-65] += 1

print(f'{chr(max(range(len(alphabet)), key=alphabet.__getitem__)+65)} {max(alphabet)}')
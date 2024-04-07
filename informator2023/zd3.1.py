file  = open("dane3.txt" , "r").read().split("\n")
file.pop()


min_diff1 = 0
min_diff2 = 0
diffs = []
for line in file:
    num1 = int(line.split()[0])
    num2 = int(line.split()[1])
    diffs.append( abs(num2-num1) +1)

diffs.sort()
print(diffs[0],diffs[1])
print(diffs)

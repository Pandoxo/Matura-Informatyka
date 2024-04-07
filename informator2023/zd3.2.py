file = open("dane3.txt", "r").read().split("\n")
file.pop()

dlugosci = [0] * 4047

min_diff1 = 0
min_diff2 = 0
diffs = []
for line in file:
    num1 = int(line.split()[0])
    num2 = int(line.split()[1])
    dlugosci[abs(num2 - num1) + 1] += 1

max_count = max(dlugosci)
for i in range(4047-1,-1,-1):
    if max_count == dlugosci[i]:
        print(i)
        break
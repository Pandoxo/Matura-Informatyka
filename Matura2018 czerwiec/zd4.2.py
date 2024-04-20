file1 = open("dane1.txt", "r").read().split("\n")
file2 = open("dane2.txt", "r").read().split("\n")
file1.pop()
file2.pop()
count = 0
for i in range(len(file1)):
    tab1 = file1[i].split()
    tab2 = file2[i].split()
    even1 = 0
    even2 = 0
    odd1 = 0
    odd2 = 0
    for num in tab1:
        if int(num) % 2 == 0:
            even1 += 1
        else:
            odd1 += 1

    for num in tab2:
        if int(num) % 2 == 0:
            even2 += 1
        else:
            odd2 += 1

    if even1 == 5 and even2 == 5 and odd1 == 5 and odd2 == 5:
        count += 1

print(count)

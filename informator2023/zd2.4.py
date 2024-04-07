file = open("dane2_4.txt" , "r").read().split("\n")

file.pop()

for line in file:
    sum = 0
    for char in line:
        if char == '[':
            sum += 1
        else:
            sum -= 1
    if sum != 0:
        print("NIE")
    else:
        print("TAK")

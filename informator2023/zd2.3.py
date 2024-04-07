file = open("dane2_3.txt" , "r").read().split("\n")

file.pop()

for line in file:
    sum = 0
    max_sum = 0
    for char in line:
        if char == '[':
            sum += 1
        else:
            sum -= 1
        if sum > max_sum:
            max_sum = sum
    print(max_sum)

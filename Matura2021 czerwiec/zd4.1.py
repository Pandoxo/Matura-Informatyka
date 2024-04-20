file = open("napisy.txt", "r").read().split("\n")
file.pop()

count = 0
#48 57

for line in file:
    for char in line:
        if ord(char) > 47 and ord(char) < 58:
            count +=1



print(count)
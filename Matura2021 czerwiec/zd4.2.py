file = open("napisy.txt", "r").read().split("\n")
file.pop()

count = 0
#48 57

pos = 0
password = ""
for i in range(len(file)):
    if (i+1) % 20 == 0:
        password += file[i][pos]
        pos += 1


print(password)
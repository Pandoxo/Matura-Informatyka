file1 = open("dane1.txt", "r").read().split("\n")
file2 = open("dane2.txt" , "r").read().split("\n")
file1.pop()
file2.pop()
count = 0
for i in range(len(file1)):
    num1 = file1[i].split()[-1]
    num2 = file2[i].split()[-1]
    if num1 == num2:
        count += 1


print(count)








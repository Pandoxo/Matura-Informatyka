file = open("dane6.txt", "r").read().split("\n")
file.pop()

def anypalindrom(num):
    n = len(num)
    for i in range(n//2):
        if num[i] == num[n-i-1]:
            return 0

    return 1

count = 0
for num in file:
    if anypalindrom(num):
        count +=1
        print(num)
print(count)
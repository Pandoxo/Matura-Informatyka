file = open("mecz_przyklad.txt", "r").read()
file = file[:-1]
n = len(file)

count = 0
for i in range(1,n):
    if file[i] != file[i-1]:
        count += 1
print(count)
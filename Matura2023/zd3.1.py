file = open("pi.txt", "r").read().split("\n")
wyniki = open("wyniki3.txt", "a")

count = 0
for i in range(len(file)-1):
    if int(file[i])*10 + int(file[i+1]) > 90:
        count += 1

wyniki.write(str(count))

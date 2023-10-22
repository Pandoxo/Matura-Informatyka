file = open("dane.txt", "r")
wyniki = open("wyniki6.txt", "a")

count = 0
for line in file:
    pixels = line.split()
    for i in range(0,320):
        if pixels[i] != pixels[319 -i]:
            count += 1
            break
wyniki.write(str(count))

#Nie wiem



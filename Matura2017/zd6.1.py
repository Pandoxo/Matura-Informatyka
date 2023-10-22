file = open("dane.txt", "r")
wyniki = open("wyniki6.txt", "a")

brightest = 0
darkest = 255

for pixel in file:
    pixels = pixel.split()
    for num in pixels:
        num = int(num)
        if num > brightest:
            brightest = num
        if num < darkest:
            darkest = num

wyniki.write(f'{brightest} {darkest}')
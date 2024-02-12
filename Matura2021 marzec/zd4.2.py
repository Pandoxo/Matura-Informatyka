file = open("galerie_przyklad.txt").read().split("\n")
file.pop()
CountryNationDict = {}

maxSurface = 0
minSurface = 2000
maxCity = ""
minCity = ""

for line in file:
    line = line.split()
    city = line[1]
    surface = 0

    places = 0
    for i in range(2, len(line)-1,2):
        if line[i] == '0':
            break
        else:
            surface += int(line[i]) * int(line[i+1])
            places += 1
    if surface > maxSurface:
        maxSurface = surface
        maxCity = city
    if surface < minSurface:
        minSurface = surface
        minCity = city

    print(city, surface, places)
print("b)")
print(maxCity, maxSurface)
print(minCity, minSurface)




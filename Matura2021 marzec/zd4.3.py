file = open("galerie_przyklad.txt").read().split("\n")
file.pop()
CountryNationDict = {}

minDiffPremises = 0
maxDiffPremises = 0
maxCity = ""
minCity = ""
for line in file:
    line = line.split()
    city = line[1]
    surfacesDict = {}
    diffSameTypeSurfaces = 0
    print(city)
    for i in range(2, len(line) - 1, 2):
        if line[i] == '0':
            break
        else:
            surface = int(line[i]) * int(line[i + 1])
            print(surface, end=" ")
            if surface not in surfacesDict:
                surfacesDict[surface] = 1
            else:
                surfacesDict[surface] += 1
    print()
    for surface_ in surfacesDict:
        if surfacesDict[surface_] != 1:
            diffSameTypeSurfaces += 1

print(maxCity, maxDiffPremises)

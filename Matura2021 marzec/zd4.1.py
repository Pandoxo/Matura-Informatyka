file = open("galerie.txt").read().split("\n")
file.pop()
CountryNationDict = {}

for line in file:
    country = line.split(" ")[0]

    if country in CountryNationDict:
        CountryNationDict[country] += 1
    else:
        CountryNationDict[country] = 1


for country_ in CountryNationDict:
    print(f"{country_} {CountryNationDict[country_]}")

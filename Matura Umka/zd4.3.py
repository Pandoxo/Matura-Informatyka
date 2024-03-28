file = open("konta.txt" , "r").read().split("\n", )


odwrotne = []
for line in file:
    txt = line.split()[1] +" " + line.split()[0]
    odwrotne.append(txt)


count = 0
for para1 in file:
    for para2 in odwrotne:
        if para1 == para2:
            count +=1

print(count/2)
file = open("test.txt" , "r").read().split("\n", )

konta = []
for line in file:
    konta.append(line.split()[0])
    konta.append(line.split()[1])


konta = list(dict.fromkeys(konta))

print(len(konta))
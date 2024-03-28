file = open("konta.txt" , "r").read().split("\n", )

konta = []
for line in file:
    konta.append(line.split()[0])
    konta.append(line.split()[1])


konta = list(dict.fromkeys(konta))
obserwowane = []
for line in file:
    obserwowane.append(line.split()[1])
for konto in konta:
    if konto not in obserwowane:
        print(konto)


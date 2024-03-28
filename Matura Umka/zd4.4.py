file = open("konta.txt" , "r").read().split("\n", )

konta = []
for line in file:
    konta.append(line.split()[0])
    konta.append(line.split()[1])


ilosc_obserwowanych = [0 for i in range(32)]
konta = list(dict.fromkeys(konta))

i =0
maxCount =0
for konto in konta:

    count = 0
    for line in file:
        if line.split()[0] == konto:
            count +=1

    ilosc_obserwowanych[i] = count
    i +=1


print(ilosc_obserwowanych)
Max_ = max(ilosc_obserwowanych)

for i in range(len(ilosc_obserwowanych)):
    if ilosc_obserwowanych[i] == Max_:
        print(konta[i])

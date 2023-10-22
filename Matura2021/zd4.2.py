file = open("przyklad.txt", "r")

ls = []
for inst in file:
    ls.append(inst[:-2])

max = 0
maxInst = ""
count = 1
for i in range(0,len(ls)-1):

    if ls[i] == ls[i+1]:
        count +=1
    else:
        if count > max:
            max = count
            maxInst = ls[i]
        count = 1

print(f'{maxInst} {max}')
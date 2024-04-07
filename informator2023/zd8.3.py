def lis(tab):
    lenght = len(tab)
    max_dl = 0
    max_beginning = 0
    result = []
    for i in range(lenght):
        dl = 1
        for j in range(i,lenght-1):
            if tab[j+1] > tab[j]:
                dl += 1
            else:
                break
        if dl > max_dl:
            max_dl = dl
            max_beginning = i

    for i in range(max_beginning,max_beginning+max_dl):
        result.append(tab[i])

    return result


file = open("dane8.txt", "r").read().split("\n")
file.pop()

liczby = [int(_) for _ in file]

print(len(lis(liczby)))

file = open("pi_przyklad.txt", "r").read().split("\n")
wyniki = open("wyniki3.txt", "a")

ls = [0 for _ in range(100)]

for i in range(len(file)-1):
    fragment = file[i] + file[i+1]
    if fragment[0] == "0":
        ls[int(fragment[1])] += 1
    else:
        ls[int(fragment)] += 1

wyniki.write(f'0{ls.index(min(ls))} {min(ls)}\n')
wyniki.write(f'{ls.index(max(ls))} {max(ls)}')

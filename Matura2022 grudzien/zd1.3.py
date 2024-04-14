file = open("mecz.txt", "r").read()
file = file[:-1]

n = len(file)

max_passa = 0
max_druzyna = ""
A = 0
B = 0
passa = 1
for i in range(n - 1):

    if file[i] == file[i + 1]:
        passa += 1
    else:
        if passa > 9:
            if file[i] == "A":
                A += 1
            else:
                B += 1

            if passa > max_passa:
                max_passa = passa
                max_druzyna = file[i]
        passa = 1


print(f"{A + B} {max_druzyna} {max_passa} ")



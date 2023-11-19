file = open("liczby.txt", "r").read().split("\n")
wyniki = open("wyniki4.txt", "a")

ls_count = [0 for _ in range(10000)]

for num in file:
    ls_count[int(num)] += 1

diffCount = 0
twoReps = 0
threReps = 0
for i in range(10000):
    if ls_count[i] != 0:
        diffCount += 1
    if ls_count[i] == 2:
        twoReps += 1
    if ls_count[i] == 3:
        threReps += 1


wyniki.write(f"{diffCount}\n{twoReps}\n{threReps}")
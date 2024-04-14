file = open("mecz.txt", "r").read()
file = file[:-1]
n = len(file)


A = 0
B = 0
for score in file:
    if score == "A":
        A += 1
    else:
        B += 1
    if (A>B and A > 999 and A-B > 2) or (B>A and B >999 and B-A > 2):
        print(f"A {A}")
        print(f"B {B}")
        break


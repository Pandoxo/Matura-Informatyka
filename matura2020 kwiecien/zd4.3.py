dane = open("dane4.txt", "r").read().split("\n")
dane.pop()
nums = [int(i) for i in dane]

luki = []
for i in range(len(nums) - 1):
    luka = abs(nums[i] - nums[i + 1])
    luki.append(luka)

iloscKrotnosci = dict((i, luki.count(i)) for i in luki)

maxKrotnosc = max(iloscKrotnosci.values())

print("najczestsze luki:")
for luka in iloscKrotnosci:
    if iloscKrotnosci[luka] == maxKrotnosc:
        print(luka)
print(f"Maksymalna krotnosc: {maxKrotnosc}")

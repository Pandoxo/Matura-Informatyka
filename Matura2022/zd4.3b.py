file = open("liczby.txt", "r")
fives= open("piatki.txt", "w")

nums = []
for num in file:
    nums.append(int(num))

inum1 = 0
inum2 = 0
inum3 = 0
inum4 = 0
inum5 = 0

count = 0
l = len(nums)
while inum1 < l:
    while inum2 < l:
        if nums[inum2] % nums[inum1] == 0 and nums[inum2] != nums[inum1]:
            while inum3 < l:
                if nums[inum3] % nums[inum2] == 0 and nums[inum3] != nums[inum2]:
                    while inum4 < l:
                        if nums[inum4] % nums[inum3] == 0 and nums[inum4] != nums[inum3]:
                            while inum5 < l:
                                if nums[inum5] % nums[inum4] == 0 and nums[inum5] != nums[inum4]:
                                    fives.write(f'{nums[inum1]} {nums[inum2]} {nums[inum3]} {nums[inum4]} {nums[inum5]}\n')
                                    count += 1
                                inum5 += 1
                        inum4 += 1
                        inum5 =0
                inum3 += 1
                inum4 = 0
        inum2 += 1
        inum3 =0
    inum1 += 1
    inum2 = 0

print(count)

#moza posortowac liste nums i troche zoptymalizowac algorytm

file = open("przyklad.txt", "r")
trojki = open("trojki.txt", "w")

nums = []
for num in file:
    nums.append(int(num))

inum1 = 0
inum2 = 0
inum3 = 0
count = 0
while inum1 < len(nums):
    while inum2 < len(nums):
        if nums[inum2] % nums[inum1] == 0 and nums[inum2] != nums[inum1]:
            while inum3 < len(nums):
                if nums[inum3] % nums[inum2] == 0 and nums[inum3] != nums[inum2]:
                    trojki.write(f'{nums[inum1]} {nums[inum2]} {nums[inum3]}\n')
                    count += 1
                inum3 += 1

        inum2 += 1
        inum3 = 0
    inum1 += 1
    inum2 = 0

print(count)

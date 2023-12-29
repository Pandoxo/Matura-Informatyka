dane = open("dane4.txt", "r").read().split("\n")
dane.pop()
nums = [int(i) for i in dane]

luki = []
for i in range(len(nums) - 1):
    luka = abs(nums[i] - nums[i + 1])
    luki.append(luka)

longest = 0
longestEndIndex = 0
count = 1
for i in range(len(luki) - 1):
    if luki[i] == luki[i + 1]:
        count += 1
    else:
        if count > longest:
            longest = count
            longestEndIndex = i + 1
        count = 1

print(longest + 1)
print(f"first {nums[longestEndIndex - longest]} last {nums[longestEndIndex]}")

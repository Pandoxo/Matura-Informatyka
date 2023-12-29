dane = open("dane4.txt", "r").read().split("\n")
dane.pop()
nums = [int(i) for i in dane]

luki = []
for i in range(len(nums) - 1):
    luka = abs(nums[i] - nums[i + 1])
    luki.append(luka)
print(luki)
print(min(luki))
print(max(luki))

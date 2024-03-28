file = open("dane.txt", "r").read().split("\n")
file.pop()

# nums = [int(_) for _ in file]
nums = [i for i in range(1, 10001)]

i = 0
step = 2

for i in range(1,len(nums)):
    nums.pop(i)

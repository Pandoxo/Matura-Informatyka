file = open("napisy.txt", "r").read().split("\n")
file.pop()

def wordFromNums(tab):
    result = ""
    for num in tab:
        if int(num) > 64 and int(num) < 91:
            result += chr(int(num))
    return result

password = ""
for line in file:
    nums = []
    for char in line:
        if ord(char) > 47 and ord(char) < 58:
            nums.append(char)
    if len(nums) % 2 ==1:
        nums.pop()

    if len(nums) >1:
        pairs = []
        pair = ""
        for i in range(len(nums)):
            pair += nums[i]
            if len(pair) ==2:
                pairs.append(pair)
                pair = ""
        password += wordFromNums(pairs)
        if password[-3:] == "XXX":
            break
print(password)


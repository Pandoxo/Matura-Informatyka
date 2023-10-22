pi = open("pi_przyklad.txt", "r")
piList = []
i = 0
for num in pi:
    piList.append(num)

def check(ls):
    i = 0
    count = 1
    while(i < 5):
        if ls[i] <= ls[i+1]:
            count+=1
            i+=1
        else:
            break
    while(i < 5):
        if ls[i] >= ls[i+1]:
            count += 1
            i+=1
        else:
            break
    if count == 6:
        return True
    else:
        return False

result = 0
for i in range(0, len(piList) - 6):
    nums = []
    for j in range(0, 6):
        nums.append(piList[i+j])
    if check(nums):
        result += 1

print(result)












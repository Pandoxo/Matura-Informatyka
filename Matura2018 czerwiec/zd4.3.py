file1 = open("dane1.txt", "r").read().split("\n")
file2 = open("dane2.txt", "r").read().split("\n")
file1.pop()
file2.pop()
count = 0
for i in range(len(file1)):
    tab1 = file1[i].split()
    tab2 = file2[i].split()
    nums1 = [0]*100
    nums2 = [0]*100
    for num in tab1:
        nums1[int(num)] +=1
    for num in tab2:
        nums2[int(num)] +=1

    for i in range(10):
        if nums1[i] != 0 and nums2[i] != 0:
            count += 1


print(count)





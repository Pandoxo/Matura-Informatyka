file = open("przyklad.txt", 'r')
i =1
first = 0
count = 0
for num in file:
    num = num[:-1]
    if(num[0] == num[len(num)-1]):
        if(i>0):
            first = num
            i-=1
        count +=1

print(first)
print(count)


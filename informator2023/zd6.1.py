file = open("dane6.txt" , "r").read().split("\n")
file.pop()

def check(num,p):
    contains_p_1 = False
    for integer in num:
        if int(integer) > p-1:
            return 0
        if int(integer) == p-1:
            contains_p_1 = True
    if contains_p_1:
        return True



for p in range(2,11):
    count = 0
    for num in file:
        if check(num,p):
            count +=1
    print(p,count)





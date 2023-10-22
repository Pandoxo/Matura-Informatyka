file = open("liczby.txt" , "r")

def check(n):
    base = 3
    result = 1
    while result<n:
        result *= base
        if result == n:
            return True
    return False


count = 0
for num in file:
    if check(int(num)):
        count+=1

print(count)
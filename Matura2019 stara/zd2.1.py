import math

def prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            return 0
    return 1

def pot(a,k):
    result = a
    for i in range(k):
        result *=a
    return a%k

def testF(k):

    for a in range(2,k):
        if pot(a,k) != a:
            return 0
    return 1

def czyLC(k):
    if testF(k) ==1 and prime(k) ==0:
        return 1
    else:
        return 0

print(pot(4,3))
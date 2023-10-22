def Blocks(n):
    last = None
    count = 0
    while(n>0):
        if(last != n%2 ):
            count+=1
        last= n%2
        n //= 2

    return count

print(Blocks(245))



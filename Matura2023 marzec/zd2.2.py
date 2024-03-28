A = [_ for _ in range(5, 101, 5)]
s =500
B = [0 for x in range(0, s+1)]

B[0] =1

print(B)
print(A)
def CountOnes(l):
    result = 0
    for num in l:
        if num == 1:
            result +=1

    return result
def Tura(k):
    i = s
    while i >= A[k]:
        if B[i - A[k]] == 1 and B[i] == 0:
            B[i] = 1
            print(B)
        if B[s] == 1:
            print("sukces")
            print(CountOnes(B))
            break

        i -= 1



for k in range(len(A)):
    Tura(k)

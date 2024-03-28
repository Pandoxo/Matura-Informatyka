file = open("krosno.txt" , "r").read().split('\n')

def czy_k_rosnaca(A,k_):
    for i in range(100-k_):
        if A[i] > A[i+k]:
            return False
    return True
for k in range(1,100):
    if czy_k_rosnaca(file,k):
        print(k)



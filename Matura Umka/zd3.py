


A=[[4,2,1,10,5],[0,4,22,2,8],[40,1,1,1,1],[0,4,22,2,8],[0,4,22,2,8]]
def Kop(A,n,m,i,j):

    if n==5 and m==5 and i==3 and j==3:
        print("_")

    if i > n or j> m:
        return 0
    k1 = Kop(A,n,m,i+1,j)
    k2 = Kop(A,n,m,i,j+1)
    if k1>k2:
        return A[i-1][j-1] + k1
    else:
        return A[i-1][j-1] + k2



print(Kop(A,5,5,1,1))
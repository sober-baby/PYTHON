L = [1, [2,3], 4]
L1 = L[:]
L[0] = 7
L[1][0] = 8
L1[1][1] = 9
print(L)
print(L1)



def g(L):
    L[1][0] = 3

L = [4 ,[2,3] ,6]
g(L)
print(L)

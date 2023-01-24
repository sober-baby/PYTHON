# lists of lists
M = [[1, 2, 3, 4],
    [1, 0, 1, 0],
    [2, 2, 3, 5]]

print(M[1])
print(M[2][1])

for row in M:
    print(row)

for col_i in range(len(M[0])):
    for row_i in range(len(M)):
        print(str(M[row_i][col_i]) + " ")
    print("")

def Mult_M_v(M, v):
    ''' Multiply matrix M by vector v'''
    res = []
    for row_i in range(len[M]):
        dot_pr = 0
        for col_i in range(len(M[0])):
            dot_pr += M[row_i][col_i] * v[col_i]
        res.append(dot_pr)

    return res
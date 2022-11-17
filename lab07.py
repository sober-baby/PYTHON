import numpy as py

#question 1
def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

#question 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

#question 3
def get_row_to_swap(M, start_i):
    a = get_lead_ind(M[start_i])
    min = start_i
    for i in range(start_i, len(M)):
        if a > get_lead_ind(M[i]):
            a = get_lead_ind(M[i])
            min = i
    return min

#question 4
def add_rows_coefs(r1, c1, r2, c2):
    list = []
    for i in range(len(r1)):
        list.append(r1[i]*c1 + r2[i]*c2)
    return list

#question 5
def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        factor = -(M[i][best_lead_ind])/(M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[i] ,1 ,M[row_to_sub], factor)

#question 6
def forward_step(M):
    for i in range(len(M)):
        r = get_row_to_swap(M,i)
        tempr = M[r]
        M[r] = M[i]
        M[i] = tempr
        lead = get_lead_ind(M[i])
        eliminate(M,i,lead)
        print(py.array(M),"\n")


#question 7


M = [[ 0, 0, 1, 0, 2],
[ 1, 0, 2, 3, 4],
[ 3, 0, 4, 2, 1],
[ 1, 0, 1, 1, 2,]]

M2 = [[ 1, -2, 3, 22],
[ 3, 10, 1, 314],
[ 1, 5, 3, 92]]
forward_step(M2)
print(M2)
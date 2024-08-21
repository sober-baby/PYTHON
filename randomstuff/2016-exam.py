def insert(L, e):
    return sorted(L + [e])

a = insert([], 42.0)
print(a)

def select_gifts(good_ratings, want_ratings):
    dict = {}
    for gift in good_ratings:
        dict[gift] = good_ratings.get(gift, 0) + want_ratings.get(gift, 0)


good_ratings = {"Calc textbook": 5, "iPhone": 1, "Alarm clock": 4, "Notebooks": 4}
want_ratings = {"iPhone": 4, "A+ in CSC": 5, "Calc textbook": 4, "Notebooks": 5}
print(select_gifts(good_ratings, want_ratings))

def transpose(M):
    t_list = [] * len(M[0])
    for i in range (len(M[0])):
        row = []
        for j in range (len(M)):
            row.append(M[j][i])
        t_list.append(row)
    return t_list

print(transpose([[5, 6, 7], [0, -3, 5]]))

def max_rec(L):
    if len(L) == 1:
        return L[0]

    res1 = max_rec(L[1:])


    if res1 > L[0]:
        return res1
    else:
        return L[0]

print(max_rec([103, 110, 180]))


A = [[1, 2], [3, 4]]
A[0] = A[1]
B = A[:][0]
print(B)
B[0] = 5
print(A)

def f(L, M):
    L = M
    L[0] = 3
M = [1, 2]
L = [3, 4]
f(L, M)
print(M[0])
print(L)



s1 = "HO HO HO"
s2 = s1
s1 = "Happy Holidays!"
print(s2)
'''
O(n)
O(n^2)
O(logn)
O(n)
'''

def sorted_timestamps(L):
    for i in range (len(L) - 1):
        if L[i+1][0] * 60 + L[i+1][1] < L[i][0] * 60 + L[i][1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = L[i]
    return L

print(sorted_timestamps([(5, 10), (2, 40), (22, 59), (5, 10)]))

sorted_timestamps([(5, 10), (2, 40), (22, 59), (5, 10)])
print(sorted_timestamps[0][1])







































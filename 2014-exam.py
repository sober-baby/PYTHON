'''
def most_productive_elf(toys_produced):
    max_elf = ""
    max_count = -1
    for elf, num in toys_produced.items():
        if num > max_count:
            max_count = num
            max_elf = elf
    return max_elf

toys = {"Bob":4000, "Gloria":7000, "Hugo":6000, "Grumbles":42}

print(most_productive_elf(toys))

def two_smallest(L):
    L1 = L
    list = []
    min = L1[0]
    for i in range (1, len(L1)):
        if(L1[i] < min):
            min = L1[i]
    L1.remove(min)
    min_2 = L1[0]
    for i in range (1, len(L1)):
        if(L1[i] < min_2):
            min2 = L1[i]
    list.append(min_2)
    list.append(min)
    return(list)

L = [1,2,3,4,5]
L = two_smallest(L)
print(L)

# the time complexity othe function

def two_smallest(L):
    m1, m2 = max(L[0], L[1]), min(L[0], L[1])
    for i in range(2, len(L)):
        if L[i] < m1:
            m1, m2 = max(m2, L[i]), min(m2, L[i])

    return [m1, m2]



def largest_col_sum(M):
    temp = 0
    max = 0
    list = []
    for i in range(len(M[0])):
        for j in range(len(M)):
            temp += M[j][i]
            list.append(temp)
        temp = 0
    for i in list:
        if i > max:
            max = i
    return max


L = [ [1, 2, 3, 4], [5, 0, 5, 0], [6, 7, 8, 9]]
print(largest_col_sum(L))


def f(n):
    n = 5
m = 2
f(m)
print(m)

L = [[1, 2], 3]
M = L[:]
M[0][1] = 5
M[1] = 5
print(L)
'''

def f(d):
    d1 = {}
    for k in d:
        d1[k] = d[k]
    return d1

d = {1:[[1, 2]], 0:[[3, 4]]}
d1 = f(d)
d1[1][0][0] = 5
print(d[1])

s = "HO HO HO"
su = s
s = "Merry Christmas!"
print(su)

#question 5

# O(n)
# O(5n)
# O(nk(k+1)/2)

def filter_out_odds(L):



print(filter_out_odds([5, -2, 4, 0, 3, 7, 8]))










































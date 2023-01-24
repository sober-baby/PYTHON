
'''
def f(L):
    L = [5, 6]
    L[1] = 6 #changing something in the memory

L = [6, 7]
f(L)
print(L)

# lists of lists


'''
'''
res = []
L1 = [1,2,3,4]
L2 = [6,7,8,9]
res.append([0] * L2[2])
print(res)
'''
'''
d = {"bro": 1, "lol": 1}
res = d.values()
for k in grades:
    res.append
    '''

    '''
d = {"bro": 1, "lol": 1}
res = []
res1 = []
for k, v in d.items():
    res.append(v)
    res1.append(k)

print(res)
print(res1)

'''


def add_sparse_matrices(A, B, dim):
  res = []
  for i in range(dim[0]):
    res.append([0] * dim[1])

  for coords, value in A.items():
    res[coords[0]][coords[1]] += value

  for coords, value in B.items():
    res[coords[0]][coords[1]] += value
  return res


dim = (2,3)
d = {(0,0): 5, (1,2): 1}
print(d.values)





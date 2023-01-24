def merge(L1, L2):
    '''Return a list that contains the elements of lis1 and lis2 and is sorted
    Precondition: lis1 and lis2 are sorted

    '''
    i, j = 0, 0
    #L1[:i] was already processed
    #L2[:j] was already processed
    merged = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    #Only one of L1[i:] and L2[j:] is non-empty, so we can just append
    #them both in arbitrary order
    merged.extend(L1[i:])
    merged.extend(L2[j:])

    return merged


def merge_sort(L):
    '''Return a sorted version of lis

    '''
    #base case
    if len(L) <= 1:
        return L[:] #return a copy of L
                      #need to return a copy in case the user wants to modify
                      #the original lis and also modify the copy; so they
                      #need to be kept separated

    #Sort the first half, sort the second half, and then merge the two halves!
    mid = len(L)//2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

L = [2,4,1,3,5,6,2,4]
L1 = merge_sort(L)
print(L1)





A = [[1 ,2], [3,4]]
print(A)
print("check1:",A[:][:][:][:][:][:])
B = A[:][0]
print(B)
B[0] = 5
print(B)













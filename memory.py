
'''
L = [1, [2,3], 4]
L1 = L
L1 = [1, [3,3], 4]
print(L)
print(L1)


def g(L):
    L[1][0] = 3

L = [4 ,[2,3] ,6]
g(L)
print(L)
'''


# Binary Search in python


def binarySearch(array, x, low, high):

    mid = low + (high - low)//2

    # If found at mid, then return it
    if array[mid] == x:
        return mid

    # Search the left half
    elif array[mid] > x:
        return binarySearch(array, x, low, mid-1)

        # Search the right half
    else:
        return binarySearch(array, x, mid + 1, high)


array = [3, 4, 5, 6, 7, 8, 9, 10]
x = 4
result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")



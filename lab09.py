
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

x = power(2, 4)
print(x)



def interleave(L1, L2):
    if len(L1) == 0:
        return []
    else:
        return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

L1 = [1, 3, 5]
L2 = [2, 4, 6]
L = interleave(L1, L2)
print(L)

def reverse_rec(L):
    if len(L) == 0:
        return []
    else:
        return [L[-1]] + reverse_rec(L[:-1])

L_reverse = reverse_rec(L1)
print(L_reverse)


L = [1,2,3,4,5]
def zigzag1(L):
    n = len(L)
    a = n//2
    if len(L) == 1:
        print(L[0])
    elif n % 2 == 0:
        print(L[a-1], end = "")
        zigzag1(L[:a-1] + L[-a:])
    else:
        print(L[a], end = "")
        zigzag1(L[:a] + L[-a:])
zigzag1(L)

def is_balanced(s):
    a = s.find("(")
    b = s.find(")")
    if a and b == -1:
        return True
    if a != -1 and b == -1:
        return False
    if b != -1 and a == -1:
        return False
    else:
        if a < b:
            return(is_balanced(s[:a] + s[a + 1:b] + s[b+1:]))
        else:
            return(is_balanced(s[:b] + s[b + 1:a] + s[a+1:]))


a = "(()())"
print(is_balanced(a))





















def get_perfect_square(n):
    res = []
    count = 0
    temp = 0
    while temp < n:
        temp = count * count
        res.append(temp)
        count += 1
    return res

r = get_perfect_square(2)
print(r)

res = [[]] * 5
print(res)
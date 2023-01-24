def get_nums(L):
    c = []
    for i in range(len(L)):
        for j in range(len(L[i])):
            if type(L[i][j]) == type(2.0) or type(L[i][j]) == type(2):
                c.append(L[i][j])
    return c

def loopup(L, num):
    c = ""
    for i in range(len(L)):
        for j in range(len([L][j])):
            if L[i][j] == num:
                c = append(L[i][j])
                return c
            else:
                return "None"

L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]

if __name__ == '__main__':
    print(L[2][1])
    #print(len(L[0]))
    print(get_nums(L))
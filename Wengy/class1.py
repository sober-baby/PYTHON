def solution(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            intlist = [int(x) for x in str(numbers[j])]
            if numbers[i] == numbers[j]:
                count += 1
            else:
                for k in range(len(intlist)-1):
                    for l in range(k+1, len(intlist)):
                        tempintlist = intlist.copy()
                        tempintlist[k], tempintlist[l] = tempintlist[l], tempintlist[k]
                        num = int(''.join(map(str, tempintlist)))
                        if num == numbers[i]:
                            count += 1
                    
            
    
    return count


def solution2(matrix):
    re = []
    
    
    return re



    
    

    
    
if __name__ == '__main__':
    numbers = [1,23,156,1650,651,165,32]
    print(solution(numbers))
    matrix = [[2,3,2],
              [0,2,5],
              [1,0,1]]
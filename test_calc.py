import lab02
lab02.initialize()
lab02.add(41)

def count_evens(L):
    count = 0
    for num in L:
        if(num%2 == 0):
            count+=1
    return count

def list_to_str(lis):
    word = ""
    for a in lis:
        word =  word + str(a)
    return word

def lists_are_the_same(list1, list2):
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


def list1_start_with_list2(list1, list2):
    boolean = False
    if len(list2) <= len(list1):
        for a in range(len(list2)):
            if list1[a] == list2[a]:
                boolean = True
            else:
                return False
    return boolean


def match_pattern(list1, list2):
    i = 0
    boolean = False
    while i <= (len(list1) - len(list2)):
        for a in range(len(list2)):
            if list1[i+a] == list2[a]:
                boolean = True
            else:
                return False
        i += 1
    return boolean

def duplicates(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i + 1]:
            return True

    return False

if __name__ == '__main__':
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
    list1 = [0,1,2,3,4]
    list2 = [1,2,3,4]

    #print(count_evens(list1))
    #print("hello"+"python")
    #print(list_to_str(list2))
    #print(lists_are_the_same(list1,list2))
    print(list1_start_with_list2(list1,list2))
    #print(duplicates(list1))
    #print(match_pattern(list1, list2))






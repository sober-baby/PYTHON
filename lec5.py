def f(x):
    res = x**2
    return res

#have the function accesss a global variable

def g():
    return y**2

def a():
    global y
    y = y + 5
    
def adjust_grade():
    global grade
    while grade < 1000:
        grade += 3
    
if __name__ == '__main__':
    #while True:
    #my_res = f(5)
    y = 5
    a()
    print(g())
    #print(a())
    print(f(54))
    
    grade = 90
    adjust_grade()
    print(grade)
        

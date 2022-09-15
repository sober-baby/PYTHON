# functions

#f(x, y) = 2*x*y - 5

def f(x, y): #function signiture - name of function #parameters - variables that you plug into the function #aguments - actual values that you put into the parameters
    res = 2 * x * y - 5
    return res

def g(x, y):
    return 2 * x * y - 5

def prod(x, y):
    return x * y
# #
def pirate_print(s):
    ''' Print the piratified version of the string s

    '''
    print("Ahoy!" + s +" Arrgh!")

def actually_plunder_grade():
    global grade
    grade = 95

def has_roots(a, b, c):
    disc = b**2-4*a*c
    return disc >= 0

if __name__ == '__main__':
    my_prod = prod(2, 5)
    print(my_prod)
    pirate_print("I love CIV!")
    print(has_roots(1,2,3))
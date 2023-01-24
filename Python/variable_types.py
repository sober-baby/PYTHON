# variable types
# int (integer): a whole number
# float: floating point number

def f(x):
    print("I am about to compute a square, horray!")
    return x**2
    print("hi") # won't execute

def artsie_math(arg1, arg2, op):

    if op!= "+" and op != "-":
        print("Too hard")
        return
    if op == "+":
        return arg1 - arg2
    elif op == "-":
        return  arg1 - arg2
    else:                       #what is this used for?

        print("Too hard")




if __name__ == '__main__':

    print(artsie_math(1, 2, "lol"))
    print(f(5))
    str(42)  # converting a int to a string
    print("lmao" + str(42))

    print("ESE", 180)
    print("CSC", 180, sep = "!", )
    float(5)
    int(5.0)

    round(101)



    # naming

    # a valid name for a variable or function starts with a letter or an underscore and contains only letters, numbers and underscores

    # pathole case
    num_courses_engsci = 6

    # you can use all caps to refer to a constant
    PI = 3.1415916
import math

a = 1
b = -10
c = 1

#(x-2)(x+1) = x^2-x-2

disc = b**2 - 4*a*c
if disc > 0:
        r1 = (-b+math.sqrt(disc))/(2*a)
        r2 = (-b-math.sqrt(disc))/(2*a)
        print(r1, r2)
elif disc == 0:
    r = -b/(2*a)
    print(r)
else:
    print("No solution")


x = 9.3845186345186354168354168
print((a*x**2+b*x+c - r1**2-r1*2+c) == 0)  #ask Aiden

# multiple assignments
a = 5
a, b = 5, 6

# swapping multiple assignments
a, b = b, a

# swapping with a temporary variable
temp = a
a = b

# swap the values without using temp or assignments to be done
a = a + b


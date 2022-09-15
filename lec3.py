a = 10
if a > 5:
    print(">5")
elif a > 3:
    print(">3")
else:
    print("else")

b = 5
if a == "hi":
    print("hi")
elif a == "hello":
    print("hello")
elif a == "hi" and b == 5:
    print("idk")

# solve ax^2 + bx + c = 0

a = -1
b = -1
c = 1

#(x-2)(x+1) = x^2-x-2

disc = b**2 - 4*a*c
if disc > 0:
        r1 = (-b+math.sqrt(disc))/(2*a)
        r1 = (-b-math.sqrt(disc))/(2*a)
        print(r1, r2)
elif disc == 0:
    r = -b/(2*a)
    print(r)
else:
    print("No solution")


# string literals (no double quotes together, but single can go in double quote and double can go in single quote)

print('Arsties are "smart"')
print("Arsties are \"smart\"") # "\" way of telling python that
print("\\")

# multiline string
r = '''abc
asd
asd'''

f = "12\n34"
























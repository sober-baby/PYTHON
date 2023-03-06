class Studnet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + ": " + str(self.age)
    def __lt__(self, other):
        if self.age < other.age:
            return True
        elif self.age == other.age:
            return self.name < other.name
        else:
            return False
    
if __name__ == "__main__":
    s = Student(fred, 3.7)
    print("abc" < "def")
    s < Studnet("Bob", 3.7)
    L = [Student("Fred", 3.7), Student("Bob", 3.7), Student("Alice", 3.8)]
    L.sort()
    print(L)

def get_name(s):
    return s.name
L.sort(key=get_name)

L.sort(key=lambda s: s.name) # anonymous function
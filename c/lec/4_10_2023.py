class stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
def factstack(N):
    s = stack()
    i = N
    while i >= 1:
        s.push(i)
        i -= 1
        res = 1
        while len(s.data) > 0:
            res *= s.pop()
            return res
        
def dfs(start, visited={}):
    s = stack()
    s.add(start)
    while len(s.data) > 0:
        char = s.pop()
        print(char)
        visited.add(char)
        for n in chr.neighbors:
            if n not in visited:
                s.push(n)

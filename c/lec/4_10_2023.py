class stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def add(self, item):
        self.data.append(item)
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
        
def dfs1(start, visited={}):
    s = stack()
    s.add(start)
    while len(s.data) > 0:
        char = s.pop()
        print(char)
        visited.add(char)
        for n in chr.neighbors:
            if n not in visited:
                s.push(n)

def dfs2(start, visited = {}):
    print(start)
    visited.add(start)
    for n in start.neighbors:
        dfs2(n, visited)
        
        
#all the password of length 3
#over alphabet "ab"
    ""
    / \
   "a" "b"
   /    \    
    "aa"   "ab"
    /      \
    "aaa"   "aab"
    

class CirQueue:
    def __init__(self, n):
        self.data = []
        self.n = n
        for x in range(n):
            self.data.append(None)
        self.start = 0
        self.end  = 0
        
    def __str__(self): # print out all values in the queue and return a string
        string = ''
        i = self.start
        lol = True 
        if self.start == self.end:
            if self.data[self.start] == None:
                return string
            else:
                self.start += 1
                lol = False

        while i != self.end:
            string += str(self.data[i]) + ' '
            i = (i + 1) % self.n1
            
        if lol == False:
            self.start = self.start - 1
            
        return string
                
    def enqueue(self, item):
        self.data[self.end] = item
        self.end = (self.end + 1) % self.n
        return
            
    def dequeue(self):
        # return self.data.pop()
        ret_val = self.data[self.start]
        self.data[self.start] = None # O(n), because need to move self.data[1:] to self.data[0:]
        self.start = (self.start + 1) % self.n
        return ret_val
    
    def __lt__(self, other): #comparing two queues lexicographically
        si = self.start
        oi = other.start
        output = False
        while si != self.end and oi != other.end:
            if self.data[si] < other.data[oi]:
                output = True
                break
            elif self.data[si] > other.data[oi]:
                output = False
                break
            else:
                si = (si + 1) % self.n
                oi = (oi + 1) % other.n
    
if __name__ == "__main__":
    q1 = CirQueue(4)
    q1.enqueue(100)
    print(q1)
      

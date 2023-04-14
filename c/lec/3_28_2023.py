class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.cur_num_nodes = 0
        self.indicies = {}
class AdajacencyMatGraph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.cur_num_nodes = 0
        self.indicis = {}
        self.adajacency_mat = []
        for i in range(n_nodes):
            self.adajacency_mat.append([0] * n_nodes)
    def connect_by_index(self, node1, node2):
        self.adajacency_mat[node1][node2] = 1

    def register_node(self):
        if self.cur_num_nodes == self.n_nodes:
            self.n_nodes *= 2
            adj_mat_new = []
            for i in range(self.n_nodes):
                self.adajacency_mat.append([0] * self.n_nodes)
                adj_mat_new[:self.n_nodes//2] = self.adajacency_mat[i]
            for i in range(self.n_nodes//2, self.n_nodes):
                adj_mat_new.append([0] * self.n_nodes)
        if self.cur_num_nodes < self.n_nodes:
            self.names[name] = self.cur_num_nodes
            self.cur_num_nodes += 1
            
    def connect_by_name(self, node1, node2):
        ''' Connect the node named node1 to the node named node2
            if node1 or node2 are not in the graph and there is a space
            add them to the graph'''
        if node1 not in self.indices:
            self.register_node(node1)
        if node2 not in self.indices:
            self.register_node(node2)
        self.connect(self.indices[node1], self.indices[node2])
            
        
if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    a.adjacent.append(b)
    a.adjacent.append(c)
    b.adjacent.append(c)
    

    
    
#  b  ->   c
#   ^     ^
#    \   /
#      a
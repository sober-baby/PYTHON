import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []
        self.distance_from_start = np.inf

class Con: # Connection
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

def dijkstra(start, end):
    start.distance_from_start = 0
    visited = set([start])
    current = start
    while current != end:
        cur_dist = np.inf
        cur_v = None
        for node in visited:
            for con in node.connections:
                if con.node in visited:
                    continue
                if cur_dist > node.distance_from_start + con.weight:
                    cur_dist = node.distance_from_start + con.weight
                    cur_v = con.node
        current = cur_v
        current.distance_from_start = cur_dist
        visited.add(current)
    return current.distance_from_start

if __name__ == '__main__':
    # Create nodes
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')

    # Create connections
    A.connections = [Con(B, 1), Con(D, 2)]
    B.connections = [Con(C, 2), Con(D, 3)]
    C.connections = []  # C has no outgoing connections
    D.connections = [Con(E, 4)]
    E.connections = []  # E has no outgoing connections

    # Test Dijkstra's algorithm
    start_node = A
    end_node = E
    shortest_path_distance = dijkstra(start_node, end_node)
    print(shortest_path_distance)


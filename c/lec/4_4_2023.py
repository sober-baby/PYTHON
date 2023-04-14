from graph import Graph, Node

def bfs(graph, start):
    visited = set() 
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node.data)
            visited.add(node)
            queue.extend(node.neighbors)
    return visited
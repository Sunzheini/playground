# ------------------------------------------------------------------
## Graphs
# ------------------------------------------------------------------
# G(V, E) is a set of vertices / nodes V (нодове) and a set of edges E (ребра)

# Adjacency List Representation of a Graph
graph = [
    ['B', 'C'],       # Neighbors of A
    ['A', 'D'],       # Neighbors of B
    ['A', 'D'],       # Neighbors of C
    ['B', 'C'],       # Neighbors of D
]


def print_graph(g):
    for i, neighbors in enumerate(g):
        print(f"Node {chr(65 + i)}: {', '.join(neighbors)}")


# print_graph(graph)

# ------------------------------------------------------------------
# Adjacency Matrix Representation of a Graph

adjacency_matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0],  # D
]

def print_adjacency_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(' '.join(str(x) for x in row))


# print_adjacency_matrix(adjacency_matrix)

# ------------------------------------------------------------------
# List of Edges Representation of a Graph

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
]

# Function to print edges in a readable format
def print_edges(edges):
    print("Edges:")
    for edge in edges:
        print(f"{edge[0]} - {edge[1]}")


# print_edges(edges)

# ------------------------------------------------------------------

# Dictionary Representation of a Graph

graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}


def print_graph_dict(graph):
    print("Graph Dictionary:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")


# print_graph_dict(graph_dict)

# ------------------------------------------------------------------

# OOP Representation of a Graph

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def print_graph(self):
        for node, neighbors in self.adjacency_list.items():
            print(f"{node}: {', '.join(neighbors)}")


# g = Graph()
# g.add_edge('A', 'B')

# ------------------------------------------------------------------

# Depth-First Search (DFS) Implementation
# visits nodes successors first, implemented using recursion

directional_graph_dfs = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    6: []
}


def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph.get(node, []):  # .get handles missing keys gracefully
        dfs(child, graph, visited)
    print(node, end=' ')


def dfs_start(graph):
    visited = set()
    for node in graph:  # Assumes graph has all nodes as keys
        dfs(node, graph, visited)


dfs_start(directional_graph_dfs)
print()

# ------------------------------------------------------------------

# Breadth-First Search (BFS) Implementation
# first visits neighbors of the current node, implemented using a queue


from collections import deque


directional_graph_bfs = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    6: []
}


def bfs(node, graph, visited):
    queue = deque([node])
    visited.add(node)

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for child in graph.get(current, []):
            if child not in visited:
                visited.add(child)
                queue.append(child)


def bfs_start(graph):
    visited = set()
    for node in graph:  # Assumes graph has all nodes as keys
        dfs(node, graph, visited)


bfs_start(directional_graph_bfs)
print()

# ------------------------------------------------------------------

# Topological Sorting Implementation: ordering of vertices in a directed acyclic graph (DAG)

def topological_sort_util(node, visited, stack, graph):
    visited.add(node)
    for child in graph.get(node, []):
        if child not in visited:
            topological_sort_util(child, visited, stack, graph)
    stack.append(node)


def topological_sort(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            topological_sort_util(node, visited, stack, graph)

    stack.reverse()  # Reverse the stack to get the correct order
    return stack


# Example usage of topological sort
graph_dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}


sorted_order = topological_sort(graph_dag)
print("Topological Sort Order:", sorted_order)

# ------------------------------------------------------------------




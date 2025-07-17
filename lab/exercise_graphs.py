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


print_graph(graph)

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


print_adjacency_matrix(adjacency_matrix)

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


print_edges(edges)

# ------------------------------------------------------------------

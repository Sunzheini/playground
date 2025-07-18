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


# dfs_start(directional_graph_dfs)
# print()

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


# bfs_start(directional_graph_bfs)
# print()

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


# sorted_order = topological_sort(graph_dag)
# print("Topological Sort Order:", sorted_order)

# ------------------------------------------------------------------

# Shortest Path in an unweighted graph with BFS

from collections import deque  # Required for BFS queue

def shortest_path_bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])  # Store tuples of (current_node, path)
    visited.add(start)
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path  # Return the path when the end node is reached
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None  # Return None if no path is found


# Example usage of shortest path BFS
graph_shortest_path = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}


# path = shortest_path_bfs(graph_shortest_path, 'A', 'E')  # Corrected parameter order
# print("Shortest Path from A to E:", path if path else "No path found")

# ------------------------------------------------------------------

# Dijkstra's Algorithm for Shortest Path in a weighted graph
# Assumptions:
# - Weights on edges are non-negative
# - Edges can be directed or undirected

import heapq  # Required for priority queue in Dijkstra's algorithm

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage of Dijkstra's algorithm
graph_dijkstra = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 3},
    'E': {'B': 5, 'D': 3}
}


# distances = dijkstra(graph_dijkstra, 'A')
# print("Dijkstra's Distances from A:", distances)

# ------------------------------------------------------------------

# Bellman-Ford Algorithm for Shortest Path in a weighted graph with negative weights

def bellman_ford(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances


# Example usage of Bellman-Ford algorithm
graph_bellman_ford = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': -3},  # Negative weight edge
    'E': {'B': 5, 'D': 3}
}


# distances_bellman_ford = bellman_ford(graph_bellman_ford, 'A')
# print("Bellman-Ford Distances from A:", distances_bellman_ford)

# ------------------------------------------------------------------

# Spanning tree: A subgraph that includes all vertices and is a tree (connected and acyclic)

# Minimum Spanning Tree (MST): The spanning tree with the minimum total edge weight
# Minimum Spanning Forest (MSF): A spanning forest that includes all vertices and is a tree for each connected component


# Kruskal's Algorithm for Minimum Spanning Tree (MST)

def kruskal(graph):
    # Convert graph to edge list
    edges = []
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((weight, node, neighbor))

    # Sort edges by weight
    edges.sort()

    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Initialize disjoint set
    for node in graph:
        parent[node] = node
        rank[node] = 0

    mst_edges = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))

    return mst_edges


# Example usage of Kruskal's algorithm
graph_kruskal = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 3},
    'E': {'B': 5, 'D': 3}
}


# mst_edges = kruskal(graph_kruskal)
# print("Kruskal's Minimum Spanning Tree Edges:")
# for u, v, weight in mst_edges:
#     print(f"{u} - {v}: {weight}")
# ------------------------------------------------------------------

# Prim's Algorithm for Minimum Spanning Tree (MST)

def prim(graph, start):
    mst_edges = []
    visited = set([start])
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            for next_neighbor, next_weight in graph[v].items():
                if next_neighbor not in visited:
                    heapq.heappush(edges, (next_weight, v, next_neighbor))

    return mst_edges


# Example usage of Prim's algorithm
graph_prim = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 3},
    'E': {'B': 5, 'D': 3}
}


# mst_edges_prim = prim(graph_prim, 'A')
# print("Prim's Minimum Spanning Tree Edges:")
# for u, v, weight in mst_edges_prim:
#     print(f"{u} - {v}: {weight}")
# ------------------------------------------------------------------

















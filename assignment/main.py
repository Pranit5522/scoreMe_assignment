
### 2. `main.py`


"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes here
    topo_order = topological_sort(graph)
    dist = calculate_longest_path(graph,topo_order)
    return dist

# Helper function to perform topological sort
def topoSort(v, adj, visited, stack):
    visited[v] = True
    for i in adj[v]:
        if not visited[i[0]]:
            topoSort(i[0], adj, visited, stack)

    stack.append(v)


def topological_sort(graph):
    stack = []
    V = len(graph)
    visited = [False] * V
    ans = []
    for i in range(V):
        if not visited[i]:
            topoSort(i, graph, visited, stack)
    while stack:
        ans.append(stack.pop())
    return ans

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    V = len(graph)
    int_min = 0
    weights = [int_min] * V
    for i in topo_order:
        for j in graph[i]:
            weights[j[0]] = max(weights[j[0]],weights[i]+j[1])
    return max(weights)
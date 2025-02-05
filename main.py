
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

# def longest_path(graph: list) -> int:
#     # Your implementation goes here
#     pass

# # Helper function to perform topological sort
# def topological_sort(graph):
#     # Your implementation goes here
#     pass

# # Function to calculate longest path using topological sort
# def calculate_longest_path(graph, topo_order):
#     # Your implementation goes here
#     pass

# def longest_path(graph: list) -> int:
#     def topological_sort(graph):
#         n = len(graph)
#         visited = [False] * n
#         topo_order = []

#         def dfs(v):
#             visited[v] = True
#             for (neighbor, weight) in graph[v]:
#                 if not visited[neighbor]:
#                     dfs(neighbor)
#             topo_order.append(v)
        
#         for i in range(n):
#             if not visited[i]:
#                 dfs(i)
        
#         topo_order.reverse()
#         return topo_order
    
#     def calculate_longest_path(graph, topo_order):
#         n = len(graph)
#         dist = [-float('inf')] * n
#         dist[topo_order[0]] = 0  # start with the first node in topological order
        
#         for u in topo_order:
#             if dist[u] != -float('inf'):
#                 for (v, weight) in graph[u]:
#                     if dist[u] + weight > dist[v]:
#                         dist[v] = dist[u] + weight
        
#         return max(dist)

#     topo_order = topological_sort(graph)
#     return calculate_longest_path(graph, topo_order)

def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        visited = [False] * n
        topo_order = []

        def dfs(v):
            visited[v] = True
            for (neighbor, weight) in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
            topo_order.append(v)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        topo_order.reverse()
        return topo_order
    
    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [-float('inf')] * n

        # We need to consider the longest path starting from every node
        for start in topo_order:
            if dist[start] == -float('inf'):
                dist[start] = 0
            for u in topo_order:
                if dist[u] != -float('inf'):
                    for (v, weight) in graph[u]:
                        if dist[u] + weight > dist[v]:
                            dist[v] = dist[u] + weight
        
        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)




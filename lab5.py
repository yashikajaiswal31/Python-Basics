def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set for the first call

    if start_node not in visited:
        print()
        print("Visiting:", start_node)
        visited.add(start_node)
        print()
        # Recursively visit all unvisited neighbors
        for neighbor in graph[start_node]:
            dfs(graph, neighbor, visited)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Start DFS from node 'A'
dfs(graph, 'A')

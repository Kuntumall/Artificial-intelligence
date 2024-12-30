def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  
    visited.add(node)
    print(node, end=" ")  
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start_node):
    visited = set() 
    stack = [start_node] 
    
    while stack:
        node = stack.pop() 
        if node not in visited:
            visited.add(node)
            print(node, end=" ") 
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print("Recursive DFS:")
dfs_recursive(graph, 0)

print("\nIterative DFS:")
dfs_iterative(graph, 0)

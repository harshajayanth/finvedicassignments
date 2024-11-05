def is_cyclic_util(graph, v, visited, rec_stack):
    visited[v] = True
    rec_stack[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:  # A cycle is detected
            return True

    rec_stack[v] = False
    return False

def is_cyclic(graph):
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            if is_cyclic_util(graph, node, visited, rec_stack):
                return True
    return False

# Example usage for directed graph
graph = {
    0: [1],
    1: [2],
    2: [0],  # This creates a cycle
    3: [4],
    4: []
}

if is_cyclic(graph):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")

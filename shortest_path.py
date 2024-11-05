import heapq

def dijkstra(graph, start):
    # Create a priority queue
    min_heap = []
    # Dictionary to store the shortest path to each node
    shortest_paths = {node: float('infinity') for node in graph}
    shortest_paths[start] = 0
    # Push the start node into the priority queue
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return shortest_paths

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node", start_node)
for node, distance in shortest_paths.items():
    print(f"Distance to {node}: {distance}")

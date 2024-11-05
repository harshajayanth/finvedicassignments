import heapq
from collections import defaultdict

def prims_mst(graph, start_node):
    mst = []
    visited = set()
    min_heap = [(0, start_node, None)]
    
    while min_heap:
        cost, node, prev = heapq.heappop(min_heap)
        
        if node not in visited:
            visited.add(node)
            if prev is not None:
                mst.append((prev, node, cost))
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))
                    
    return mst
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

# Find the MST starting from node 0
mst = prims_mst(graph, 0)
for i in mst:
    print(i[2])
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    # Function to perform the greedy coloring of the graph
    def greedy_coloring(self):
        # Initialize result array to store colors for each vertex
        result = [-1] * self.V
        
        # Assign the first color to the first vertex
        result[0] = 0
        
        # Temporary array to store the availability of colors
        available = [False] * self.V
        
        # Assign colors to remaining V-1 vertices
        for u in range(1, self.V):
            # Process all adjacent vertices and mark their colors as unavailable
            for i in self.graph[u]:
                if result[i] != -1:
                    available[result[i]] = True
            
            # Find the first available color
            color = 0
            while color < self.V and available[color]:
                color += 1
            
            # Assign the found color to the current vertex
            result[u] = color
            
            # Reset the available array for the next iteration
            for i in self.graph[u]:
                if result[i] != -1:
                    available[result[i]] = False
        
        # Print the result
        for u in range(self.V):
            print(f"Vertex {u} ---> Color {result[u]}")

# Driver code
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    
    print("Graph Coloring of the given graph:")
    g.greedy_coloring()

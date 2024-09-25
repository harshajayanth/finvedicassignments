from collections import deque

def is_valid_move(maze, visited, row, col):
    rows = len(maze)
    cols = len(maze[0])
    return (0 <= row < rows) and (0 <= col < cols) and maze[row][col] == 0 and not visited[row][col]


def bfs_maze(maze, start, end):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    

    queue = deque([(start[0], start[1], [])])
    

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    
    while queue:
        row, col, path = queue.popleft()
        path = path + [(row, col)] 
        

        if (row, col) == end:
            return path
        
    
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            
            if is_valid_move(maze, visited, new_row, new_col):
                queue.append((new_row, new_col, path))
                visited[new_row][new_col] = True
                
    return []


def main():

    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]


    start = (0, 0)  
    finish = (4, 4) 
    

    shortest_path = bfs_maze(maze, start, finish)
    
    if shortest_path:
        print("Shortest path found:")
        for step in shortest_path:
            print(step)
    else:
        print("No path found from start to finish.")


if __name__ == "__main__":
    main()

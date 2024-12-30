import heapq

class Node:
    def __init__(self, position, g, h):
        self.position = position  
        self.g = g  
        self.h = h  
        self.f = g + h  
        self.parent = None 

    def __lt__(self, other):
        return self.f < other.f

def astar(start, goal, grid):
    open_list = []  
    closed_list = set()  
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            return reconstruct_path(current_node)
        
        closed_list.add(current_node.position)
        
        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor in closed_list:
                continue  
            g_cost = current_node.g + 1  
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g_cost, h_cost)
            neighbor_node.parent = current_node
            
            if not any(open_node.position == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  
def heuristic(node, goal):
    
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_neighbors(position, grid):
    x, y = position
    neighbors = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  
goal = (4, 4)  

path = astar(start, goal, grid)

if path:
    print("Path found:", path)
else:
    print("No path found")
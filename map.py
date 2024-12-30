class MapColoringCSP:
    def __init__(self, map_structure, colors):
        self.map_structure = map_structure  
        self.colors = colors 
        self.assignment = {}  
    
    def is_safe(self, region, color):
        for neighbor in self.map_structure[region]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def backtrack(self):
        if len(self.assignment) == len(self.map_structure):
            return self.assignment  
        
        unassigned_region = self.select_unassigned_region()
        
        for color in self.colors:
            if self.is_safe(unassigned_region, color):
                self.assignment[unassigned_region] = color
               
                result = self.backtrack()
                if result:
                    return result
                
                del self.assignment[unassigned_region]
        
        return None 

    def select_unassigned_region(self):
        for region in self.map_structure:
            if region not in self.assignment:
                return region
        return None

    def solve(self):
        return self.backtrack()

map_structure = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

colors = ['Red', 'Green', 'Blue']

map_coloring = MapColoringCSP(map_structure, colors)

solution = map_coloring.solve()

if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"Region {region} is colored {color}")
else:
    print("No solution exists.")

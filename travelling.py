import itertools
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  
    return total_distance

def tsp_bruteforce(distance_matrix):
    
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    all_routes = itertools.permutations(cities)

    min_distance = float('inf')
    best_route = None

    for route in all_routes:
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

distance_matrix = [
    [0, 10, 15, 20],  
    [10, 0, 35, 25], 
    [15, 35, 0, 30],  
    [20, 25, 30, 0]  
]

best_route, min_distance = tsp_bruteforce(distance_matrix)

print(f"The best route is: {best_route}")
print(f"The minimum distance is: {min_distance}")

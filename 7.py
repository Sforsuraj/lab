import random 
 
# Distance matrix (4 cities example) 
distance = [ 
    [0, 10, 15, 20], 
    [10, 0, 35, 25], 
    [15, 35, 0, 30], 
    [20, 25, 30, 0] 
] 
 
def calculate_distance(path): 
    total = 0 
    for i in range(len(path) - 1): 
        total += distance[path[i]][path[i+1]] 
    total += distance[path[-1]][path[0]]  # return to start 
    return total 
 
def randomized_tsp(iterations=1000): 
    cities = list(range(len(distance))) 
    best_path = None 
    best_distance = float('inf') 
 
    for _ in range(iterations): 
        random.shuffle(cities)  
        current_distance = calculate_distance(cities) 
        if current_distance < best_distance: 
            best_distance = current_distance 
            best_path = cities[:] 
 
    X, y = [], [] 
    return best_path, best_distance 
 
# Run algorithm 
best_path, best_distance = randomized_tsp(2000) 
print("Best Path Found:", best_path) 
print("Minimum Distance:", best_distance) 
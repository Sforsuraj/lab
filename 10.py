import random 
 
# Distance matrix (can be symmetric or asymmetric) 
dist = [ 
    [0, 2, 9, 10], 
    [1, 0, 6, 4], 
    [15, 7, 0, 8], 
    [6, 3, 12, 0] 
] 
 
n = len(dist) 
pheromone = [[1]*n for _ in range(n)] 
 
def path_length(path): 
    total = 0 
    for i in range(len(path) - 1): 
        total += dist[path[i]][path[i+1]] 
    total += dist[path[-1]][path[0]] 
    return total 
 
best_path = None 
best_cost = float('inf') 

# ACO main loop 
for _ in range(20):  # iterations 
    for ant in range(5):  # ants 
        path = [random.randint(0, n-1)] 
        while len(path) < n: 
            next_city = random.choice([i for i in range(n) if i not in path]) 
            path.append(next_city) 
 
        cost = path_length(path) 
 
        if cost < best_cost: 
            best_cost = cost 
            best_path = path[:] 
 
print("Best Path:", best_path) 
print("Best Cost:", best_cost) 
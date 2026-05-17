#============ Code 1 Shortest Path (Unconstrained Multi-Stage Optimization) ===============#
def shortest_path_dp(graph, start): 
    # graph: {node: [(neighbor, weight)]} 
    dist = {node: float('inf') for node in graph} 
    dist[start] = 0 
    for node in graph: 
        for neighbor, weight in graph[node]: 
            if dist[node] + weight < dist[neighbor]: 
                dist[neighbor] = dist[node] + weight 
    return dist 
graph = { 
    'A': [('B', 1), ('C', 4)], 
    'B': [('C', 2), ('D', 6)], 
    'C': [('D', 3)], 
    'D': [] 
} 
print(shortest_path_dp(graph, 'A'))

#==================== Code 2 ====================#
def unconstrained_quadratic(): 
    min_value = float('inf') 
    best_solution = None 
    for x1 in range(4): 
        for x2 in range(4): 
            value = x1**2 + x2**2 
            if value < min_value: 
                min_value = value 
                best_solution = (x1, x2) 
    return best_solution, min_value 
 
print(unconstrained_quadratic())

 
#============================ Code 3 (Constrained Optimization ) ============================#
def resource_allocation(total_resource): 
    best_value = 0 
    best_allocation = None 
    for x1 in range(total_resource + 1): 
        for x2 in range(total_resource + 1 - x1): 
            value = 3*x1 + 5*x2  # objective function 
            if value > best_value: 
                best_value = value 
                best_allocation = (x1, x2) 
    return best_allocation, best_value 
 
print(resource_allocation(5)) 
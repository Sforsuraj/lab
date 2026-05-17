#====== 3A ========#
from scipy.optimize import linprog 
c = [-40, -30] 
A = [ 
    [2, 1], 
    [1, 1] 
] 
b = [100, 80] 
x_bounds = (0, None) 
y_bounds = (0, None) 
result = linprog( c, A_ub=A, b_ub=b,  bounds=[x_bounds, y_bounds],  method='highs') 
print("Optimal value of x (Product A):", result.x[0]) 
print("Optimal value of y (Product B):", result.x[1]) 
print("Maximum Profit:", -result.fun)


#====== 3B ========#
from scipy.optimize import linprog 
 
# Minimize cost 
c = [10, 8] 
 
# Constraints (convert >= to <= by multiplying -1) 
A = [ 
    [-3, -2],  # Protein 
    [-200, -150]  # Calories 
] 
b = [-12, -800] 
bounds = [(0, None), (0, None)] 
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs') 
 
print("Food A units:", result.x[0]) 
print("Food B units:", result.x[1]) 
print("Minimum Cost:", result.fun)


#====== 3C ========#
from scipy.optimize import linprog 
c = [4, 6, 5, 3] 
A = [ 
    [1, 1, 0, 0], 
    [0, 0, 1, 1], 
    [1, 0, 1, 0], 
    [0, 1, 0, 1] 
] 
b = [40, 60, 50, 50] 
bounds = [(0, None)] * 4 
result = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method='highs') 
print("Shipment plan:", result.x) 
print("Minimum Transportation Cost:", result.fun)
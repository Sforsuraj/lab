#======= CODE 1=======# 
import numpy as np 
Q = np.array([ 
    [2, 0], 
    [0, 2] 
]) 
 
C = np.array([-4, -6]) 
x = np.array([1, 2]) 
 
f = 0.5 * x.T @ Q @ x + C.T @ x 
 
grad = Q @ x + C 
 
print("Decision variable x:", x) 
print("Objective function value:", f) 
print("Gradient:", grad) 
 
#======== CODE 2 ========# 
import numpy as np 
 
X = np.array([ 
    [1, 1], 
    [1, 2], 
    [1, 3] 
]) 
 
y = np.array([2, 3, 4]) 
  
w = np.linalg.inv(X.T @ X) @ X.T @ y 

print("Optimal weight vector:", w)
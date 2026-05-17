import numpy as np 

def min_cost_path(grid): 
    rows, cols = grid.shape 
    
    dp = np.zeros((rows, cols), dtype=int) 
    
    dp[0][0] = grid[0][0] 
    
    # Fill first column
    for i in range(1, rows): 
        dp[i][0] = dp[i-1][0] + grid[i][0] 
    
    # Fill first row
    for j in range(1, cols): 
        dp[0][j] = dp[0][j-1] + grid[0][j] 
    
    # Fill the rest of the DP table
    for i in range(1, rows): 
        for j in range(1, cols): 
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) 
    
    return dp[rows-1][cols-1] 

grid = np.array([ 
    [1, 3, 1], 
    [1, 5, 1], 
    [4, 2, 1] 
]) 

result = min_cost_path(grid) 
print("Minimum Cost:", result)
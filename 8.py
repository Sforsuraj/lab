N = 4 
board = [[0]*N for _ in range(N)] 
 
def is_safe(board, row, col): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False 
 
    i, j = row, col 
 
 
 
 
    while i >= 0 and j >= 0: 
        if board[i][j] == 1: 
            return False 
        i -= 1 
        j -= 1 
    i, j = row, col 
    while i < N and j >= 0: 
        if board[i][j] == 1: 
            return False 
        i += 1 
        j -= 1 
    return True 
 
def solve_nqueens(board, col): 
    if col >= N: 
        return True 
 
    for i in range(N): 
        if is_safe(board, i, col): 
            board[i][col] = 1 
            if solve_nqueens(board, col + 1): 
                return True 
            board[i][col] = 0 
    return False 
 
if solve_nqueens(board, 0): 
    for row in board: 
        print(row) 
else: 
    print("No solution found")
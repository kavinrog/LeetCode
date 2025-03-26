def solve(board):
    ROWS = len(board)
    COLS = len(board[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]  # Down, Up, Right, Left
    
    # DFS to mark 'O's connected to border as 'T' (temporary safe)
    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c]!= "O":
            return 
        board[r][c] = "T"
        for dr, dc in directions:
            dfs(r+dr, c+dc)
            
    # Start DFS from 'O's on the borders
    for r in range(ROWS):
        if board[r][0] == "O":
            dfs(r, 0)
        if board[r][COLS-1] == "O":
            dfs(r,COLS-1)
    
    for c in range(COLS):
        if board[0][c] == "O":
            dfs(0, c)
        if board[ROWS-1][c] == "O":
            dfs(ROWS-1,c)
            
    # Flip all remaining 'O's to 'X' (captured),
    # and convert 'T' (safe) back to 'O'        
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"        
# Code Testing 
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

solve(board)

for row in board:
    print(row)
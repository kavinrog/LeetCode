def solve(board):
    ROWS = len(board)
    COLS = len(board[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    
    def dfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c]!= "O":
            return 
        board[r][c] = "T"
        for dr, dc in directions:
            dfs(r+dr, c+dc)
        
    for r in range(ROWS):
        if board[r][0] == 0:
            dfs(r, 0)
        if board[r][COLS-1] == 0:
            dfs(r,COLS-1)
    
    for c in range(COLS):
        if board[0][c] == 0:
            dfs(0, c)
        if board[ROWS-1][c] == 0:
            dfs(ROWS-1,c)
            
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"        
    
def pacificAtlantic(heights):
    if not heights and not heights[0]:
        return []
    ROWS, COLS = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def dfs(r, c ,visited, prevHeight):
        if (r < 0 or r >= ROWS or 
            c < 0 or c >= COLS or 
            (r, c) in visited or
            heights[r][c]<prevHeight):
            return
        visited.add((r,c))
        for dr, dc in directions:
            dfs(dr+r, dc+c, visited, heights[r][c])
    
    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])
        dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
    
    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, COLS-1, atlantic, heights[r][COLS-1])
    return list(pacific & atlantic)
        
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

result = pacificAtlantic(heights)
print("Cells that can flow to both Pacific and Atlantic:", result)
def countComponents(n, edges):
    adjacent_list = [[] for i in range(edges)]
    for u, v in edges:
        adjacent_list[u].append(v)
        adjacent_list[v].append(u)
    
    visited = [False] * n
    def dfs(node):
        for neighbor in adjacent_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)
            
        components = 0 
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                components+=1
        return components        
                 
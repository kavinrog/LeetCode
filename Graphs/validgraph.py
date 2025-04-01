def validgraphtree(edges, n):
    if len(edges) > n-1:
        return False
    
    adjacent_list = [[] for _ in range(n)]
    
    for node1, node2 in edges:
        adjacent_list[node1].append(node2)
        adjacent_list[node2].append(node1)
        
    visited = set()
    
    def dfs(current_node, parent_node):
        if current_node in visited:
            return False
        visited.add(current_node)
        for neighbour in adjacent_list[current_node]:
            if neighbour == parent_node:
                continue
            if not dfs(neighbour):
                return False
        return True 
    return dfs(0, -1) and len(visited) == n
    
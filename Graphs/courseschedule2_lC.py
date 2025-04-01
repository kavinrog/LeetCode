def findOrder(numCourses, prerequistes):
    if len(numCourses) < 0:
        return -1
    graph = [[] for _ in range(numCourses)]
    
    for course, preq in prerequistes:
        graph[course].append(preq)
    
    has_cycle = False
    res = []
        
    visited = [0] * numCourses
    
    def dfs(courses):
        nonlocal has_cycle
        if visited[courses] == 1:
            has_cycle = True
            return
        if visited[courses] == 2:
            return 
        visited[course] = 1
        for neighbour in graph[courses]:
            dfs(neighbour)
        visited[courses] = 2
        res.append(courses)
    
    for i in range(numCourses):
        if visited[i] == 0:
            dfs(i)
            if has_cycle:
                return []
    return res[::-1]
            
        
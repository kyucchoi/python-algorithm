# BFS 방법
from collections import deque, defaultdict

def solution(n, wires):
    def bfs(start, graph):
        visited = set()
        queue = deque([start])
        visited.add(start)
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return count
    
    min_diff = n
    
    for i in range(len(wires)):
        graph = defaultdict(list)
        
        for j, (v1, v2) in enumerate(wires):
            if i != j:
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        one_side = bfs(1, graph)
        other_side = n - one_side
        
        diff = abs(one_side - other_side)
        min_diff = min(min_diff, diff)
    
    return min_diff

# DFS 방법
from collections import defaultdict

def solution(n, wires):
    def dfs(node, graph, visited):
        visited.add(node)
        count = 1
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, graph, visited)
        
        return count
    
    min_diff = n
    
    for i in range(len(wires)):
        graph = defaultdict(list)
        
        for j, (v1, v2) in enumerate(wires):
            if i != j:
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        visited = set()
        one_side = dfs(1, graph, visited)
        other_side = n - one_side
        
        diff = abs(one_side - other_side)
        min_diff = min(min_diff, diff)
    
    return min_diff
# DFS 방법
def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
    
    return network_count

# BFS 방법
from collections import deque

def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_count += 1
    
    return network_count
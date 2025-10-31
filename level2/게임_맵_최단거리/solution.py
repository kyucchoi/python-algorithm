# 방법 1
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # 예외 처리
    if maps[0][0] == 0 or maps[n - 1][m - 1] == 0:
        return -1
    
    # BFS 초기화
    queue = deque([(0, 0, 1)])  # (행, 열, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 4방향 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col, distance = queue.popleft()
        
        # 도착점 확인
        if (row, col) == (n - 1, m - 1):
            return distance
        
        # 4방향 탐색
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 
                0 <= new_col < m and 
                maps[new_row][new_col] == 1 and 
                not visited[new_row][new_col]):
                
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))
    
    return -1  # 도달 불가능

# 방법 2
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    
    return -1
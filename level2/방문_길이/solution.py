def solution(dirs):
    x, y = 0, 0
    
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    visited = set()
    
    for direction in dirs:
        dx, dy = move[direction]
        nx, ny = x + dx, y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path1 = ((x, y), (nx, ny))
            path2 = ((nx, ny), (x, y))
            
            if path1 not in visited:
                visited.add(path1)
                visited.add(path2)
            
            x, y = nx, ny
    
    return len(visited) // 2
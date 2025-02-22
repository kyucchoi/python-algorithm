def solution(n):
    # n x n 크기의 0으로 채워진 배열 생성
    result = [[0] * n for _ in range(n)]
    
    # 방향 정의 (우->하->좌->상)
    dx = [0, 1, 0, -1]  # 행 이동
    dy = [1, 0, -1, 0]  # 열 이동
    
    x, y = 0, 0  # 현재 위치
    dir = 0      # 현재 방향
    
    # 1부터 n*n까지 숫자 채우기
    for i in range(1, n * n + 1):
        result[x][y] = i
        
        # 다음 위치 계산
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        # 방향 전환이 필요한 경우
        # (배열을 벗어나거나 이미 숫자가 채워진 경우)
        if (nx < 0 or nx >= n or ny < 0 or ny >= n or result[nx][ny] != 0):
            dir = (dir + 1) % 4  # 다음 방향으로 전환
            
            nx = x + dx[dir]
            ny = y + dy[dir]
            
        x, y = nx, ny
        
    return result
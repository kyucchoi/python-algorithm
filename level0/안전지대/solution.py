def solution(board):
    n = len(board)
    # 위험지역을 표시할 배열 생성 (0으로 초기화)
    danger = [[0] * n for _ in range(n)]
    # 8방향 좌표 (상하좌우 + 4개 대각선)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # # 지뢰가 있는 위치를 찾아서 위험지역 표시
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 경우
                # 지뢰 위치 자체도 위험지역
                danger[i][j] = 1

                # 주변 8칸도 위험지역으로 표시
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1
    
    # 안전한 지역(0인 칸) 개수 세기
    safe_count = 0

    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1

    return safe_count
def solution(board, k):
    total = 0
    # 행의 개수
    rows = len(board)
    # 열의 개수
    cols = len(board[0])
    
    # 모든 위치 (i,j)에 대해 검사
    for i in range(rows):
        for j in range(cols):
            # i + j가 k 이하인 경우만 더함
            if i + j <= k:
                total += board[i][j]
    
    return total
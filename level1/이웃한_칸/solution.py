def solution(board, h, w):
    # 보드의 크기
    n = len(board)
    
    # 같은 색상의 인접 칸 개수를 저장할 변수
    count = 0
    
    # 상, 우, 하, 좌 방향의, h와 w의 변화량
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # 현재 칸의 색상
    current_color = board[h][w]
    
    # 인접한 네 방향 확인
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # 보드 범위 내에 있는지 확인
        if 0 <= h_check < n and 0 <= w_check < n:
            # 색상이 같은지 확인
            if board[h_check][w_check] == current_color:
                count += 1
    
    return count
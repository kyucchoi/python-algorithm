def solution(keyinput, board):
    # 시작 위치
    x, y = 0, 0
    
    # 맵의 경계 계산
    max_x = board[0] // 2  # 오른쪽 최대 이동 거리
    max_y = board[1] // 2  # 위쪽 최대 이동 거리
    min_x = -max_x         # 왼쪽 최대 이동 거리
    min_y = -max_y         # 아래쪽 최대 이동 거리
    
    # 각 키 입력 처리
    for key in keyinput:
        if key == 'up':
            y = min(y + 1, max_y)  # 위로 이동, 경계 체크
        elif key == 'down':
            y = max(y - 1, min_y)  # 아래로 이동, 경계 체크
        elif key == 'left':
            x = max(x - 1, min_x)  # 왼쪽으로 이동, 경계 체크
        elif key == 'right':
            x = min(x + 1, max_x)  # 오른쪽으로 이동, 경계 체크
    
    return [x, y]
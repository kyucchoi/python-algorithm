def solution(park, routes):
    # 1. 공원의 크기 계산 및 시작 위치 찾기
    # - h: 공원의 세로 길이 (행의 개수)
    # - w: 공원의 가로 길이 (열의 개수)
    h = len(park)
    w = len(park[0])
    
    # 시작 위치 찾기 (이중 반복문으로 'S'를 찾음)
    x, y = 0, 0  # 현재 위치 변수 초기화 (시작 위치로 설정됨)

    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j  # 시작 위치 저장
                break
    
    # 방향별 이동 값 정의
    # - key: 방향 문자 ('N', 'S', 'W', 'E')
    # - value: (dx, dy) 형태의 좌표 변화량
    directions = {
        'N': (-1, 0),  # 북쪽: 행 감소 (위로)
        'S': (1, 0),   # 남쪽: 행 증가 (아래로)
        'W': (0, -1),  # 서쪽: 열 감소 (왼쪽으로)
        'E': (0, 1)    # 동쪽: 열 증가 (오른쪽으로)
    }
    
    # 2. 각 명령(route) 처리하기
    for route in routes:
        # 방향과 거리 분리
        direction, distance = route.split()  # "E 2" -> direction="E", distance="2"

        distance = int(distance)  # 문자열을 정수로 변환
        dx, dy = directions[direction] # 방향에 따른 좌표 변화량 계산
        
        # 이동 가능한지 확인
        can_move = True
        
        # 이동 경로의 모든 칸 확인
        for i in range(1, distance + 1):
            nx = x + dx * i  # i칸 이동했을 때의 행 위치
            ny = y + dy * i  # i칸 이동했을 때의 열 위치
            
            # a. 공원을 벗어나는지 확인
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                can_move = False
                break
            
            # b. 장애물을 만나는지 확인
            if park[nx][ny] == 'X':
                can_move = False
                break
        
        # 이동 가능하면 위치 업데이트
        if can_move:
            x = x + dx * distance
            y = y + dy * distance
    
    # 3. 최종 위치 반환
    return [x, y]
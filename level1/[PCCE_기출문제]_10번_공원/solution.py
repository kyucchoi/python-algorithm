def solution(mats, park):
    # 공원의 크기 확인
    h = len(park)
    w = len(park[0])
    
    # 가용한 돗자리 크기를 내림차순으로 정렬
    mats.sort(reverse=True)
    
    # 각 돗자리 크기에 대해 확인
    for mat_size in mats:
        # 공원 전체를 순회하면서 각 위치에서 돗자리를 놓을 수 있는지 확인
        for i in range(h - mat_size + 1):
            for j in range(w - mat_size + 1):
                # 현재 위치(i, j)에서 mat_size 크기의 정사각형이 모두 비어있는지 확인
                is_available = True
                
                # 정사각형 내의 모든 위치 확인
                for r in range(i, i + mat_size):
                    for c in range(j, j + mat_size):
                        # 공원 범위를 벗어나거나 이미 사람이 있는 경우
                        if r >= h or c >= w or park[r][c] != '-1':
                            is_available = False
                            break

                    if not is_available:
                        break
                
                # 돗자리를 놓을 수 있는 경우
                if is_available:
                    return mat_size
    
    # 어떤 돗자리도 놓을 수 없는 경우
    return -1
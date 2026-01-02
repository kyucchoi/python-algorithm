def solution(routes):
    # 1. 진출 지점 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    camera_position = -30001
    
    # 2. 각 차량 확인
    for start, end in routes:
        if start > camera_position:
            camera_count += 1
            camera_position = end
    
    return camera_count
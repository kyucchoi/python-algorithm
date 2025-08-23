# 방법 1
def solution(dots):
    # 두 점을 이은 직선의 기울기를 구하는 함수
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    # 4개 점을 2개씩 묶는 3가지 경우
    # 경우 1: (점0, 점1)과 (점2, 점3)
    slope1 = get_slope(dots[0], dots[1])
    slope2 = get_slope(dots[2], dots[3])

    if slope1 == slope2:
        return 1
    
    # 경우 2: (점0, 점2)와 (점1, 점3)
    slope1 = get_slope(dots[0], dots[2])
    slope2 = get_slope(dots[1], dots[3])

    if slope1 == slope2:
        return 1
    
    # 경우 3: (점0, 점3)과 (점1, 점2)
    slope1 = get_slope(dots[0], dots[3])
    slope2 = get_slope(dots[1], dots[2])

    if slope1 == slope2:
        return 1
    
    return 0

# 방법 2
def solution(dots):
    # 교차곱셈으로 기울기 비교 (부동소수점 오차 방지)
    def is_parallel(p1, p2, p3, p4):
        return (p2[1] - p1[1]) / (p2[0] - p1[0]) == (p4[1] - p3[1]) / (p4[0] - p3[0])
    
    # 3가지 경우 확인
    cases = [
        (dots[0], dots[1], dots[2], dots[3]),  # (0,1)과 (2,3)
        (dots[0], dots[2], dots[1], dots[3]),  # (0,2)와 (1,3)
        (dots[0], dots[3], dots[1], dots[2])   # (0,3)과 (1,2)
    ]
    
    for p1, p2, p3, p4 in cases:
        if is_parallel(p1, p2, p3, p4):
            return 1
    
    return 0
def solution(topping):
    n = len(topping)
    
    if n <= 1:
        return 0
    
    # 왼쪽 종류 수 계산
    left_types = [0] * n
    left_set = set()

    for i in range(n):
        left_set.add(topping[i])
        left_types[i] = len(left_set)
    
    # 오른쪽 종류 수 계산
    right_types = [0] * n
    right_set = set()

    for i in range(n - 1, -1, -1):
        right_set.add(topping[i])
        right_types[i] = len(right_set)
    
    # 공평한 지점 세기
    count = 0

    for i in range(n - 1):
        if left_types[i] == right_types[i + 1]:
            count += 1
    
    return count
# 방법 1
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

# 방법 2
def solution(topping):
    answer = 0
    
    # 왼쪽 조각의 토핑 종류를 저장할 set
    left_set = set()
    # 오른쪽 조각의 토핑 개수를 저장할 dict
    right_dict = {}
    
    # 처음에 모든 토핑을 오른쪽에 배치
    for t in topping:
        right_dict[t] = right_dict.get(t, 0) + 1
    
    for i in range(len(topping) - 1):
        current = topping[i]
        
        left_set.add(current)
        
        right_dict[current] -= 1

        if right_dict[current] == 0:
            del right_dict[current]
        
        if len(left_set) == len(right_dict):
            answer += 1
    
    return answer
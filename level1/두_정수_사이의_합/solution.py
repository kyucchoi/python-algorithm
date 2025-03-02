def solution(a, b):
    # a와 b의 대소관계에 따라 시작점과 끝점을 정합니다
    start = min(a, b)
    end = max(a, b)
    
    # start부터 end까지의 모든 정수를 더합니다
    total = 0
    
    for i in range(start, end + 1):
        total += i
        
    return total
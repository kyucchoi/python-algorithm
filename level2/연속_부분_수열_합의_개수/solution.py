# 방법 1
def solution(elements):
    n = len(elements)
    # 원형을 위해 배열 확장
    extended = elements * 2
    
    sums = set()
    
    # 각 시작점에서 길이별로 누적합 계산
    for start in range(n):
        current_sum = 0
        
        for length in range(1, n + 1):
            current_sum += extended[start + length - 1]
            sums.add(current_sum)
    
    return len(sums)

# 방법 2
def solution(elements):
    n = len(elements)
    sums = set()
    
    for length in range(1, n + 1):
        for start in range(n):
            total = 0

            for i in range(length):
                total += elements[(start + i) % n]
                
            sums.add(total)
    
    return len(sums)
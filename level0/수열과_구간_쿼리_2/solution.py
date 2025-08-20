def solution(arr, queries):
    result = []  # 결과를 저장할 리스트
    
    for s, e, k in queries:
        min_value = float('inf')  # 최솟값을 찾기 위한 초기값
        
        # s부터 e까지 범위 확인
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < min_value:
                min_value = arr[i]
        
        # k보다 큰 값을 찾지 못한 경우
        if min_value == float('inf'):
            result.append(-1)
        else:
            result.append(min_value)
            
    return result
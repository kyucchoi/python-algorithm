def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        min_value = float('inf')
        
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < min_value:
                min_value = arr[i]
        
        # k보다 큰 값을 찾지 못한 경우
        if min_value == float('inf'):
            result.append(-1)
        else:
            result.append(min_value)
            
    return result
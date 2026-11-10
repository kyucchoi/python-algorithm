def solution(arr, divisor):
    result = []
    
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    
    if not result:
        return [-1]
    
    return sorted(result)
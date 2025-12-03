def solution(arr):
    result = []
    
    for num in arr:
        # 원소를 원소만큼 반복해서 추가
        result.extend([num] * num)
    
    return result
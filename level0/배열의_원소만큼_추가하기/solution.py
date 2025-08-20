def solution(arr):
    result = []
    
    # arr의 각 원소에 대해
    for num in arr:
        # 원소를 원소만큼 반복해서 추가
        result.extend([num] * num)
    
    return result
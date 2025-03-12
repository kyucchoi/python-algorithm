def solution(arr):
    # 배열의 길이가 1인 경우, [-1] 반환
    if len(arr) == 1:
        return [-1]
    
    # 배열에서 가장 작은 수 찾기
    min_value = min(arr)
    
    # 가장 작은 수를 제거한 새 배열 생성
    # result = [num for num in arr if num != min_value]
    result = []

    for num in arr:
        if num != min_value:
            result.append(min_value)
    
    return result
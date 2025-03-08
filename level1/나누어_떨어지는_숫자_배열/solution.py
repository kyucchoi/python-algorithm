def solution(arr, divisor):
    # 나누어 떨어지는 값을 저장할 리스트
    result = []
    
    # 배열의 각 요소를 검사
    for num in arr:
        if num % divisor == 0:  # divisor로 나누어 떨어지는지 확인
            result.append(num)
    
    # 나누어 떨어지는 값이 없는 경우
    if not result:
        return [-1]
    
    # 오름차순 정렬하여 반환
    return sorted(result)
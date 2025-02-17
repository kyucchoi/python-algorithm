def solution(arr, k):
    # 중복 제거하면서 순서 유지
    result = []
    seen = set()  # 이미 나온 숫자를 기록할 집합
    
    # arr 순회하면서 중복되지 않는 숫자 찾기
    for num in arr:
        if num not in seen and len(result) < k:
            result.append(num)
            seen.add(num)
    
    # k개가 되지 않으면 -1로 채우기
    while len(result) < k:
        result.append(-1)
    
    return result
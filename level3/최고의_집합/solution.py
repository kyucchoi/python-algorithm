def solution(n, s):
    # 1. 불가능한 경우
    if s < n:
        return [-1]
    
    # 2. 기본값과 나머지 계산
    base = s // n
    remainder = s % n
    
    # 3. 결과 배열 생성
    result = [base] * n
    
    # 4. 나머지를 뒤에서부터 분배
    for i in range(remainder):
        result[n - 1 - i] += 1
    
    return result
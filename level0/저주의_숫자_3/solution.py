def solution(n):
    count = 0  # 3x 마을에서 사용 가능한 숫자의 개수
    number = 0  # 현재 확인 중인 숫자
    
    while count < n:
        number += 1
        
        # 3의 배수이거나 숫자에 3이 포함되어 있으면 건너뛰기
        if number % 3 == 0 or '3' in str(number):
            continue
        
        # 조건을 만족하는 숫자이면 카운트 증가
        count += 1
    
    return number
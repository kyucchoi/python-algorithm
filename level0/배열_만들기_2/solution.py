def solution(l, r):
    answer = []
    
    # l부터 r까지의 숫자 확인
    for num in range(l, r + 1):
        # 숫자를 문자열로 변환하여 검사
        if all(digit in ['0', '5'] for digit in str(num)):
            answer.append(num)
    
    # 조건을 만족하는 숫자가 없으면 [-1] 반환
    return answer if answer else [-1]
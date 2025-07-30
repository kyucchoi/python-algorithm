def solution(my_string):
    # 공백으로 분리하여 토큰 리스트 생성
    tokens = my_string.split()
    
    # 첫 번째 숫자로 결과 초기화
    result = int(tokens[0])
    
    # 연산자와 숫자를 순서대로 처리
    for i in range(1, len(tokens), 2):
        operator = tokens[i]      # 연산자
        number = int(tokens[i + 1]) # 다음 숫자
        
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
    
    return result
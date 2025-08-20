def solution(binomial):
    # 공백으로 분리하여 a, op, b 추출
    a, op, b = binomial.split()
    
    # 문자열을 정수로 변환
    a = int(a)
    b = int(b)
    
    # 연산자에 따라 계산
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b
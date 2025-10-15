def solution(binomial):
    # 공백으로 분리하여 a, op, b 추출
    a, op, b = binomial.split()
    
    a = int(a)
    b = int(b)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
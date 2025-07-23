def solution(n):
    i = 1
    factorial = 1
    
    # 팩토리얼이 n을 넘지 않는 동안 계속 증가
    while factorial * (i + 1) <= n:
        i += 1
        factorial *= i
    
    return i
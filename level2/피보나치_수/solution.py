def solution(n):
    # 피보나치 수열의 처음 두 숫자
    a, b = 0, 1
    
    # n번째 피보나치 수를 계산
    for i in range(2, n + 1):
        a, b = b, (a + b) % 1234567
        
    return b
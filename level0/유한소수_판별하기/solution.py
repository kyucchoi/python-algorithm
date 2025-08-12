def solution(a, b):
    import math
    
    # 1단계: 기약분수로 만들기 (최대공약수로 약분)
    gcd = math.gcd(a, b)
    b = b // gcd  # 분모만 확인하면 됨 (분자는 유한소수 판별에 영향 없음)
    
    # 2단계: 분모에서 2와 5의 인수를 모두 제거
    while b % 2 == 0:
        b //= 2
    
    while b % 5 == 0:
        b //= 5
    
    # 3단계: 남은 분모가 1이면 유한소수, 아니면 무한소수
    return 1 if b == 1 else 2
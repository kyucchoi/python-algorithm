def solution(a, b, n):
    # 받은 총 콜라 수
    total_cola = 0
    
    # 가지고 있는 빈 병이 a개 이상인 동안 반복
    while n >= a:
        # 교환으로 받는 콜라 수
        received = (n // a) * b
        
        # 총 콜라 수에 더함
        total_cola += received
        
        # 남은 빈 병 계산: 원래 있던 빈 병 - 교환한 빈 병 + 새로 받은 콜라
        n = n - (n // a) * a + received
    
    return total_cola
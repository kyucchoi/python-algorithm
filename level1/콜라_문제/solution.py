def solution(a, b, n):
    total_cola = 0
    
    while n >= a:
        received = (n // a) * b
        
        total_cola += received
        
        # 남은 빈 병 계산: 원래 있던 빈 병 - 교환한 빈 병 + 새로 받은 콜라
        n = n - (n // a) * a + received
    
    return total_cola
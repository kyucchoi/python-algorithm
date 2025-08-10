def solution(chicken):
    coupons = chicken  # 처음에 시킨 치킨 수만큼 쿠폰 보유
    service_chicken = 0  # 받은 서비스 치킨 총 개수
    
    # 쿠폰이 10장 이상 있는 동안 반복
    while coupons >= 10:
        # 쿠폰 10장으로 서비스 치킨 몇 마리 받을 수 있는지
        new_service = coupons // 10
        service_chicken += new_service
        
        # 남은 쿠폰 계산
        remaining_coupons = coupons % 10
        
        # 새로 받은 서비스 치킨에서 나온 쿠폰 추가
        coupons = remaining_coupons + new_service
    
    return service_chicken
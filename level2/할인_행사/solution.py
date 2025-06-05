def solution(want, number, discount):
    # 1단계: 원하는 제품과 수량을 딕셔너리로 변환
    want_count = {}
    
    for i in range(len(want)):
        want_count[want[i]] = number[i]
    
    answer = 0
    
    # 2단계: 가능한 모든 시작일에 대해 확인
    # 10일간 확인해야 하므로, 마지막 가능한 시작일은 len(discount) - 10
    for start_day in range(len(discount) - 9):
        # 3단계: 현재 10일 구간의 할인 제품 개수 세기
        discount_count = {}
        
        # start_day부터 10일간의 할인 제품들
        for day in range(start_day, start_day + 10):
            product = discount[day]
            discount_count[product] = discount_count.get(product, 0) + 1
        
        # 4단계: 원하는 제품 구성과 일치하는지 확인
        if want_count == discount_count:
            answer += 1
    
    return answer
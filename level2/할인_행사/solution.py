# 방법 1
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

# 방법 2
def solution_optimized(want, number, discount):
    # 원하는 제품과 수량을 딕셔너리로 변환
    want_count = {}

    for i in range(len(want)):
        want_count[want[i]] = number[i]
    
    answer = 0
    
    # 첫 번째 10일 구간의 제품 개수 세기
    if len(discount) < 10:
        return 0
    
    discount_count = {}
    
    for i in range(10):
        product = discount[i]
        discount_count[product] = discount_count.get(product, 0) + 1
    
    # 첫 번째 구간 확인
    if want_count == discount_count:
        answer += 1
    
    # 슬라이딩 윈도우로 나머지 구간들 확인
    for start_day in range(1, len(discount) - 9):
        # 이전 구간의 첫 번째 제품 제거
        prev_product = discount[start_day - 1]
        discount_count[prev_product] -= 1
        
        if discount_count[prev_product] == 0:
            del discount_count[prev_product]
        
        # 새 구간의 마지막 제품 추가
        new_product = discount[start_day + 9]
        discount_count[new_product] = discount_count.get(new_product, 0) + 1
        
        # 현재 구간이 조건을 만족하는지 확인
        if want_count == discount_count:
            answer += 1
    
    return answer
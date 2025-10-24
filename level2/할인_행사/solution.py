def solution(want, number, discount):
    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    # 또는 zip 사용
    # want_dict = dict(zip(want, number))
    
    answer = 0
    
    # 10일 연속 확인
    for start in range(len(discount) - 9):
        discount_dict = {}

        for i in range(start, start + 10):
            product = discount[i]
            discount_dict[product] = discount_dict.get(product, 0) + 1
        
        if want_dict == discount_dict:
            answer += 1
    
    return answer
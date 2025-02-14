def solution(order):
    total = 0
    
    for drink in order:
        # 아메리카노 주문 (4500원)
        if 'americano' in drink or drink == 'anything':
            total += 4500
        # 카페라테 주문 (5000원)
        elif 'cafelatte' in drink:
            total += 5000
            
    return total
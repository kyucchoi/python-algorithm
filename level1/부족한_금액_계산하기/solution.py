# 방법 1
def solution(price, money, count):
    total_cost = 0
    
    for ride_count in range(1, count + 1):
        total_cost += ride_count * price
        
    if total_cost > money:
        return total_cost - money
    else:
        return 0

# 방법 2
def solution(price, money, count):
    # 총 필요한 금액: price * (1 + 2 + ... + count)
    total_price = price * (count * (count + 1) // 2)
    
    # 부족한 금액 계산 (0보다 작으면 0으로)
    return max(total_price - money, 0)
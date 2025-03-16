# 방법 1
def solution(price, money, count):
    # 총 필요한 금액 계산
    total_price = 0

    for i in range(1, count + 1):
        total_price += price * i
    
    # 부족한 금액 계산
    shortage = total_price - money
    
    # 부족하지 않으면 0 반환
    return shortage if shortage > 0 else 0

# 방법 2
def solution(price, money, count):
    # 총 필요한 금액: price * (1 + 2 + ... + count)
    total_price = price * (count * (count + 1) // 2)
    
    # 부족한 금액 계산 (0보다 작으면 0으로)
    return max(total_price - money, 0)
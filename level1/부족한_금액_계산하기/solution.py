# 방법 1
def solution(price, money, count):
    total_cost = 0
    
    for ride_count in range(1, count + 1):
        total_cost += ride_count * price
        
    # return max(total_cost - money, 0)
    if total_cost > money:
        return total_cost - money
    else:
        return 0

# 등차수열 방법
def solution(price, money, count):
    total_price = price * count * (count + 1) // 2
    
    return max(total_price - money, 0)
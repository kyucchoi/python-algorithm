# 방법 1
def solution(wallet, bill):
    answer = 0
    
    wallet.sort()
    bill.sort()
    
    # bill의 작은 값이 wallet의 작은 값보다 크거나
    # bill의 큰 값이 wallet의 큰 값보다 큰 동안 반복
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        # bill[0]이 bill[1]보다 크다면 (큰 쪽을 접음)
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        elif bill[0] < bill[1]:
            bill[1] = bill[1] // 2
        
        answer += 1
        
        # 지폐를 다시 작은 값, 큰 값 순으로 정렬 (90도 회전 가능성 고려)
        bill.sort()
    
    return answer

# 방법 2
def solution(wallet, bill):
    answer = 0
    
    while True:
        wallet_min = min(wallet)
        wallet_max = max(wallet)
        bill_min = min(bill)
        bill_max = max(bill)
        
        # 들어가는지 체크 (그대로 또는 90도 회전)
        if bill_min <= wallet_min and bill_max <= wallet_max:
            break
        
        if bill[0] > bill[1]:
            bill[0] //= 2
        elif bill[0] < bill[1]:
            bill[1] //= 2
        
        answer += 1
    
    return answer
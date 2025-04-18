def solution(wallet, bill):
    # 지폐를 접은 횟수를 저장할 변수
    answer = 0
    
    # wallet과 bill을 각각 작은 값과 큰 값으로 정렬
    wallet.sort()
    bill.sort()
    
    # bill의 작은 값이 wallet의 작은 값보다 크거나
    # bill의 큰 값이 wallet의 큰 값보다 큰 동안 반복
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        # bill[0]이 bill[1]보다 크다면 (큰 쪽을 접음)
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2  # 2로 나누고 나머지 버림
        else:
            bill[1] = bill[1] // 2  # 2로 나누고 나머지 버림
        
        # 접었으므로 횟수 증가
        answer += 1
        
        # 지폐를 다시 작은 값, 큰 값 순으로 정렬 (90도 회전 가능성 고려)
        bill.sort()
    
    return answer
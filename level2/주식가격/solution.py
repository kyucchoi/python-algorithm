def solution(prices):
    length = len(prices)
    answer = [0] * length  # 결과를 저장할 리스트를 0으로 초기화
    
    for i in range(length):
        for j in range(i + 1, length):
            answer[i] += 1  # 시간 증가
            
            if prices[i] > prices[j]:  # 가격이 떨어졌으면
                break  # 더 이상 확인하지 않음
                
    return answer
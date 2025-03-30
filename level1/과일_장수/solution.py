# 방법 1
def solution(k, m, score):
    # 사과 점수를 내림차순으로 정렬
    score.sort(reverse = True)
    
    total_profit = 0
    
    # m개씩 상자를 구성하여 이익 계산
    for i in range(m - 1, len(score), m):
        total_profit += score[i] * m
    
    return total_profit

# 방법 2
def solution(k, m, score):
    # 이익 초기화
    total_profit = 0
    
    # 사과 점수를 내림차순으로 정렬
    score.sort(reverse = True)
    
    # m개씩 상자를 구성
    for i in range(0, len(score) // m):
        # 현재 상자의 시작 인덱스
        box_start = i * m
        
        # 현재 상자의 마지막 인덱스
        box_end = box_start + m - 1
        
        # 상자에서 가장 낮은 점수 (마지막 원소)
        min_score = score[box_end]
        
        # 상자의 가격 = 최저 점수 × 상자에 담긴 사과 개수
        box_price = min_score * m
        
        # 총 이익에 더함
        total_profit += box_price
    
    return total_profit
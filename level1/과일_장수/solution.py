# 방법 1
def solution(k, m, score):
    score.sort(reverse = True)
    
    total_profit = 0
    
    for i in range(m - 1, len(score), m):
        total_profit += score[i] * m
    
    return total_profit

# 방법 2
def solution(k, m, score):
    if len(score) < m:
        return 0
    
    score.sort(reverse = True)
    
    answer = 0
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            min_score = score[i + m - 1]
            answer += min_score * m
    
    return answer
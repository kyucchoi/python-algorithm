# 방법 1
def solution(hp):
    a = hp // 5
    b = (hp - (5 * a)) // 3
    c = (hp - ((5 * a) + (3 * b)))
    
    return a + b + c

# 방법 2
def solution(hp):
    answer = 0
    
    if hp >= 5:
        answer += hp // 5
        hp %= 5

    if hp >= 3:
        answer += hp // 3
        hp %= 3

    if hp >= 1:
        answer += hp // 1
        hp %= 1
        
    return answer
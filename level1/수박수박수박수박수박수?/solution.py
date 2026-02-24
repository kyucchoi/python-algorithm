# 방법 1
def solution(n):
    result = ''
    
    for i in range(n):
        if i % 2 == 0:
            result += '수'
        else:
            result += '박'
            
    return result

# 방법 2
def solution(n):
    return ('수박' * n)[:n]

# 내 방법
def solution(n):
    answer = ''
    
    if n % 2 == 0:
        answer += '수박' * (n // 2)
    else:
        answer += '수박' * (n // 2) + '수'
        
    return answer
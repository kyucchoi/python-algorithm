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

# 방법 3
def solution(n):
    if n % 2 == 1:
        return '수박' * (n // 2) + '수'
    else:
        return '수박' * (n // 2)

# 방법 4
def solution(n):
    return '수박' * (n // 2) + '수' * (n % 2)
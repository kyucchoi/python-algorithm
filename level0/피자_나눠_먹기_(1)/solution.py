# 방법 1
def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1
    
# 방법 2
def solution(n):
    return (n - 1) // 7 + 1
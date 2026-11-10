# 방법 1
def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x
        
    return n - 1

# 방법 2
def solution(n):
    m = n - 1
    i = 2

    while i * i <= m:
        if m % i == 0:
            return i
            
        i += 1

    return m
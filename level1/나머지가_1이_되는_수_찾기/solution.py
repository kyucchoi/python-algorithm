def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x
        
    return n - 1  # n - 1은 항상 나머지가 1이 됨
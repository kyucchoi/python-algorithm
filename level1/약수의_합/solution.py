# 방법 1
def solution(n):
    total = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
            
    return total

# 제곱근까지만 확인하기 (O(√n))
def solution(n):
    answer = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            answer += i

            if i != n // i:
                answer += n // i
                
        i += 1

    return answer
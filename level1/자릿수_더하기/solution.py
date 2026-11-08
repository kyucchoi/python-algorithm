# 방법 1
def solution(n):
    digits = str(n)
    answer = 0
    
    for digit in digits:
        answer += int(digit)
        
    return answer

# map 사용
def solution(n):
    return sum(map(int, str(n)))

# 수학적으로 풀기
def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n //= 10
        
    return answer
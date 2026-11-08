# reversed 함수 방법
def solution(n):
    return list(map(int, reversed(str(n))))

# 슬라이싱 방법
def solution(n):
    return list(map(int, str(n)[::-1]))

# 나머지 연산 방법
def solution(n):
    answer = []

    while n > 0:
        answer.append(n % 10)
        n //= 10
        
    return answer
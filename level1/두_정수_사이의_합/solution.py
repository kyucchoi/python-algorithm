# sum + range
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

# 등차수열 합 공식을 쓰면 O(1)
def solution(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
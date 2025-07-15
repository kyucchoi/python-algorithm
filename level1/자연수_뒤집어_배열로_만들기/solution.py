# 방법 1
def solution(n):
    return [int(x) for x in str(n)][::-1]

# 방법 2
def solution(n):
    return [int(x) for x in reversed(str(n))]

# 방법 3
def solution(n):
    return list(map(int, reversed(str(n))))
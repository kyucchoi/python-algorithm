# 방법 1
def solution(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i - 1] * b[i - 1]

    return result

# zip 함수 사용
def solution(a, b):
    return sum(x * y for x, y in zip(a, b))
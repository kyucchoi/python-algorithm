def solution(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i - 1] * b[i - 1]

    return result
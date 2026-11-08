# math.isqrt 방법
import math

def solution(n):
    x = math.isqrt(n)

    if x * x == n:
        return (x + 1) ** 2
    else:
        return -1

# 나머지 연산 방법
def solution(n):
    x = n ** 0.5

    if x == int(x):
        return (int(x) + 1) ** 2
    else:
        return -1

# 이분탐색 방법
def solution(n):
    left, right = 1, n

    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == n:
            return (mid + 1) ** 2
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1
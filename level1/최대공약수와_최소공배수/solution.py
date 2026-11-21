# 방법 1
import math

def solution(n, m):
    g = math.gcd(n, m)

    return [g, n * m // g]

# 유클리드 호제법
def solution(n, m):
    a, b = n, m

    while b > 0:
        a, b = b, a % b

    return [a, n * m // a]
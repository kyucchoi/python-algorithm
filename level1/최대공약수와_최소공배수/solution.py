# 방법 1
def solution(n, m):
    # 최대공약수(GCD) 계산 - 유클리드 알고리즘
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # 최소공배수(LCM) 계산 - GCD를 이용한 공식
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    return [gcd(n, m), lcm(n, m)]

# 방법 2
import math

def solution(n, m):
    # 최대공약수
    gcd_value = math.gcd(n, m)
    
    # 최소공배수
    lcm_value = n * m // gcd_value
    
    return [gcd_value, lcm_value]
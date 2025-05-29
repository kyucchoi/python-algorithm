# 방법 1
def solution(arr):
    # 최대공약수를 구하는 함수 (유클리드 호제법)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # 최소공배수를 구하는 함수
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    # 배열의 모든 원소에 대해 순차적으로 LCM 계산
    result = arr[0]

    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    
    return result

# 방법 2
import math

def solution(arr):
    def lcm(a, b):
        return (a * b) // math.gcd(a, b)
    
    result = arr[0]
    
    for num in arr[1:]:
        result = lcm(result, num)
    
    return result
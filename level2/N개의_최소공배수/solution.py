# 방법 1
def solution(arr):
    # 최대공약수를 구하는 함수 (유클리드 호제법)
    def gcd(a, b):
        while b:
            a, b = b, a % b
            
        return a
    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
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
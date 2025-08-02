# 방법 1
def solution(balls, share):
    # 팩토리얼을 계산하는 함수
    def factorial(n):
        if n <= 1:
            return 1
        
        result = 1

        for i in range(2, n + 1):
            result *= i
            
        return result
    
    # 조합 공식: nCr = n! / (r! * (n-r)!)
    n_factorial = factorial(balls)
    r_factorial = factorial(share)
    nr_factorial = factorial(balls - share)
    
    return n_factorial // (r_factorial * nr_factorial)

# 방법 2
from math import comb

def solution(balls, share):
    return comb(balls, share)
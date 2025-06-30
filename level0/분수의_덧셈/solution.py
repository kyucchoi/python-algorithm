import math

def solution(numer1, denom1, numer2, denom2):
    # 분수 덧셈 계산
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    # 기약 분수로 만들기 위해 최대공약수 계산
    gcd_val = math.gcd(numer, denom)

    # 기약 분수 반환
    return [numer // gcd_val, denom // gcd_val]
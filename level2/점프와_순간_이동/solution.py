# 방법 1
def solution(n):
    battery = 0
    
    while n > 0:
        if n % 2 == 0:  # 현재 위치가 짝수인 경우
            n //= 2     # 순간이동 (현재 위치를 2로 나눔)
        else:           # 현재 위치가 홀수인 경우
            n -= 1      # 1칸 점프 (건전지 1 사용)
            battery += 1
    
    return battery

# 방법 2 (비트 연산 활용)
def solution(n):
    return bin(n).count('1')
# 방법 1
def solution(n):
    # 기저 사례
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1  # 1칸 도달하는 방법: 1가지
    dp[2] = 2  # 2칸 도달하는 방법: 2가지
    
    # 점화식 적용: dp[i] = dp[i - 1] + dp[i - 2]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    return dp[n]

# 방법 2
def solution(n):
    if n <= 2:
        return n
    
    prev1 = 1
    prev2 = 2

    for i in range(3, n + 1):
        current = (prev1 + prev2) % 1234567
        prev1 = prev2
        prev2 = current

    return prev2